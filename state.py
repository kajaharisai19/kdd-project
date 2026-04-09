"""
Session state initialisation for MathMentor AI.
"""

import streamlit as st


def init_session():
    defaults = {
        "mode": "home",
        "topic": None,
        "question_idx": 0,
        "error_log": [],          # knowledge tracing: {concept, error_type, timestamp}
        "mastery": {},            # concept -> 0..1 float
        "attempts": {},           # q_key -> attempt count
        "chat_history": [],       # [{role, content}]
        "streak": 0,
        "total_correct": 0,
        "total_attempted": 0,
        "hint_used": set(),
        "debug_mode_feedback": None,
        "student_name": "Student",
        "show_hint": False,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value
