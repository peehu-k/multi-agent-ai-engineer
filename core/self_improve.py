import os
from core.debugger import debug_code
from core.reviewer import review_code

TOOLS_FOLDER = "tools"

def improve_all_tools():
    """
    Scans all tools and upgrades weak ones.
    """

    if not os.path.exists(TOOLS_FOLDER):
        print("No tools folder")
        return

    files = os.listdir(TOOLS_FOLDER)

    if not files:
        print("No tools to improve")
        return

    print("[SELF-IMPROVE] Scanning tools...\n")

    for file in files:
        path = os.path.join(TOOLS_FOLDER, file)

        try:
            with open(path, "r", encoding="utf-8") as f:
                code = f.read()
        except:
            continue

        score = review_code(file, code)
        print(f"{file} → score {score}")

        if score < 8:
            print("   Improving tool...")
            improved = debug_code(file, code)

            if improved:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(improved)
                print("   Improved.\n")
