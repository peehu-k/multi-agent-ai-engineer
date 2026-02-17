import subprocess

MODEL = "phi3"

def design_system(task):
    """
    Breaks big tasks into modules.
    Example: 'build trading bot' → multiple tools
    """

    prompt = f"""
You are a senior software architect.

If this task requires multiple modules,
break into a list of sub-tools.

If simple tool → return ONLY original task.

Return each module on new line.
No explanation.

TASK:
{task}
"""

    try:
        result = subprocess.run(
            ["ollama", "run", MODEL, prompt],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="ignore",
            timeout=60
        )

        text = result.stdout.strip()
        lines = [l.strip() for l in text.split("\n") if l.strip()]

        if len(lines) <= 1:
            return None

        return lines

    except:
        return None
