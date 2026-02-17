import subprocess

def understand_task(task):

    prompt = f"""
Convert this request into ONE clear software engineering instruction.

Rules:
- Only one sentence
- No code
- No markdown
- Plain English only

Request: {task}
"""

    try:
        result = subprocess.run(
            ["ollama", "run", "phi3", prompt],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="ignore",
            timeout=60
        )

        clarified = result.stdout.strip()
        clarified = clarified.replace("```","").replace("python","")

        if len(clarified) < 10:
            return f"Create a Python tool for: {task}"

        return clarified

    except:
        return f"Create a Python tool for: {task}"
