"""
Sidebar: student name input, navigation, and knowledge-map overview.
"""

import streamlit as st


def render_sidebar() -> None:
    with st.sidebar:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("## MathMentor AI")
        st.caption("Adaptive Math Practice")

        st.divider()

        st.markdown("### Student")
        name = st.text_input("Your Name", value=st.session_state.student_name, label_visibility="collapsed", placeholder="Enter your name")
        if name:
            st.session_state.student_name = name

        st.divider()

        st.markdown("### Navigate")
        nav_items = [
            ("🏠  Home", "home"),
            ("🎯  Practice", "practice"),
            ("🐛  Debug the AI", "debug"),
            ("💬  Ask the Tutor", "chat"),
            ("📈  My Progress", "progress"),
        ]
        for label, mode in nav_items:
            if st.button(label, use_container_width=True, key=f"nav_{mode}"):
                st.session_state.mode = mode
                st.rerun()

        if st.session_state.mastery:
            st.divider()
            st.markdown("### Knowledge Map")
            for concept, val in sorted(st.session_state.mastery.items(), key=lambda x: x[1]):
                pct = int(val * 100)
                color = "#d20f39" if pct < 40 else "#df8e1d" if pct < 70 else "#40a02b"
                st.markdown(
                    f'<div style="display:flex;justify-content:space-between;margin:6px 0 2px;">'
                    f'<span style="font-size:0.8rem;">{concept}</span>'
                    f'<span style="font-size:0.8rem;font-weight:600;color:{color};">{pct}%</span>'
                    f'</div>',
                    unsafe_allow_html=True,
                )
                st.progress(val)
