import json
import os

MEMORY_PATH = "memory/learning.json"

def load_memory():
    if not os.path.exists(MEMORY_PATH):
        return {
            "total_runs": 0,
            "successes": 0,
            "failures": 0,
            "common_failures": [],
            "successful_patterns": []
        }

    with open(MEMORY_PATH, "r") as f:
        return json.load(f)

def save_memory(data):
    with open(MEMORY_PATH, "w") as f:
        json.dump(data, f, indent=4)

def update_learning(task, success, code):
    data = load_memory()

    data["total_runs"] += 1

    if success:
        data["successes"] += 1

        # store good pattern
        if len(data["successful_patterns"]) < 50:
            data["successful_patterns"].append(task)

    else:
        data["failures"] += 1

        if len(data["common_failures"]) < 50:
            data["common_failures"].append(task)

    save_memory(data)

def get_learning_context():
    data = load_memory()

    context = f"""
SYSTEM LEARNING DATA:
Total Runs: {data['total_runs']}
Successes: {data['successes']}
Failures: {data['failures']}

Successful task patterns:
{data['successful_patterns'][-5:]}

Common failures to avoid:
{data['common_failures'][-5:]}
"""
    return context
