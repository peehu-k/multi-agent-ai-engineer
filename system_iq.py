import json
import os

IQ_PATH = "memory/system_iq.json"

def load_iq():
    if not os.path.exists(IQ_PATH):
        return {
            "system_iq": 50,
            "reasoning": 50,
            "coding": 50,
            "debugging": 50,
            "architecture": 50,
            "learning": 50,
            "total_runs": 0
        }
    with open(IQ_PATH, "r") as f:
        return json.load(f)

def save_iq(data):
    with open(IQ_PATH, "w") as f:
        json.dump(data, f, indent=4)

def update_iq(success=True, score=7):
    data = load_iq()
    data["total_runs"] += 1

    boost = score/10

    if success:
        data["system_iq"] += 1 + boost
        data["coding"] += boost
        data["reasoning"] += 0.4
        data["learning"] += 0.3
    else:
        data["system_iq"] -= 0.3
        data["debugging"] += 0.2

    for k in data:
        if isinstance(data[k], (int,float)):
            if data[k] < 0: data[k] = 0
            if data[k] > 200: data[k] = 200

    save_iq(data)

def get_iq():
    return load_iq()
