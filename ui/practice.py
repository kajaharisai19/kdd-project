"""
Practice mode: adaptive question selection, answer grading, and AI feedback.
"""

import streamlit as st

from data.content import TOPICS
from services.feedback import get_adaptive_feedback
from services.knowledge import get_adaptive_question, log_error, update_mastery


def _check_answer(student_answer: str, correct_answer: str) -> bool:
    """Keyword / substring matching for answer correctness."""
    correct_lower = correct_answer.lower().replace(" ", "")
    student_lower = student_answer.lower().replace(" ", "")
    return any(part in student_lower for part in correct_lower.split("or")) or correct_lower in student_lower


def render_practice() -> None:
    st.markdown("<h1>🎯 Adaptive Practice</h1>", unsafe_allow_html=True)
    st.markdown(
        '<p style="color:#94A3B8; margin-top:-0.5rem;">Questions adapt to your knowledge state in real time</p>',
        unsafe_allow_html=True,
    )

    # Topic selector
    topic_cols = st.columns(len(TOPICS))
    for i, (t, info) in enumerate(TOPICS.items()):
        with topic_cols[i]:
            if st.button(f"{info['icon']} {t}", key=f"topic_{t}", use_container_width=True):
                st.session_state.topic = t
                st.session_state.question_idx = 0
                st.session_state.show_hint = False
                st.session_state.debug_mode_feedback = None
                st.rerun()

    if not st.session_state.topic:
        st.markdown("""
        <div class='card card-accent' style='text-align:center; margin-top:2rem;'>
            <p style='font-size:1rem; color:#94A3B8;'>👆 Select a topic above to begin adaptive practice</p>
        </div>
        """, unsafe_allow_html=True)
        return

    topic = st.session_state.topic
    question = get_adaptive_question(topic)
    q_key = f"{topic}_{question['q'][:20]}"

    st.markdown("---")

    # Question header
    mastery_val = st.session_state.mastery.get(question["concept"], 0.3)
    diff_label = ["", "Foundational", "Developing", "Advanced"][question["difficulty"]]
    diff_color = ["", "#16A34A", "#B45309", "#DC2626"][question["difficulty"]]

    col_q, col_info = st.columns([3, 1])
    with col_q:
        st.markdown(f"""
        <div class='section-header'>
            <h3>{TOPICS[topic]['icon']} {topic} — {question['concept']}</h3>
        </div>
        """, unsafe_allow_html=True)
    with col_info:
        st.markdown(
            f'<div style="text-align:right; padding-top:0.5rem;">'
            f'<span class="badge" style="background:rgba(0,0,0,0.2);color:{diff_color}!important;border-color:{diff_color};">'
            f"{diff_label}</span><br>"
            f'<span style="font-size:0.75rem;color:#64748B;">Mastery: {mastery_val:.0%}</span>'
            f"</div>",
            unsafe_allow_html=True,
        )

    st.markdown(f"""
    <div class='card' style='margin-top:0.5rem;'>
        <p style='font-size:1.15rem; color:#1e1e2e; font-weight:500;'>{question['q']}</p>
    </div>
    """, unsafe_allow_html=True)

    attempt_count = st.session_state.attempts.get(q_key, 0)

    student_answer = st.text_input(
        "Your Answer:",
        key=f"ans_{q_key}_{attempt_count}",
        placeholder="Type your answer here...",
    )

    col_submit, col_hint, col_next = st.columns([2, 1, 1])
    with col_submit:
        submitted = st.button("✅ Submit Answer", use_container_width=True, key=f"sub_{q_key}")
    with col_hint:
        if st.button("💡 Hint", use_container_width=True, key=f"hint_{q_key}"):
            st.session_state.show_hint = True
            st.session_state.hint_used.add(q_key)
    with col_next:
        if st.button("⏭ Next Question", use_container_width=True, key=f"next_{q_key}"):
            st.session_state.question_idx += 1
            st.session_state.show_hint = False
            st.session_state.debug_mode_feedback = None
            st.rerun()

    if st.session_state.show_hint:
        st.markdown(f"""
        <div class='card card-warn'>
            <p style='margin:0; font-size:0.9rem;'>💡 <strong style='color:#FCD34D;'>Hint:</strong> {question['hint']}</p>
        </div>
        """, unsafe_allow_html=True)

    if submitted and student_answer.strip():
        st.session_state.attempts[q_key] = attempt_count + 1
        st.session_state.total_attempted += 1

        is_correct = _check_answer(student_answer, question["answer"])

        if is_correct:
            st.session_state.total_correct += 1
            st.session_state.streak += 1
            update_mastery(question["concept"], True)
            st.markdown("""
            <div class='card card-ok'>
                <p style='font-size:1.1rem; margin:0;'>✅ <strong style='color:#86EFAC;'>Correct!</strong> Great work!</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.session_state.streak = 0
            update_mastery(question["concept"], False)
            log_error(question["concept"], f"answered '{student_answer}' instead of '{question['answer']}'")
            st.markdown(f"""
            <div class='card card-err'>
                <p style='font-size:1rem; margin:0;'>❌ <strong style='color:#FCA5A5;'>Not quite.</strong>
                The correct answer is: <code>{question['answer']}</code></p>
            </div>
            """, unsafe_allow_html=True)

        with st.spinner("🤖 Generating personalized feedback..."):
            feedback = get_adaptive_feedback(question, student_answer, is_correct, topic)

        st.markdown(f"""
        <div class='card card-accent' style='margin-top:1rem;'>
            <div style='display:flex;align-items:center;gap:8px;margin-bottom:0.5rem;'>
                <span style='font-size:1.2rem;'>🤖</span>
                <strong style='color:#0D9488;'>MathMentor Feedback</strong>
                <span class='badge badge-teal'>Adaptive · Personalized</span>
            </div>
            <p style='margin:0; line-height:1.7;'>{feedback}</p>
        </div>
        """, unsafe_allow_html=True)
