"""
Chat mode: free-form tutoring conversation with error-history context.
"""

import streamlit as st

from data.content import TOPICS
from services.feedback import get_chat_response


def render_chat() -> None:
    st.markdown("<h1>💬 Ask the Tutor</h1>", unsafe_allow_html=True)
    st.markdown(
        '<p style="color:#94A3B8; margin-top:-0.5rem;">'
        "Your personal AI tutor — adapts every response to your error history and mastery level</p>",
        unsafe_allow_html=True,
    )

    chat_topic = st.selectbox("Topic context:", list(TOPICS.keys()), key="chat_topic_sel")

    for msg in st.session_state.chat_history:
        if msg["role"] == "user":
            st.markdown(
                f'<div class="bubble-user"><strong>You:</strong> {msg["content"]}</div>',
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f'<div class="bubble-ai"><strong>🤖 MathMentor:</strong> {msg["content"]}</div>',
                unsafe_allow_html=True,
            )

    user_msg = st.text_input(
        "Ask anything about math:",
        key="chat_input",
        placeholder="e.g. Can you explain how to factor quadratics?",
    )

    col_send, col_clear = st.columns([3, 1])
    with col_send:
        if st.button("📤 Send", use_container_width=True, key="chat_send"):
            if user_msg.strip():
                st.session_state.chat_history.append({"role": "user", "content": user_msg})
                with st.spinner("Thinking..."):
                    response = get_chat_response(user_msg, chat_topic)
                st.session_state.chat_history.append({"role": "assistant", "content": response})
                st.rerun()
    with col_clear:
        if st.button("🗑 Clear", use_container_width=True, key="chat_clear"):
            st.session_state.chat_history = []
            st.rerun()
