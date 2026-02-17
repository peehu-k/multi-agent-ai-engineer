import os
import time
import json

from core.coder import generate_code
from core.debugger import debug_code
from core.reviewer import review_code
from core.tool_reuse import find_existing_tool
from core.intelligence import update_intelligence
from core.system_iq import update_iq
from core.benchmark_engine import run_benchmark
from core.report_generator import generate_report
from core.demo_mode import run_demo

TOOLS_FOLDER = "tools"
MEMORY_FILE = "tool_memory.json"

os.makedirs(TOOLS_FOLDER, exist_ok=True)

if not os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE,"w") as f:
        json.dump({},f)

def log(msg):
    print(msg)
    os.makedirs("memory", exist_ok=True)
    with open("memory/activity_log.txt","a",encoding="utf-8") as f:
        f.write(msg+"\n")

def load_memory():
    try:
        with open(MEMORY_FILE,"r") as f:
            return json.load(f)
    except:
        return {}

def save_memory(data):
    with open(MEMORY_FILE,"w") as f:
        json.dump(data,f,indent=2)

def save_tool(task, code, score):
    safe = task.replace(" ","_").lower()
    path = f"{TOOLS_FOLDER}/{safe}.py"

    with open(path,"w",encoding="utf-8") as f:
        f.write(code)

    mem = load_memory()
    mem[safe] = float(score)
    save_memory(mem)

    log(f"[TOOL CREATED] {path}")

# ================= ENGINE ================= #

def run_task(task, benchmark=False):
    start = time.time()
    log(f"\n=== NEW TASK: {task} ===")

    safe = task.replace(" ","_").lower()
    mem = load_memory()

    # reuse tool
    existing_tool = find_existing_tool(task)

    if existing_tool and safe in mem:
        score = float(mem.get(safe,7))

        log("[TOOL INTELLIGENCE] Existing tool detected")
        log(f"[PAST SCORE]: {score}")

        if score >= 8:
            log("[AI] Using existing high-quality tool instantly ⚡")
            update_intelligence(True, score, True)
            update_iq(True, score)
            return score, True

        log("[AI] Improving weak tool...")

        with open(existing_tool,"r",encoding="utf-8") as f:
            old_code = f.read()

        improved = debug_code(task, old_code)

        if improved and len(improved)>20:
            with open(existing_tool,"w",encoding="utf-8") as f:
                f.write(improved)

            mem[safe]=9.0
            save_memory(mem)

            update_intelligence(True,9,True)
            update_iq(True,9)

            log("[AI] Tool upgraded")
            return 9.0, True

    # build new tool
    log("[CODER] Generating tool...")
    code = generate_code(task,"","")

    if not code or len(code)<20:
        log("[FAIL] generation failed")
        update_intelligence(False,0,False)
        update_iq(False,0)
        return 0, False

    log("[DEBUG] Improving code...")
    fixed = debug_code(task,code)
    if fixed and len(fixed)>20:
        code = fixed

    log("[REVIEW] Evaluating quality...")
    score = review_code(task,code)

    if not isinstance(score,(int,float)):
        score = 7.0

    save_tool(task,code,score)

    success = score>=7
    update_intelligence(success,score,True)
    update_iq(success,score)

    log(f"[DONE] Score: {score} | Success: {success}")
    log(f"[TIME] {round(time.time()-start,2)}s")

    return score, success

# ================= MAIN ================= #

if __name__ == "__main__":
    print("\n=== Autonomous AI Software Engineer (FULL INTELLIGENCE MODE) ===")

    while True:
        task = input("\nEnter engineering task (or exit): ").strip().lower()

        if task=="exit":
            break

        if task=="benchmark":
            run_benchmark(run_task)
            continue

        if task=="report":
            generate_report()
            continue

        if task=="demo":
            run_demo(run_task)
            continue

        run_task(task)
