import os
import re

TOOLS_FOLDER = "tools"

def save_as_tool(task, code):
    if not os.path.exists(TOOLS_FOLDER):
        os.makedirs(TOOLS_FOLDER)

    name = re.sub(r'[^a-zA-Z0-9]+', '_', task.lower())[:40]
    path = f"{TOOLS_FOLDER}/{name}.py"

    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(code)
        return path
    except:
        return None
