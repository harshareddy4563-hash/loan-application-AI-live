import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("Loan Application with Face & CIBIL")

app_aadhaar = st.text_input("Applicant Aadhaar")
guard_aadhaar = st.text_input("Guardian Aadhaar")
cibil = st.number_input("CIBIL Score", 300, 900)

app_face = st.camera_input("Applicant Face")
guard_face = st.camera_input("Guardian Face")

if st.button("Submit"):
    if app_face and guard_face:
        res = requests.post(
            f"{API_URL}/apply-loan",
            data={
                "applicant_aadhaar": app_aadhaar,
                "guardian_aadhaar": guard_aadhaar,
                "cibil_score": cibil
            },
            files={
                "applicant_face": app_face.getvalue(),
                "guardian_face": guard_face.getvalue()
            }
        )
        st.json(res.json())
