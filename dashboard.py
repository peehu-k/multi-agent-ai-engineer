import streamlit as st
import json
import os
import subprocess
import time
import pandas as pd

st.set_page_config(layout="wide", page_title="Multi-Agent AI Engineer")

PERF_FILE = "memory/performance.json"
LOG_FILE = "memory/activity_log.txt"
INTEL_FILE = "memory/intelligence.json"

# ---------- LOAD DATA ----------
def load_json(path):
    if os.path.exists(path):
        try:
            with open(path,"r") as f:
                return json.load(f)
        except:
            return {}
    return {}

intel = load_json(INTEL_FILE)
perf = load_json(PERF_FILE)

def safe(x):
    try: return float(x)
    except: return 0

int_score = safe(intel.get("intelligence_score",50))
tools = intel.get("tools_created",0)
runs = intel.get("total_runs",0)
success = intel.get("successful_builds",0)
rate = round((success/runs)*100,1) if runs else 0

# ---------- STYLE ----------
st.markdown("""
<style>

body {background:#F7F8FA;}
.main {background:#F7F8FA;}

.title{
font-size:42px;
font-weight:800;
color:#0F172A;
}

.subtitle{
color:#64748B;
font-size:16px;
margin-bottom:20px;
}

.card{
background:white;
padding:22px;
border-radius:14px;
border:1px solid #E2E8F0;
box-shadow:0 2px 6px rgba(0,0,0,0.04);
}

.metric{
font-size:34px;
font-weight:700;
color:#0F172A;
}

.label{
color:#64748B;
font-size:13px;
}

.section{
background:white;
padding:20px;
border-radius:14px;
border:1px solid #E2E8F0;
}

.event{
background:#F1F5F9;
padding:10px;
border-left:4px solid #2563EB;
margin-bottom:6px;
border-radius:6px;
font-size:14px;
color:#0F172A;
}

.highlight{
background:#EEF2FF;
padding:12px;
border-left:5px solid #2563EB;
margin-bottom:10px;
border-radius:6px;
font-weight:600;
color:#0F172A;
}

.stTextInput input{
background:white;
border:2px solid #2563EB;
border-radius:12px;
padding:18px;
font-size:18px;
color:#0F172A;
}

.stButton>button{
background:#2563EB;
color:white;
border-radius:10px;
height:50px;
font-weight:600;
border:none;
}

</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown('<div class="title">Multi-Agent Autonomous AI Software Engineer</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Self-Building • Self-Debugging • Self-Improving • Benchmarking AI System</div>', unsafe_allow_html=True)

# ---------- METRICS ----------
c1,c2,c3,c4 = st.columns(4)

with c1:
    st.markdown(f'<div class="card"><div class="metric">{int_score}</div><div class="label">AI Intelligence Score</div></div>', unsafe_allow_html=True)

with c2:
    st.markdown(f'<div class="card"><div class="metric">{rate}%</div><div class="label">Success Rate</div></div>', unsafe_allow_html=True)

with c3:
    st.markdown(f'<div class="card"><div class="metric">{tools}</div><div class="label">Tools Created</div></div>', unsafe_allow_html=True)

with c4:
    st.markdown(f'<div class="card"><div class="metric">{runs}</div><div class="label">Total Runs</div></div>', unsafe_allow_html=True)

st.divider()

# ---------- COMMAND CENTER ----------
st.markdown("## Command Center")

task = st.text_input("Enter engineering task")

b1,b2,b3 = st.columns(3)

if b1.button("Execute Task"):
    if task.strip():
        open(LOG_FILE,"w").close()
        subprocess.Popen(f'echo {task} | python agent.py', shell=True)
        st.success("AI executing task...")

if b2.button("Run Benchmark"):
    open(LOG_FILE,"w").close()
    subprocess.Popen('echo benchmark | python agent.py', shell=True)
    st.success("Benchmark running...")

if b3.button("Evolve System"):
    open(LOG_FILE,"w").close()
    subprocess.Popen('echo evolve fast | python agent.py', shell=True)
    st.success("System evolving...")

st.divider()

# ---------- LAYOUT ----------
left, right = st.columns([1.6,1])

# ---------- LIVE AI FEED ----------
with left:
    st.markdown("### Live AI Activity")

    if os.path.exists(LOG_FILE):
        with open(LOG_FILE,"r",encoding="utf-8") as f:
            logs = f.readlines()[-40:]
    else:
        logs = []

    for line in reversed(logs):
        if "[DONE]" in line or "[TOOL CREATED]" in line:
            st.markdown(f'<div class="highlight">{line}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="event">{line}</div>', unsafe_allow_html=True)

# ---------- RIGHT PANEL ----------
with right:
    st.markdown("### Tool Ecosystem")

    if os.path.exists("tools"):
        files = os.listdir("tools")
        if files:
            for f in files[:12]:
                st.write("•", f)

    st.markdown("### Intelligence Growth")
    st.progress(min(int(int_score),100))

# ---------- PERFORMANCE ----------
st.divider()
st.markdown("## Performance Analytics")

if isinstance(perf,list) and perf:
    df = pd.DataFrame(perf)

    g1,g2,g3 = st.columns(3)

    with g1:
        if "quality_score" in df.columns:
            st.markdown("Quality Score Trend")
            st.line_chart(df["quality_score"])

    with g2:
        if "time_taken" in df.columns:
            st.markdown("Build Time Trend")
            st.line_chart(df["time_taken"])

    with g3:
        if "success" in df.columns:
            st.markdown("Success Rate")
            st.bar_chart(df["success"].astype(int))
else:
    st.info("Run benchmark to generate performance graphs")

# ---------- AUTO REFRESH ----------
time.sleep(2)
st.rerun()
