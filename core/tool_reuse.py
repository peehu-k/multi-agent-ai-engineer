import os
import difflib

TOOLS_FOLDER = "tools"

def find_existing_tool(task):
    """
    Finds if a similar tool already exists based on task similarity
    """

    if not os.path.exists(TOOLS_FOLDER):
        return None

    files = os.listdir(TOOLS_FOLDER)
    if not files:
        return None

    task = task.lower()

    best_match = None
    best_score = 0

    for file in files:
        name = file.lower().replace(".py","")

        score = difflib.SequenceMatcher(None, task, name).ratio()

        if score > best_score:
            best_score = score
            best_match = file

    # similarity threshold
    if best_score > 0.55:
        return os.path.join(TOOLS_FOLDER, best_match)

    return None
