import streamlit as st
import joblib
import pandas as pd

# Page setup
st.set_page_config(
    page_title="Diabetes Risk Assessment",
    page_icon="🩺",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.main {
    background: linear-gradient(to bottom right, #0f172a, #1e293b);
    color: white;
}
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}
.card {
    background: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 20px;
    margin-bottom: 20px;
}
.big-title {
    font-size: 42px;
    font-weight: bold;
}
.small-text {
    color: #cbd5e1;
}
.stButton>button {
    width: 100%;
    height: 55px;
    border-radius: 15px;
    font-size: 18px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)


# Load model + scaler
@st.cache_resource
def load_artifacts():
    model = joblib.load("model/diabetes_model.joblib")
    scaler = joblib.load("model/diabetes_scaler.joblib")
    return model, scaler


try:
    model, scaler = load_artifacts()
except Exception as e:
    st.error(f"Error loading files: {e}")
    st.stop()


# Header
st.markdown('<div class="big-title">🩺 Diabetes Risk Assessment Tool</div>', unsafe_allow_html=True)
st.markdown('<div class="small-text">Smart lifestyle-based diabetes screening for home users</div>', unsafe_allow_html=True)

st.markdown("---")


# Sidebar
with st.sidebar:
    st.header("👤 Personal Info")

    age = st.slider("Age", 10, 100, 30)

    gender = st.selectbox("Gender", ["Female", "Male"])

    weight = st.slider("Weight (kg)", 20, 200, 70)

    height_cm = st.slider("Height (cm)", 100, 220, 165)

    bmi = round(weight / ((height_cm / 100) ** 2), 2)

    st.metric("Calculated BMI", bmi)


# Main layout
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("❤️ Blood Pressure")
    systolic = st.slider("Systolic BP", 80, 250, 120)
    diastolic = st.slider("Diastolic BP", 40, 150, 80)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🧬 Family History")
    family_history = st.selectbox("Family History of Diabetes?", ["No", "Yes"])
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🏃 Lifestyle")
    exercise = st.slider("Daily Exercise (minutes)", 0, 180, 20)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("💧 Symptoms")
    thirst = st.selectbox("Excessive Thirst?", ["No", "Yes"])
    urination = st.selectbox("Frequent Urination?", ["No", "Yes"])
    st.markdown('</div>', unsafe_allow_html=True)


st.markdown("---")


# Prediction
if st.button("🔍 Check My Diabetes Risk"):

    # Encode categoricals
    gender_enc = 1 if gender == "Male" else 0
    family_history_enc = 1 if family_history == "Yes" else 0
    thirst_enc = 1 if thirst == "Yes" else 0
    urination_enc = 1 if urination == "Yes" else 0

    # Scale continuous columns — names must match training exactly
    cont_cols = ['Age', 'Weight_kg', 'BMI', 'Systolic_BP',
                 'Diastolic_BP', 'Exercise_Duration']

    cont_values = pd.DataFrame([[
        age, weight, bmi, systolic, diastolic, exercise
    ]], columns=cont_cols)

    cont_scaled = scaler.transform(cont_values)

    # Build input — column names and order must match X_train exactly
    input_data = pd.DataFrame([{
        'Age':                          cont_scaled[0][0],
        'Gender':                       gender_enc,
        'Weight_kg':                    cont_scaled[0][1],
        'BMI':                          cont_scaled[0][2],
        'Systolic_BP':                  cont_scaled[0][3],
        'Diastolic_BP':                 cont_scaled[0][4],
        'Family_History':               family_history_enc,
        'Exercise_Duration':            cont_scaled[0][5],
        'Polydipsia_Excessive_Thirst':  thirst_enc,
        'Polyuria_Frequent_Urination':  urination_enc
    }])

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    st.markdown("## 📊 Assessment Result")
    st.progress(float(probability))

    if prediction == 1:
        st.error(f"⚠ High Risk Detected ({probability*100:.1f}%)")
        st.info("Your inputs suggest an elevated diabetes risk. "
                "Consider consulting a healthcare professional for further testing.")
    else:
        st.success(f"✅ Low Risk ({probability*100:.1f}%)")
        st.info("Your health indicators look stable. "
                "Maintain a healthy lifestyle and monitor regularly.")

st.markdown("---")
st.caption("⚠ This tool is for educational screening only and not a medical diagnosis.")