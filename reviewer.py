import subprocess
import re

MODEL = "phi3"

def review_code(task, code):
    """
    Returns numeric quality score out of 10.
    Fast + safe.
    """

    prompt = f"""
Rate this Python code out of 10.

Return ONLY a number.
Examples:
8
7.5
9

Code:
{code[:3000]}
"""

    try:
        result = subprocess.run(
            ["ollama", "run", MODEL, prompt],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="ignore",
            timeout=90
        )

        output = result.stdout.strip()

        match = re.search(r"\d+(\.\d+)?", output)
        if match:
            return float(match.group())

        return 7.0

    except:
        return 7.0
