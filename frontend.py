import streamlit as st
import requests
import streamlit as st
import requests

# ---------------- BLUE THEME CSS ----------------
st.markdown("""
<style>
/* Page background */
.stApp {
    background-color: #f5f9ff;
}

/* Title */
h1, h2, h3 {
    color: #0b5ed7;
}

/* Buttons */
.stButton > button {
    background-color: #0b5ed7;
    color: white;
    border-radius: 8px;
    padding: 0.5rem 1.2rem;
    font-weight: 600;
    border: none;
}

.stButton > button:hover {
    background-color: #084298;
    color: white;
}

/* Input fields */
input, textarea {
    border-radius: 6px !important;
    border: 1px solid #cfe2ff !important;
}

/* Success box */
div[data-testid="stSuccess"] {
    background-color: #e7f1ff;
    border-left: 6px solid #0b5ed7;
}

/* Warning box */
div[data-testid="stWarning"] {
    background-color: #fff3cd;
    border-left: 6px solid #ffc107;
}

/* Error box */
div[data-testid="stError"] {
    background-color: #f8d7da;
    border-left: 6px solid #dc3545;
}

/* Metric styling */
div[data-testid="metric-container"] {
    background-color: white;
    border: 1px solid #cfe2ff;
    padding: 12px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)
# ------------------------------------------------

st.set_page_config(page_title="Fraud Detection UI", layout="centered")

st.title("💳 Real-Time Fraud Detection")
st.write("Enter transaction details to evaluate fraud risk.")

API_URL = "http://backend:8000/score"  # Docker network
# If running without Docker frontend, use:
# API_URL = "http://localhost:8000/score"

amount = st.number_input("Transaction Amount ($)", min_value=0.0, step=10.0)
user_id = st.text_input("User ID")
merchant_id = st.text_input("Merchant ID")

if st.button("Check Fraud Risk"):
    if not user_id or not merchant_id:
        st.error("Please enter User ID and Merchant ID")
    else:
        payload = {
            "amount": amount,
            "user_id": user_id,
            "merchant_id": merchant_id
        }

        try:
            response = requests.post(API_URL, json=payload)
            result = response.json()

            st.subheader("Result")
            st.metric("Risk Score", result["risk_score"])
            st.success(f"Decision: {result['decision']}")

        except Exception as e:
            st.error(f"Error connecting to API: {e}")
