"""
AI-Enhanced Personalized Math Learning System
============================================
Grounded in:
  1. Wen et al. (2024) AI4EDU @ KDD '24 — LLMs as adaptive human-in-loop interfaces
  2. Lane (2023) IJAIED Commentary on K-12 AI Education — ZPD, scaffolding, AI literacy

Hybrid architecture:
  - Streamlit frontend (interactive demo)
  - Claude API backend (adaptive LLM tutor)
  - Session-state knowledge tracing (error-pattern tracking)
  - "Debugging the AI" mode — student corrects a flawed AI explanation (Bloom's top tier)
"""

import streamlit as st

from config import apply_theme
from state import init_session
from ui.sidebar import render_sidebar
from ui.home import render_home
from ui.practice import render_practice
from ui.debug import render_debug
from ui.chat import render_chat
from ui.progress import render_progress

# ─── Page config ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="MathMentor AI",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="expanded",
)

apply_theme()
init_session()
render_sidebar()

# ─── Route to active mode ─────────────────────────────────────────────────────
mode = st.session_state.mode

if mode == "home":
    render_home()
elif mode == "practice":
    render_practice()
elif mode == "debug":
    render_debug()
elif mode == "chat":
    render_chat()
elif mode == "progress":
    render_progress()
