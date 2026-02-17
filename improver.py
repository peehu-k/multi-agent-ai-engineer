import subprocess

def improve_code(task, code, memory):

    prompt = f"""
Improve this Python code.

Task: {task}

Code:
{code[:2500]}

Make it:
- cleaner
- more efficient
- production quality

Return ONLY improved Python code.
"""

    try:
        result = subprocess.run(
            ["ollama", "run", "phi3", prompt],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="ignore",
            timeout=120
        )

        improved = result.stdout.strip()
        improved = improved.replace("```python","").replace("```","")

        if len(improved) > 20:
            return improved
        return code

    except:
        return code
