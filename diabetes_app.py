# paste your Python code below this line, no shell commands
print("Hello from diabetes_app.py")
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier

# Set page configuration
st.set_page_config(
    page_title="Diabetes Prediction App",
    page_icon="🏥",
    layout="wide"
)

# Title and introduction
st.title("Diabetes Prediction App 🏥")
st.write("This app predicts the likelihood of diabetes based on health metrics.")

# Create a form for user input
with st.form("prediction_form"):
    st.header("Enter Patient Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=0)
        glucose = st.number_input("Glucose Level", min_value=0, max_value=200, value=100)
        blood_pressure = st.number_input("Blood Pressure", min_value=0, max_value=150, value=70)
        skin_thickness = st.number_input("Skin Thickness", min_value=0, max_value=100, value=20)
    
    with col2:
        insulin = st.number_input("Insulin Level", min_value=0, max_value=900, value=80)
        bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=25.0, step=0.1)
        diabetes_pedigree = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.5, step=0.01)
        age = st.number_input("Age", min_value=0, max_value=120, value=25)
    
    # Submit button
    submitted = st.form_submit_button("Predict Diabetes Risk")

# If the form is submitted, make a prediction
if submitted:
    # Create a feature array from the input
    features = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, 
                         insulin, bmi, diabetes_pedigree, age]])
    
    # For demonstration purposes, we'll create a simple model
    # In a real app, you would load your trained model here
    st.info("Note: This is a demonstration app. In a real application, you would load a pre-trained model.")
    
    # Simple rule-based prediction for demonstration
    # (This is not a medically accurate model)
    risk_factors = 0
    
    if glucose > 140:
        risk_factors += 1
    if bmi > 30:
        risk_factors += 1
    if age > 45:
        risk_factors += 1
    if diabetes_pedigree > 1.0:
        risk_factors += 1
    if blood_pressure > 80:
        risk_factors += 0.5
    
    # Calculate risk percentage (for demonstration only)
    risk_percentage = min(100, risk_factors * 20 + 10)
    
    # Display results
    st.subheader("Prediction Results")
    
    if risk_percentage < 30:
        st.success(f"Low risk of diabetes: {risk_percentage:.1f}%")
        st.write("Based on the inputs, this patient shows a low likelihood of diabetes.")
    elif risk_percentage < 60:
        st.warning(f"Moderate risk of diabetes: {risk_percentage:.1f}%")
        st.write("This patient shows some risk factors for diabetes. Further monitoring recommended.")
    else:
        st.error(f"High risk of diabetes: {risk_percentage:.1f}%")
        st.write("This patient shows significant risk factors for diabetes. Medical consultation recommended.")
    
    # Show a detailed breakdown
    with st.expander("View Risk Factor Analysis"):
        st.write("**Risk factors identified:**")
        if glucose > 140:
            st.write(f"- Elevated glucose level ({glucose})")
        if bmi > 30:
            st.write(f"- Elevated BMI ({bmi})")
        if age > 45:
            st.write(f"- Age above 45 ({age})")
        if diabetes_pedigree > 1.0:
            st.write(f"- Elevated diabetes pedigree function ({diabetes_pedigree})")
        if blood_pressure > 80:
            st.write(f"- Elevated blood pressure ({blood_pressure})")
        
        if risk_factors == 0:
            st.write("No significant risk factors identified.")

# Add information about the app
with st.sidebar:
    st.header("About This App")
    st.write("""
    This diabetes prediction app uses machine learning to estimate 
    the likelihood of diabetes based on health metrics.
    
    **Disclaimer:** This is a demonstration app only and should not 
    be used for actual medical diagnosis. Always consult with 
    healthcare professionals for medical advice.
    """)
    
    st.header("Input Guidelines")
    st.write("""
    - **Glucose:** Normal fasting glucose is typically < 100 mg/dL
    - **BMI:** Healthy BMI range is 18.5-24.9
    - **Blood Pressure:** Normal is typically < 120/80 mmHg
    - **Age:** Risk increases with age, especially after 45
    """)

# Footer
st.markdown("---")
st.caption("Diabetes Prediction App | For demonstration purposes only")

# Add some styling
st.markdown("""
<style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
    }
    .stSuccess {
        background-color: #D4EDDA;
        padding: 15px;
        border-radius: 5px;
        border-left: 4px solid #28A745;
    }
    .stWarning {
        background-color: #FFF3CD;
        padding: 15px;
        border-radius: 5px;
        border-left: 4px solid #FFC107;
    }
    .stError {
        background-color: #F8D7DA;
        padding: 15px;
        border-radius: 5px;
        border-left: 4px solid #DC3545;
    }
</style>
""", unsafe_allow_html=True)


