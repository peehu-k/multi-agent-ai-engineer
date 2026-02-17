import json
import os

PATH = "memory/intelligence.json"

def load_intelligence():
    if not os.path.exists(PATH):
        return {
            "intelligence_score": 50,
            "tools_created": 0,
            "successful_builds": 0,
            "failed_builds": 0,
            "total_runs": 0
        }

    with open(PATH, "r") as f:
        return json.load(f)

def save_intelligence(data):
    with open(PATH, "w") as f:
        json.dump(data, f, indent=4)

def update_intelligence(success, score, tool_created=False):
    data = load_intelligence()

    data["total_runs"] += 1

    if success:
        data["successful_builds"] += 1
        data["intelligence_score"] += 1 + (score/10)
    else:
        data["failed_builds"] += 1
        data["intelligence_score"] -= 0.5

    if tool_created:
        data["tools_created"] += 1
        data["intelligence_score"] += 2

    # clamp
    if data["intelligence_score"] < 0:
        data["intelligence_score"] = 0

    if data["intelligence_score"] > 200:
        data["intelligence_score"] = 200

    save_intelligence(data)

def get_intelligence():
    return load_intelligence()
