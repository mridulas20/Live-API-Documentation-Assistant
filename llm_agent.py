import subprocess

def answer_with_llm(query, context):
    prompt = f"""
You are an API documentation assistant.

Question:
{query}

Relevant documentation:
{context}

Answer clearly and concisely.
"""

    result = subprocess.run(
        ["ollama", "run", "llama3"],
        input=prompt,
        text=True,
        capture_output=True
    )

    return result.stdout
