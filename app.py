import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Customer Retention Intelligence Platform",
    layout="wide"
)

st.title("📉 Customer Retention Intelligence Platform")

st.markdown(
    "Predict churn risk, customer health, lifetime value and revenue impact."
)

st.sidebar.header("Customer Profile")

tenure = st.sidebar.slider(
    "Customer Tenure (Months)",
    1,
    72,
    24
)

monthly_charges = st.sidebar.slider(
    "Monthly Charges (₹)",
    100,
    10000,
    2000
)

support_tickets = st.sidebar.slider(
    "Support Tickets",
    0,
    20,
    3
)

satisfaction = st.sidebar.slider(
    "Customer Satisfaction",
    1,
    10,
    7
)

contract = st.sidebar.selectbox(
    "Contract Type",
    [
        "Month-to-Month",
        "One Year",
        "Two Year"
    ]
)

if st.sidebar.button("Analyze Customer"):

    churn_score = 0

    if tenure < 12:
        churn_score += 25

    if support_tickets > 5:
        churn_score += 25

    if satisfaction < 5:
        churn_score += 30

    if contract == "Month-to-Month":
        churn_score += 20

    churn_probability = min(churn_score, 100)

    health_score = 100 - churn_probability

    clv = tenure * monthly_charges

    revenue_loss = (
        monthly_charges * 12
        * (churn_probability / 100)
    )

    if churn_probability >= 75:
        risk = "Critical Risk 🔴"
    elif churn_probability >= 50:
        risk = "High Risk 🟠"
    elif churn_probability >= 25:
        risk = "Medium Risk 🟡"
    else:
        risk = "Low Risk 🟢"

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Churn Probability",
        f"{churn_probability}%"
    )

    col2.metric(
        "Health Score",
        f"{health_score}/100"
    )

    col3.metric(
        "Customer Lifetime Value",
        f"₹{clv:,.0f}"
    )

    col4.metric(
        "Revenue Impact",
        f"₹{revenue_loss:,.0f}"
    )

    st.divider()

    st.subheader("⚠️ Churn Risk Analysis")

    st.progress(churn_probability / 100)

    st.warning(risk)

    st.divider()

    st.subheader("📊 Customer Intelligence Dashboard")

    chart_df = pd.DataFrame({
        "Metric": [
            "Health Score",
            "Churn Risk",
            "Satisfaction"
        ],
        "Value": [
            health_score,
            churn_probability,
            satisfaction * 10
        ]
    })

    fig = px.bar(
        chart_df,
        x="Metric",
        y="Value",
        title="Customer Health Overview"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    st.subheader("🎯 Retention Recommendations")

    recommendations = []

    if satisfaction < 5:
        recommendations.append(
            "Offer Customer Satisfaction Program"
        )

    if support_tickets > 5:
        recommendations.append(
            "Assign Dedicated Support Manager"
        )

    if contract == "Month-to-Month":
        recommendations.append(
            "Offer Long-Term Contract Discount"
        )

    if churn_probability > 60:
        recommendations.append(
            "Provide Loyalty Rewards"
        )

    if not recommendations:
        recommendations.append(
            "Customer Retention Status Healthy"
        )

    for rec in recommendations:
        st.success(rec)

    st.divider()

    st.subheader("📈 Business Impact")

    if churn_probability > 70:
        st.error(
            "High revenue loss risk detected."
        )

    elif churn_probability > 40:
        st.warning(
            "Moderate retention efforts required."
        )

    else:
        st.success(
            "Customer relationship is healthy."
        )

    st.divider()

    st.subheader("📥 Download Customer Report")

    report = pd.DataFrame({
        "Metric": [
            "Churn Probability",
            "Health Score",
            "Customer Lifetime Value",
            "Revenue Impact",
            "Risk Level"
        ],
        "Value": [
            churn_probability,
            health_score,
            clv,
            revenue_loss,
            risk
        ]
    })

    csv = report.to_csv(index=False)

    st.download_button(
        "Download Report",
        csv,
        "customer_retention_report.csv",
        "text/csv"
    )

else:

    st.info(
        "Fill customer details and click Analyze Customer"
    )
