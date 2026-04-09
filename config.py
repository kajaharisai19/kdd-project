"""
Flat design theme — clean, modern, classroom-appropriate.
"""

import streamlit as st

THEME_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background-color: #f0f2f5;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #1e1e2e;
}
section[data-testid="stSidebar"] * { color: #cdd6f4 !important; }
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: #cba6f7 !important;
    font-size: 0.85rem !important;
    text-transform: uppercase;
    letter-spacing: 0.08em;
}
section[data-testid="stSidebar"] .stButton button {
    background: #313244 !important;
    color: #cdd6f4 !important;
    border: none !important;
    border-radius: 6px !important;
    font-size: 0.88rem !important;
    text-align: left !important;
    font-weight: 500 !important;
}
section[data-testid="stSidebar"] .stButton button:hover {
    background: #45475a !important;
}

/* Name input — black text on white */
section[data-testid="stSidebar"] .stTextInput input {
    color: #000000 !important;
    background: #ffffff !important;
    border: 1px solid #45475a !important;
    border-radius: 6px !important;
}

/* Main content headings */
h1 { color: #11111b !important; font-size: 1.8rem !important; font-weight: 700 !important; }
h2 { color: #1e1e2e !important; font-weight: 600 !important; }
h3 { color: #1e1e2e !important; font-weight: 600 !important; }

/* Flat cards */
.card {
    background: #ffffff;
    border-radius: 10px;
    padding: 1.1rem 1.3rem;
    margin-bottom: 0.75rem;
    box-shadow: 0 1px 3px rgba(0,0,0,0.08);
}
.card-ok   { border-left: 4px solid #40a02b; background: #f4fbf0; }
.card-err  { border-left: 4px solid #d20f39; background: #fff5f7; }
.card-warn { border-left: 4px solid #df8e1d; background: #fffbf0; }
.card-info { border-left: 4px solid #1e66f5; background: #f0f5ff; }

/* Mode cards on home */
.mode-card {
    background: #ffffff;
    border-radius: 10px;
    padding: 1.2rem;
    box-shadow: 0 1px 3px rgba(0,0,0,0.08);
    height: 100%;
}
.mode-card h4 {
    margin: 0 0 0.4rem !important;
    color: #1e1e2e !important;
    font-size: 1rem !important;
    font-weight: 600 !important;
}
.mode-card p {
    color: #6c6f85 !important;
    font-size: 0.85rem !important;
    margin: 0 !important;
}

/* Stat cards */
[data-testid="stMetric"] {
    background: #ffffff;
    border-radius: 10px;
    padding: 0.8rem 1rem;
    box-shadow: 0 1px 3px rgba(0,0,0,0.07);
}
[data-testid="stMetricLabel"] { color: #6c6f85 !important; font-size: 0.8rem !important; }
[data-testid="stMetricValue"] { color: #1e1e2e !important; font-weight: 700 !important; }

/* Buttons */
.stButton button {
    background: #1e66f5 !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 6px !important;
    font-weight: 500 !important;
    font-size: 0.88rem !important;
}
.stButton button:hover {
    background: #1a56d6 !important;
}

/* Text inputs */
.stTextInput input, .stTextArea textarea {
    background: #ffffff !important;
    color: #000000 !important;
    border: 1px solid #ccd0da !important;
    border-radius: 6px !important;
    font-size: 0.95rem !important;
    caret-color: #000000 !important;
}
.stTextInput input::placeholder, .stTextArea textarea::placeholder {
    color: #9ca3af !important;
    opacity: 1 !important;
}
.stTextInput input:focus, .stTextArea textarea:focus {
    border-color: #1e66f5 !important;
    box-shadow: 0 0 0 2px rgba(30,102,245,0.15) !important;
}

/* Selectbox */
.stSelectbox > div > div {
    background: #ffffff !important;
    color: #1e1e2e !important;
    border: 1px solid #ccd0da !important;
    border-radius: 6px !important;
}

/* Progress bar */
.stProgress > div > div {
    background: #1e66f5 !important;
    border-radius: 4px !important;
}

/* Divider */
hr { border-color: #e5e7eb !important; }

/* Flawed AI box */
.flawed-box {
    background: #fffbf0;
    border: 2px dashed #df8e1d;
    border-radius: 8px;
    padding: 1rem 1.2rem;
    font-family: 'Courier New', monospace;
    font-size: 0.88rem;
    color: #4a4a4a;
    line-height: 1.6;
}

/* Chat bubbles */
.bubble-ai {
    background: #ffffff;
    border: 1px solid #e5e7eb;
    border-radius: 0 10px 10px 10px;
    padding: 0.8rem 1rem;
    margin: 0.4rem 0;
    color: #1e1e2e;
    font-size: 0.92rem;
    box-shadow: 0 1px 2px rgba(0,0,0,0.05);
}
.bubble-user {
    background: #e7effd;
    border-radius: 10px 0 10px 10px;
    padding: 0.8rem 1rem;
    margin: 0.4rem 0 0.4rem 3rem;
    color: #1e1e2e;
    font-size: 0.92rem;
}

/* Section label */
.section-label {
    font-size: 0.72rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.07em;
    color: #6c6f85;
    margin-bottom: 0.5rem;
}
</style>
"""


def apply_theme():
    st.markdown(THEME_CSS, unsafe_allow_html=True)
