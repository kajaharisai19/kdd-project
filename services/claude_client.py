"""
Thin wrapper around the Anthropic Claude API.
API key is loaded from the .env file (ANTHROPIC_API_KEY).
"""

import os

# import anthropic
# from dotenv import load_dotenv

# load_dotenv()

# _API_KEY = os.getenv("ANTHROPIC_API_KEY", "")


# def call_claude(system_prompt: str, user_message: str, max_tokens: int = 600) -> str:
#     """Call Claude API using the key from .env."""
#     if not _API_KEY:
#         return "⚠️ ANTHROPIC_API_KEY not set in .env file."
#     try:
#         client = anthropic.Anthropic(api_key=_API_KEY)
#         msg = client.messages.create(
#             model="claude-opus-4-5",
#             max_tokens=max_tokens,
#             system=system_prompt,
#             messages=[{"role": "user", "content": user_message}],
#         )
#         return msg.content[0].text
#     except Exception as e:
#         return f"⚠️ API error: {str(e)}"


import ollama

def call_claude(system_prompt: str, user_message: str, max_tokens: int = 600) -> str:
    try:
        response = ollama.chat(
            model="llama3.2",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user",   "content": user_message},
            ]
        )
        return response["message"]["content"]
    except Exception as e:
        return f"⚠️ Ollama error: {str(e)} — make sure Ollama is running."