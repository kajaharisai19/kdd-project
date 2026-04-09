"""
Home dashboard: stats and mode selection.
"""

import streamlit as st


def render_home() -> None:
    st.title(f"Welcome, {st.session_state.student_name} 👋")
    st.write("Choose a learning mode to get started.")

    st.divider()

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Attempted", st.session_state.total_attempted)
    acc = f"{st.session_state.total_correct / max(1, st.session_state.total_attempted) * 100:.0f}%"
    col2.metric("Accuracy", acc)
    col3.metric("Streak", st.session_state.streak)
    avg_mastery = sum(st.session_state.mastery.values()) / max(1, len(st.session_state.mastery))
    col4.metric("Avg Mastery", f"{avg_mastery:.0%}" if st.session_state.mastery else "—")

    st.divider()

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="mode-card">
            <h4>🎯 Practice</h4>
            <p>Adaptive questions that target your weak areas. Difficulty adjusts based on your performance.</p>
        </div>
        """, unsafe_allow_html=True)
        st.write("")
        if st.button("Start Practicing", key="btn_practice", use_container_width=True):
            st.session_state.mode = "practice"
            st.rerun()

    with c2:
        st.markdown("""
        <div class="mode-card">
            <h4>🐛 Debug the AI</h4>
            <p>The AI gives a deliberately wrong explanation. Your job is to find and correct the errors.</p>
        </div>
        """, unsafe_allow_html=True)
        st.write("")
        if st.button("Debug the AI", key="btn_debug", use_container_width=True):
            st.session_state.mode = "debug"
            st.rerun()

    with c3:
        st.markdown("""
        <div class="mode-card">
            <h4>💬 Ask the Tutor</h4>
            <p>Chat with the AI tutor. It adapts every response based on your error history.</p>
        </div>
        """, unsafe_allow_html=True)
        st.write("")
        if st.button("Open Chat", key="btn_chat", use_container_width=True):
            st.session_state.mode = "chat"
            st.rerun()
