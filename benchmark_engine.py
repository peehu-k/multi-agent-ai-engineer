import time
import json
import os

TEST_TASKS = [
    "build password generator",
    "build csv cleaner",
    "build log analyzer",
    "build file organizer",
    "build api fetcher"
]

def run_benchmark(run_task):
    print("\n=== AI BENCHMARK MODE STARTED ===\n")

    results = []
    success_count = 0
    total_score = 0
    total_time = 0

    for task in TEST_TASKS:
        print(f"\n[TESTING]: {task}")
        start = time.time()

        score, success = run_task(task, benchmark=True)

        t = round(time.time() - start,2)

        total_score += score
        total_time += t
        if success:
            success_count += 1

        results.append({
            "task": task,
            "score": score,
            "success": success,
            "time": t
        })

    success_rate = round((success_count/len(TEST_TASKS))*100,1)
    avg_score = round(total_score/len(TEST_TASKS),2)
    avg_time = round(total_time/len(TEST_TASKS),2)

    summary = {
        "success_rate": success_rate,
        "avg_score": avg_score,
        "avg_time": avg_time,
        "results": results
    }

    os.makedirs("memory", exist_ok=True)
    with open("memory/performance.json","w") as f:
        json.dump(summary,f,indent=4)

    print("\n=== BENCHMARK COMPLETE ===")
    print("Success Rate:", success_rate,"%")
    print("Avg Score:", avg_score)
    print("Avg Time:", avg_time,"s")
    print("[Saved → memory/performance.json]\n")
