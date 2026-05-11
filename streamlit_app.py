import streamlit as st

home_page = st.Page(
    "app/main.py",
    title="Home Page"
)

patient_demographic_analysis = st.Page(
    "app/pages/1_Patient_Demographic_Analysis.py",
    title = "Patient Demographic"
)

medical_condition_analysis = st.Page(
    "app/pages/2_Medical_Condition_Analysis.py",
    title = "Medical Condition"
)

admission_discharge_analysis = st.Page(
    "app/pages/3_Admission_and_Discharge_Analysis.py",
    title = "Admission & Discharge"
)

hospital_performance_analysis = st.Page(
    "app/pages/4_Hospital_Performance_Analysis.py",
    title = "Hospital Performance"
)

doctor_analysis = st.Page(
    "app/pages/5_Doctor_Analysis.py",
    title = "Doctor Information"
)

insurance_billing_analysis = st.Page(
    "app/pages/6_Insurance_and_Billing_Analysis.py",
    title = "Insurance & Billing"
)

medication_test_analysis = st.Page(
    "app/pages/7_Medication_and_Test_Result_Analysis.py",
    title = "Medical & Test Results"
)


nav = st.navigation(
    [
        home_page,
        patient_demographic_analysis,
        medical_condition_analysis,
        admission_discharge_analysis,
        hospital_performance_analysis,
        doctor_analysis,
        insurance_billing_analysis,
        medication_test_analysis
    ]
)

nav.run()