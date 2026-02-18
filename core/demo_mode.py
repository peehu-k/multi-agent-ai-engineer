import time

DEMO_TASKS = [
    "build password generator",
    "build csv cleaner",
    "build log analyzer"
]

def run_demo(run_task):
    print("\n=== LIVE AI DEMO MODE ===\n")

    for task in DEMO_TASKS:
        print(f"\n>>> AI building: {task}")
        run_task(task)
        time.sleep(1)

    print("\n=== DEMO COMPLETE ===\n")
