"""
Progress mode: concept mastery breakdown, error log, and reset.
"""

import streamlit as st


def render_progress() -> None:
    st.markdown("<h1>📈 My Learning Progress</h1>", unsafe_allow_html=True)
    st.markdown(
        '<p style="color:#94A3B8; margin-top:-0.5rem;">'
        "Your personalized knowledge map — built from your actual error patterns</p>",
        unsafe_allow_html=True,
    )

    # Summary stats
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("Questions Attempted", st.session_state.total_attempted)
    with c2:
        acc = f"{st.session_state.total_correct / max(1, st.session_state.total_attempted) * 100:.0f}%"
        st.metric("Overall Accuracy", acc)
    with c3:
        st.metric("Current Streak 🔥", st.session_state.streak)
    with c4:
        avg_m = sum(st.session_state.mastery.values()) / max(1, len(st.session_state.mastery))
        st.metric("Average Mastery", f"{avg_m:.0%}" if st.session_state.mastery else "—")

    st.markdown("---")

    if st.session_state.mastery:
        st.markdown("### 🧠 Concept Mastery Breakdown")
        for concept, val in sorted(st.session_state.mastery.items(), key=lambda x: x[1]):
            pct = int(val * 100)
            status = "🔴 Needs Work" if pct < 40 else "🟡 Developing" if pct < 70 else "🟢 Strong"
            col_l, col_p, col_r = st.columns([2, 4, 1])
            with col_l:
                st.markdown(f'<p style="margin:0.5rem 0; color:#E8F4F8;">{concept}</p>', unsafe_allow_html=True)
            with col_p:
                st.progress(val)
            with col_r:
                st.markdown(f'<p style="margin:0.5rem 0; font-size:0.8rem;">{status}</p>', unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class='card card-accent' style='text-align:center;'>
            <p style='color:#94A3B8;'>Complete some practice questions to see your knowledge map!</p>
        </div>
        """, unsafe_allow_html=True)

    if st.session_state.error_log:
        st.markdown("---")
        st.markdown("### 🔍 Recent Error Log")
        st.markdown(
            '<p style="font-size:0.85rem; color:#64748B;">This is how the AI tracks your patterns to adapt question selection:</p>',
            unsafe_allow_html=True,
        )
        for entry in reversed(st.session_state.error_log[-10:]):
            st.markdown(f"""
            <div class='card card-err' style='padding:0.7rem 1rem; margin-bottom:0.4rem;'>
                <span style='font-size:0.8rem; color:#94A3B8;'>{entry['timestamp']}</span>
                <span style='font-size:0.8rem; color:#FCA5A5; margin-left:1rem;'>
                <strong>{entry['concept']}:</strong> {entry['error']}
                </span>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""
    <div class='card card-accent'>
        <h3 style='margin:0 0 0.5rem; font-size:1rem;'>📚 How This Knowledge Map Works</h3>
        <p style='font-size:0.85rem; color:#94A3B8; margin:0;'>
        This dashboard implements the <strong style='color:#0D9488;'>knowledge tracing</strong> methodology
        from <strong>Wen et al. (AI4EDU, KDD '24)</strong>: student interactions are logged, error patterns
        are detected, and a mastery estimate per concept is maintained. The adaptive question selector
        targets your weakest concepts within your Zone of Proximal Development
        (<strong>Lane, IJAIED 2023</strong>) — never too easy, never too hard.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🗑 Reset All Progress", key="reset_all"):
        for key in ["error_log", "mastery", "attempts", "chat_history", "hint_used",
                    "streak", "total_correct", "total_attempted"]:
            val = st.session_state[key]
            if isinstance(val, dict):
                st.session_state[key] = {}
            elif isinstance(val, list):
                st.session_state[key] = []
            elif isinstance(val, set):
                st.session_state[key] = set()
            else:
                st.session_state[key] = 0
        st.success("Progress reset.")
        st.rerun()
