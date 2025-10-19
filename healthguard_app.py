import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="HealthGuard AI", page_icon="🩺", layout="wide")

# --- Custom CSS for dark theme ---
st.markdown("""
    <style>
    /* Background gradient */
    .stApp {
        background: linear-gradient(135deg, #0f0f0f, #1a1a1a);
        font-family: 'Arial', sans-serif;
        color: #e0e0e0;
    }
    /* Title styling */
    .title {
        font-size: 48px;
        font-weight: bold;
        color: #00e676;
        text-align: center;
    }
    .subtitle {
        font-size: 24px;
        color: #80d8ff;
        text-align: center;
    }
    /* Card style for input sections and results */
    .card {
        background-color: #1e1e1ecc;
        padding: 25px;
        border-radius: 20px;
        box-shadow: 3px 3px 15px rgba(0,0,0,0.5);
        margin-bottom: 20px;
    }
    /* Button style */
    .stButton>button {
        background-color: #00bfa5;
        color: black;
        font-size: 20px;
        padding: 12px 30px;
        border-radius: 12px;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #00e676;
        transform: scale(1.05);
    }
    /* Progress bar customization */
    .stProgress>div>div>div>div {
        background-color: #00bfa5 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- App Header ---
st.markdown('<div class="title">🩺 HealthGuard AI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-powered preventive healthcare — even works offline!</div>', unsafe_allow_html=True)
st.markdown("<br>")

st.markdown("### Enter Your Health Information")

# --- Input Section ---
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    age = st.number_input("Age", min_value=1, max_value=120, value=25)
    heart_rate = st.number_input("Heart Rate (bpm)", min_value=30, max_value=200, value=75)
    sleep_hours = st.slider("Average Sleep (hours)", 0.0, 12.0, 7.0)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    systolic_bp = st.number_input("Systolic BP (mmHg)", min_value=80, max_value=200, value=120)
    diastolic_bp = st.number_input("Diastolic BP (mmHg)", min_value=40, max_value=120, value=80)
    glucose = st.number_input("Glucose Level (mg/dL)", min_value=50, max_value=300, value=100)
    st.markdown('</div>', unsafe_allow_html=True)

# --- Analyze Button ---
if st.button("🔍 Analyze My Health"):
    
    # --- Risk Calculation ---
    risk_score = 0
    if systolic_bp > 140 or diastolic_bp > 90:
        risk_score += 1
    if glucose > 140:
        risk_score += 1
    if heart_rate > 100 or heart_rate < 50:
        risk_score += 1
    if sleep_hours < 5:
        risk_score += 1

    # Determine Risk Level and Color
    if risk_score == 0:
        risk_level = "Low Risk"
        advice = "You seem healthy! Keep maintaining your balanced lifestyle."
        color = "green"
        emoji = "🟢"
    elif risk_score == 1:
        risk_level = "Moderate Risk"
        advice = "Try to improve sleep and keep an eye on your vitals. Stay hydrated!"
        color = "orange"
        emoji = "🟡"
    else:
        risk_level = "High Risk"
        advice = "Consult a doctor soon. Focus on diet, exercise, and regular checkups."
        color = "red"
        emoji = "🔴"

    # --- Dashboard Display ---
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown(f"## 🧠 HealthGuard AI Analysis Result")
    
    # Risk Indicator
    st.markdown(f"<h2 style='color:{color}'>{emoji} {risk_level}</h2>", unsafe_allow_html=True)
    st.info(f"**Health Advice:** {advice}")

    # Progress Bars for each vital
    st.markdown("### 📊 Vitals Overview")
    st.progress(min(heart_rate/200, 1.0))  # heart rate
    st.caption(f"❤️ Heart Rate: {heart_rate} bpm")

    st.progress(min(systolic_bp/200, 1.0))
    st.caption(f"🩸 Systolic BP: {systolic_bp} mmHg")

    st.progress(min(diastolic_bp/120, 1.0))
    st.caption(f"🩸 Diastolic BP: {diastolic_bp} mmHg")

    st.progress(min(glucose/300, 1.0))
    st.caption(f"🍬 Glucose Level: {glucose} mg/dL")

    st.progress(min(sleep_hours/12, 1.0))
    st.caption(f"💤 Sleep Hours: {sleep_hours} hrs")

    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("💚 *HealthGuard AI empowers preventive healthcare even offline.*")

else:
    st.markdown("Click **Analyze My Health** to get your AI-powered health insights.")
