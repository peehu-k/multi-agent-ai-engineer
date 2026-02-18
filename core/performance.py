import json
import os
import time

PERF_FILE = "memory/performance.json"

def log_performance(task, score, runtime):
    os.makedirs("memory", exist_ok=True)

    if os.path.exists(PERF_FILE):
        with open(PERF_FILE, "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append({
        "task": task,
        "quality_score": score,
        "time_taken": runtime,
        "timestamp": time.time()
    })

    with open(PERF_FILE, "w") as f:
        json.dump(data, f, indent=2)
