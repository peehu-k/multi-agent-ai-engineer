import subprocess

MODEL = "phi3"

def plan_task(task):
    """
    Creates engineering plan before coding.
    """

    prompt = f"""
You are a senior software architect.

Create short step-by-step engineering plan.

TASK:
{task}

Rules:
- Max 6 steps
- No code
- Clear engineering thinking
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

        plan = result.stdout.strip()

        if len(plan) < 10:
            return ""

        return plan

    except:
        return ""
