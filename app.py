import streamlit as st

st.title("📊 Customer Churn Prediction")

tenure = st.slider("Customer Tenure (Months)", 0, 72, 12)

monthly_charges = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    value=1000.0
)

support_calls = st.number_input(
    "Support Calls",
    min_value=0,
    value=2
)

if st.button("Predict Churn"):

    score = (
        support_calls * 20
        + (monthly_charges / 100)
        - (tenure / 2)
    )

    if score > 30:
        st.error("⚠ High Churn Risk")
        st.write("Retention Action Recommended")
    else:
        st.success("✅ Low Churn Risk")
