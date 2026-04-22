"""
Thin wrapper around a local Ollama chat instance.
This module calls `ollama.chat(...)` and returns the assistant response.
"""

import ollama


def call_llm(system_prompt: str, user_message: str, max_tokens: int = 600) -> str:
    """Call a local Ollama model and return the assistant's content.

    Args:
        system_prompt: system role prompt for the model
        user_message: user message content
        max_tokens: (ignored for Ollama if unsupported) kept for compatibility

    Returns:
        assistant content as string, or an error message starting with ⚠️
    """
    try:
        response = ollama.chat(
            model="llama3.2",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message},
            ],
        )
        # Ollama returns a structure containing the assistant message
        return response.get("message", {}).get("content", "")
    except Exception as e:
        return f"⚠️ Ollama error: {str(e)} — make sure Ollama is running."