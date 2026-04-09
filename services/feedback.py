"""
AI-generated feedback functions for each learning mode.

Each function builds a context-rich system prompt grounded in:
  - Wen et al. (AI4EDU @ KDD '24) — adaptive, error-aware feedback
  - Lane (IJAIED '23) — ZPD scaffolding, AI literacy
  - Bloom's Taxonomy — push toward higher-order thinking
"""

import json

import streamlit as st

from data.content import FLAWED_EXPLANATIONS
from services.claude_client import call_claude
from services.knowledge import get_error_summary


def get_adaptive_feedback(question: dict, student_answer: str, is_correct: bool, topic: str) -> str:
    """Personalised feedback grounded in the AI4EDU + ZPD framework."""
    error_history = get_error_summary()
    mastery_snapshot = {k: f"{v:.0%}" for k, v in st.session_state.mastery.items()}

    system = f"""You are MathMentor, an adaptive AI tutor grounded in:
1. Vygotsky's Zone of Proximal Development — meet the student at their level, neither too easy nor too hard
2. Scaffolding theory (Lane 2023) — provide just-in-time support that fades as mastery grows
3. Bloom's Taxonomy — push toward analysis and evaluation, not just recall
4. AI4EDU (KDD 2024) — you adapt based on tracked error patterns, not generic responses

Student profile:
- Name: {st.session_state.student_name}
- Topic: {topic}
- Current mastery levels: {json.dumps(mastery_snapshot)}
- Recent error patterns:
{error_history}
- Streak: {st.session_state.streak} correct in a row
- Hint was used: {question.get('idx', 0) in st.session_state.hint_used}

Your feedback rules:
- If correct AND high streak: challenge with a harder extension question
- If correct AND low mastery: reinforce WHY it's correct, connect to the concept
- If incorrect: diagnose the specific error pattern, give a Socratic nudge (ask a guiding question), NOT the answer directly
- Keep responses concise (3-5 sentences max)
- NEVER be condescending; be encouraging but intellectually rigorous
- Reference their specific error history if relevant (e.g., "I notice you've had trouble with sign errors before...")
- End with one targeted follow-up question to deepen understanding"""

    user = f"""Question: {question['q']}
Correct answer: {question['answer']}
Concept: {question['concept']}
Difficulty: {question['difficulty']}/3
Student's answer: "{student_answer}"
Was correct: {is_correct}
Common errors for this type: {', '.join(question.get('common_errors', []))}

Generate personalized adaptive feedback:"""

    return call_claude(system, user, max_tokens=350)


def get_debug_feedback(flawed_explanation: str, student_critique: str, topic: str, concept: str) -> str:
    """Evaluate a student's critique of a deliberately flawed AI explanation."""
    known_errors = FLAWED_EXPLANATIONS.get(topic, {}).get(concept, {}).get("errors", [])

    system = f"""You are evaluating a student's ability to spot errors in an AI-generated math explanation.
This is the "Debugging the AI" mode — inspired by Lane (2023)'s call for AI literacy and critical evaluation skills.

The task tests Bloom's top-tier skills: evaluating and critiquing AI outputs.
The student must identify what is WRONG in the AI's reasoning and explain the correction.

Topic: {topic}, Concept: {concept}
Known errors in the flawed explanation: {json.dumps(known_errors)}

Evaluate the student's critique:
- Did they identify the core error(s)?
- Did they explain WHY it's wrong (not just that it's wrong)?
- Did they give or suggest the correct reasoning?
- Are they demonstrating understanding, or just guessing?

Give:
1. A score: Found It (full credit) / Partial (caught some errors) / Missed It (didn't find the key error)
2. Specific feedback on what they caught and what they missed
3. A brief explanation of ALL errors in the flawed explanation
4. One extension question to deepen their understanding

Keep it encouraging but rigorous. 4-6 sentences."""

    user = f"""Flawed AI explanation shown to student:
{flawed_explanation}

Student's critique:
"{student_critique}"

Evaluate their response:"""

    return call_claude(system, user, max_tokens=400)


def get_chat_response(user_message: str, topic: str) -> str:
    """Free-form tutoring chat with full error-history context."""
    error_history = get_error_summary()
    mastery_snapshot = {k: f"{v:.0%}" for k, v in st.session_state.mastery.items()}

    history_text = ""
    for msg in st.session_state.chat_history[-6:]:
        history_text += f"\n{msg['role'].upper()}: {msg['content']}"

    system = f"""You are MathMentor, a personalized AI math tutor.
Student: {st.session_state.student_name}
Current topic: {topic}
Mastery profile: {json.dumps(mastery_snapshot)}
Error patterns to be aware of: {error_history}

You adapt every response to THIS student's specific weaknesses.
Use scaffolding: give hints and guiding questions before full solutions.
Keep responses focused and pedagogically sound (Lane 2023, AI4EDU KDD'24).
Max 4 sentences unless showing a worked example."""

    user = f"""Conversation so far:{history_text}

Student: {user_message}"""

    return call_claude(system, user, max_tokens=400)
