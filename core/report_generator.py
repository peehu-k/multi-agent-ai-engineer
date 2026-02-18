import json
import os

def generate_report():
    if not os.path.exists("memory/performance.json"):
        print("No benchmark data found.")
        return

    with open("memory/performance.json","r") as f:
        data = json.load(f)

    report = f"""
AI SYSTEM PERFORMANCE REPORT
============================
Success Rate: {data['success_rate']}%
Average Score: {data['avg_score']}/10
Average Build Time: {data['avg_time']}s

Tested Tasks:
"""

    for r in data["results"]:
        report += f"- {r['task']} | score:{r['score']} | success:{r['success']} | time:{r['time']}s\n"

    with open("memory/final_report.txt","w") as f:
        f.write(report)

    print("\nReport saved → memory/final_report.txt\n")
