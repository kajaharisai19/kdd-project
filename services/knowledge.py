"""
Knowledge tracing: mastery updates, error logging, and adaptive question selection.

Grounded in:
  - Wen et al. (AI4EDU @ KDD '24) — session-state knowledge tracing
  - Lane (IJAIED '23) — ZPD-aware difficulty selection
"""

from collections import Counter
from datetime import datetime

import streamlit as st

from data.content import TOPICS


def update_mastery(concept: str, correct: bool) -> None:
    """Simplified Bayesian-style knowledge tracing update."""
    current = st.session_state.mastery.get(concept, 0.3)
    learn_rate = 0.15 if correct else -0.1
    slip = 0.05
    if correct:
        new_val = current + learn_rate * (1 - current) - slip * current
    else:
        new_val = current + learn_rate * (1 - current)
    st.session_state.mastery[concept] = max(0.0, min(1.0, new_val))


def log_error(concept: str, error_description: str) -> None:
    st.session_state.error_log.append({
        "concept": concept,
        "error": error_description,
        "timestamp": datetime.now().strftime("%H:%M"),
    })


def get_error_summary() -> str:
    """Summarise recent student errors for the AI system prompt."""
    if not st.session_state.error_log:
        return "No errors recorded yet."
    concept_errors = Counter(e["concept"] for e in st.session_state.error_log)
    lines = []
    for concept, count in concept_errors.most_common(3):
        recent = [e["error"] for e in st.session_state.error_log if e["concept"] == concept][-2:]
        lines.append(f"- {concept} ({count} error(s)): {'; '.join(recent)}")
    return "\n".join(lines)


def get_adaptive_question(topic: str) -> dict:
    """Select the next question based on mastery and ZPD principles."""
    questions = TOPICS[topic]["questions"]
    mastery = st.session_state.mastery

    def priority(q: dict) -> float:
        concept_mastery = mastery.get(q["concept"], 0.3)
        diff = q["difficulty"]
        # Avoid too easy (well-mastered) or too hard (no foundation yet)
        if concept_mastery > 0.85 and diff == 1:
            return 0.1
        if concept_mastery < 0.15 and diff == 3:
            return 0.2
        return (1 - concept_mastery) * (1 + 0.2 * diff)

    scored = sorted(questions, key=priority, reverse=True)
    idx = st.session_state.question_idx % len(scored)
    return scored[idx]
