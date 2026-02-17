import streamlit as st
from PyPDF2 import PdfReader
import re
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="404:Neural Drift", layout="wide")

# ================================
# PREMIUM UI THEME + SIDEBAR UPGRADE
# ================================
st.markdown("""
<style>
/* Layout */
.block-container {padding-top: 1.2rem; padding-bottom: 2rem; max-width: 1200px;}
section[data-testid="stSidebar"] {width: 360px !important;}
section[data-testid="stSidebar"] > div {padding-top: 1.2rem;}

/* Background */
.stApp {
  background: radial-gradient(1200px circle at 10% 10%, #1b2bff22 0%, transparent 40%),
              radial-gradient(900px circle at 90% 20%, #ff2bd922 0%, transparent 35%),
              linear-gradient(180deg, #0b1020 0%, #070a14 100%);
}

/* Hero */
.hero-card {
  background: linear-gradient(135deg, rgba(0,229,255,0.15), rgba(168,85,247,0.15));
  border: 1px solid rgba(255,255,255,0.12);
  border-radius: 22px;
  padding: 35px;
  text-align: center;
  box-shadow: 0 20px 50px rgba(0,0,0,0.35);
}
.hero-title {
  font-size: 52px;
  font-weight: 900;
  background: linear-gradient(90deg, #00E5FF, #A855F7, #FF4D8D);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
.hero-sub {font-size: 18px; opacity: 0.8; margin-top: 10px; letter-spacing: 1px;}

/* Buttons */
.stButton button {
  width: 100%;
  border-radius: 14px !important;
  border: 1px solid rgba(255,255,255,0.18) !important;
  background: linear-gradient(90deg, #00E5FF, #A855F7) !important;
  color: #070a14 !important;
  font-weight: 900 !important;
  padding: 0.7rem 1rem !important;
}
.stButton button:hover {filter: brightness(1.05); transform: translateY(-1px);}

/* Inputs */
.stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] {
  border-radius: 12px !important;
}

/* Sidebar Glass Panel */
.sidebar-panel {
  background: rgba(255,255,255,0.06);
  border: 1px solid rgba(255,255,255,0.12);
  border-radius: 18px;
  padding: 14px 14px;
  box-shadow: 0 14px 40px rgba(0,0,0,0.35);
  margin-bottom: 14px;
}
.sidebar-title {
  font-weight: 900;
  font-size: 16px;
  letter-spacing: 0.5px;
  margin-bottom: 8px;
}
.sidebar-sub {
  opacity: 0.75;
  font-size: 13px;
  margin-top: -4px;
  margin-bottom: 10px;
}
.pill {
  display:inline-block;
  padding: 6px 10px;
  border-radius: 999px;
  font-size: 12px;
  font-weight: 800;
  border: 1px solid rgba(255,255,255,0.16);
  background: rgba(255,255,255,0.08);
  margin-bottom: 10px;
}
.pill-green {border-color:#16a34a88; background:#16a34a22;}
.pill-red {border-color:#ef444488; background:#ef444422;}
hr {
  border: none;
  height: 1px;
  background: rgba(255,255,255,0.10);
  margin: 12px 0;
}
</style>
""", unsafe_allow_html=True)

# ================================
# HERO SECTION
# ================================
st.markdown("""
<div class="hero-card">
  <div class="hero-title">🚀 404:Neural Drift</div>
  <div class="hero-sub">Your AI-Powered Career Intelligence Engine</div>
</div>
""", unsafe_allow_html=True)

st.divider()

# ================================
# SIDEBAR NAVIGATION (ATTRACTIVE)
# ================================
st.sidebar.markdown("""
<div class="sidebar-panel">
  <div class="sidebar-title">🧭 Control Center</div>
  <div class="sidebar-sub">Navigate + launch your career scan</div>
</div>
""", unsafe_allow_html=True)

page = st.sidebar.radio("Navigate", ["🏠 Home", "🚀 Career Engine"], label_visibility="collapsed")

st.sidebar.markdown("<hr>", unsafe_allow_html=True)

