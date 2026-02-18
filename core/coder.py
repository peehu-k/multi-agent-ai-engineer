import subprocess

MODEL = "phi3"

def generate_code(task, context="", memory=""):
    """
    Generates production-quality Python code.
    """

    prompt = f"""
You are a FAANG-level senior Python engineer.

Write COMPLETE runnable Python code.

TASK:
{task}

STRICT RULES:
- Only Python code
- No explanation
- No markdown
- Must run directly
- Production quality
- Proper structure
"""

    try:
        result = subprocess.run(
            ["ollama", "run", MODEL, prompt],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="ignore",
            timeout=180
        )

        raw = result.stdout.strip()

        raw = raw.replace("```python", "").replace("```", "")

        with open("generated_code.py", "w", encoding="utf-8") as f:
            f.write(raw)

        return raw

    except Exception as e:
        return f"print('generation failed:', {str(e)})"
