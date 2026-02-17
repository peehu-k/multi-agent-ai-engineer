import os

TOOLS_FOLDER = "tools"

def list_tools():
    if not os.path.exists(TOOLS_FOLDER):
        return []

    return os.listdir(TOOLS_FOLDER)

def ecosystem_summary():
    tools = list_tools()

    if not tools:
        return "No tools yet"

    summary = "AI Tool Ecosystem:\n"
    for t in tools:
        summary += f"- {t}\n"

    return summary
