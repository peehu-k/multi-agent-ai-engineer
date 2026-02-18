import subprocess

MODEL = "phi3"

def debug_code(task, code):
    """
    Improves or fixes code.
    Returns improved code or None.
    """

    prompt = f"""
You are a senior Python engineer.

Fix bugs and improve this code.

TASK:
{task}

CODE:
{code[:3500]}

Rules:
- Return ONLY Python code
- No explanation
- Production quality
"""

    try:
        result = subprocess.run(
            ["ollama", "run", MODEL, prompt],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="ignore",
            timeout=120
        )

        fixed = result.stdout.strip()
        fixed = fixed.replace("```python", "").replace("```", "")

        if fixed and len(fixed) > 20:
            return fixed

        return None

    except:
        return None