# ================================
# HOME PAGE
# ================================
if page == "🏠 Home":
    st.markdown("""
    <div class="hero-card">
      <h2>Welcome to 404:Neural Drift 👋</h2>
      <p>Not just career advice. Not static roadmaps.</p>
      <p><b>This is your adaptive AI Career Intelligence System.</b></p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("### 🔍 Analyze")
        st.write("Upload your profile and detect skill strengths.")
    with c2:
        st.markdown("### 📊 Strategize")
        st.write("Get role readiness scoring + market alignment.")
    with c3:
        st.markdown("### 🎯 Execute")
        st.write("Receive roadmap + mock interview simulation.")

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.info("👉 Navigate to **Career Engine** to begin your analysis.")
    st.stop()

# ================================
# CAREER ENGINE PAGE (SIDEBAR PANEL)
# ================================
st.sidebar.markdown("""
<div class="sidebar-panel">
  <div class="sidebar-title">📂 Profile Upload</div>
  <div class="sidebar-sub">Resume + links (quick demo)</div>
</div>
""", unsafe_allow_html=True)

resume = st.sidebar.file_uploader("Resume PDF", type=["pdf"], label_visibility="visible")
github_link = st.sidebar.text_input("GitHub URL", placeholder="https://github.com/username")
linkedin_link = st.sidebar.text_input("LinkedIn URL", placeholder="https://linkedin.com/in/username")

st.sidebar.markdown("<hr>", unsafe_allow_html=True)

st.sidebar.markdown("""
<div class="sidebar-panel">
  <div class="sidebar-title">🎯 Target Role</div>
  <div class="sidebar-sub">Pick your dream role</div>
</div>
""", unsafe_allow_html=True)

dream_role = st.sidebar.selectbox(
    "Dream Role",
    ["AI Engineer", "Data Scientist", "Full Stack Developer"],
    label_visibility="collapsed"
)

launch = st.sidebar.button("🚀 Launch Career Analysis")

# Launch state
if "launched" not in st.session_state:
    st.session_state.launched = False

if launch and resume:
    st.session_state.launched = True

if not resume:
    st.session_state.launched = False

# Status pill in sidebar
if st.session_state.launched and resume:
    st.sidebar.markdown('<div class="pill pill-green">✅ Analysis Active</div>', unsafe_allow_html=True)
else:
    st.sidebar.markdown('<div class="pill pill-red">⏳ Waiting for Resume</div>', unsafe_allow_html=True)

# Reset for demo
if st.sidebar.button("🔄 Reset"):
    st.session_state.launched = False
    st.session_state.interview_active = False
    st.session_state.question = ""
    st.session_state.feedback = ""
    st.session_state.answer_box = ""

# ================================
# ROLE REQUIREMENTS
# ================================
role_requirements = {
    "AI Engineer": ["Python", "Machine Learning", "Deep Learning", "TensorFlow", "PyTorch", "Model Deployment", "Git"],
    "Data Scientist": ["Python", "SQL", "Statistics", "Machine Learning", "Data Visualization", "Pandas"],
    "Full Stack Developer": ["JavaScript", "React", "Node.js", "Databases", "Git", "HTML", "CSS"]
}

def extract_resume_text(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text

def extract_skills_local(text, required_skills):
    detected = []
    for skill in required_skills:
        if re.search(skill.lower(), text.lower()):
            detected.append(skill)
    return list(set(detected))

# ================================
# MAIN ANALYSIS
# ================================
if st.session_state.launched and resume:

    st.header("🔍 Analyzing Profile...")

    resume_text = extract_resume_text(resume)
    full_profile = resume_text + github_link + linkedin_link

    required_skills = role_requirements[dream_role]
    extracted_skills = extract_skills_local(full_profile, required_skills)
    missing_skills = list(set(required_skills) - set(extracted_skills))

    readiness = int((len(required_skills) - len(missing_skills)) / len(required_skills) * 100)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("✅ Strength Zone")
        for skill in extracted_skills:
            st.success(skill)

        st.subheader("❌ Growth Zone")
        for skill in missing_skills:
            st.error(skill)

    with col2:
        st.subheader("🎯 Role Readiness")
        st.progress(readiness / 100)
        st.write(f"{readiness}% Alignment with {dream_role}")

        fig, ax = plt.subplots()
        ax.pie([len(extracted_skills), len(missing_skills)],
               labels=["Have", "Missing"],
               autopct='%1.1f%%')
        st.pyplot(fig)

    st.divider()

    st.subheader("📅 30-Day Execution Blueprint")
    st.write("Week 1 → Fundamentals")
    st.write("Week 2 → Mini Projects")
    st.write("Week 3 → Integrated Portfolio Project")
    st.write("Week 4 → Market Positioning + Applications")

    # ================================
    # 🎤 MOCK INTERVIEW (BEHAVIORAL/TECH/HR)
    # ================================
    st.divider()
    st.subheader("🎤 Mock Interview Engine")

    # Session init
    if "interview_active" not in st.session_state:
        st.session_state.interview_active = False
    if "question" not in st.session_state:
        st.session_state.question = ""
    if "feedback" not in st.session_state:
        st.session_state.feedback = ""

    interview_type = st.selectbox(
        "Choose interview type:",
        ["Behavioral", "Technical", "HR"],
        key="interview_type"
    )

    def start_interview():
        st.session_state.interview_active = True
        st.session_state.feedback = ""

        if st.session_state.interview_type == "Behavioral":
            st.session_state.question = "Tell me about a time you handled a difficult challenge. What did you do and what was the result?"
        elif st.session_state.interview_type == "Technical":
            if dream_role == "AI Engineer":
                st.session_state.question = "Explain overfitting. How would you detect and prevent it in a real project?"
            elif dream_role == "Data Scientist":
                st.session_state.question = "How would you handle missing data and outliers in a dataset before building a model?"
            else:
                st.session_state.question = "Explain REST APIs and how you would design a backend for a simple web app."
        else:
            st.session_state.question = "Why should we hire you for this role?"

    st.button("Start Mock Interview", on_click=start_interview)

    if st.session_state.interview_active:
        st.markdown("#### 🧠 Question")
        st.info(st.session_state.question)

        st.text_area("Your Answer", height=160, key="answer_box")

        def evaluate_answer():
            ans = st.session_state.answer_box.strip()
            if not ans:
                st.session_state.feedback = "⚠️ Please type an answer first."
                return

            wc = len(ans.split())
            if wc < 30:
                st.session_state.feedback = "❌ Too short. Add details + what impact you created."
            elif wc < 60:
                st.session_state.feedback = "🟡 Good start. Add structure (STAR) and measurable results."
            else:
                st.session_state.feedback = "✅ Strong answer! Add a real project example + numbers for perfection."

        st.button("Evaluate Answer", on_click=evaluate_answer)

        if st.session_state.feedback:
            if "❌" in st.session_state.feedback:
                st.error(st.session_state.feedback)
            elif "⚠️" in st.session_state.feedback:
                st.warning(st.session_state.feedback)
            elif "✅" in st.session_state.feedback:
                st.success(st.session_state.feedback)
            else:
                st.info(st.session_state.feedback)

        st.caption("Tip: Use STAR method — Situation, Task, Action, Result.")

else:
    st.info("Upload resume and click Launch to activate 404:Neural Drift.")
