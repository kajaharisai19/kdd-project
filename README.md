# MathMentor AI

AI-Enhanced Personalized Math Learning System

## Features

- Streamlit-based interactive frontend (`app.py`).
- Topic-driven question bank and flawed-AI explanations in `data/content.py`.
- Lightweight service layer for calling LLMs (Ollama) in `services/`.
- Session-state tracking in `state.py` for simple knowledge tracing and progress.
- Modular UI in `ui/` (home, practice, debug, chat, progress, sidebar).
- Theming via `config.py` (Streamlit CSS overrides).

## Quick start (recommended)

Prerequisites

- Python 3.10+ (3.8+ may work but 3.10+ is recommended).
- git
- Optionally: Ollama installed and running locally if you prefer local LLMs.

1. Clone the repo

```bash
git clone <repo-url>
cd KDD-project
```

2. Create and activate a virtual environment (macOS / zsh)

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install Python dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Note: `requirements.txt` currently pins `streamlit`. If you use the Ollama client, install the `ollama` package (it is included in the recommended requirements in this repo):

```bash
pip install ollama
```

4. Configuration

- The UI theme is defined in `config.py`. Call `apply_theme()` is already wired into `app.py`.
The app is configured to use a local Ollama instance by default (see `services/llm_client.py`). Make sure Ollama is installed and the Ollama daemon is running locally; refer to the Ollama docs for install and run instructions.

5. Run the app (Streamlit)

```bash
streamlit run app.py
```

The app will open in your browser at the address printed by Streamlit (usually `http://localhost:8501`).

## Project layout

- `app.py` — entrypoint; wiring of Streamlit pages and session state.
- `config.py` — Streamlit CSS theme and `apply_theme()` helper.
- `state.py` — session initialization and helper functions used across UI pages.
- `data/content.py` — static question bank and flawed explanations.
- `services/` — small service wrappers for model calls and feedback/knowledge helpers. See `services/llm_client.py`.
- `ui/` — Streamlit page components (home, practice, debug, chat, progress, sidebar).

## Development notes

- If you run into `Ollama error: make sure Ollama is running.` it means the Python client couldn't reach a local Ollama instance; start Ollama before running the app.
- Streamlit hot reloads UI changes automatically. If you change Python modules, you may need to restart the Streamlit process.

## Extending the dataset

Edit `data/content.py` to add topics, questions, hints, difficulty levels, common errors, and flawed explanations. The UI reads this module to render practice items and flawed-explanation exercises.

## Troubleshooting

Missing dependencies: re-run `pip install -r requirements.txt`.
For Ollama, consult the Ollama docs; ensure the model you reference (e.g., `llama3.2`) is available locally.
