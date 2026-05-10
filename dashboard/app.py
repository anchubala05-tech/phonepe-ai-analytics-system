import streamlit as st
import pandas as pd
import plotly.express as px

# ------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------

st.set_page_config(
    page_title="PhonePe AI Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# ------------------------------------------------
# LOAD CSV DATA
# ------------------------------------------------

master_df = pd.read_csv(
    "data/processed/master_dataset.csv"
)

anomaly_df = pd.read_csv(
    "data/processed/anomaly_detection_results.csv"
)

cluster_df = pd.read_csv(
    "data/processed/state_clusters.csv"
)

forecast_df = pd.read_csv(
    "data/processed/transaction_forecast.csv"
)

# ------------------------------------------------
# TITLE
# ------------------------------------------------

st.title("📊 AI-Powered PhonePe Analytics Dashboard")

st.markdown(
    """
    Advanced ML-powered transaction intelligence system
    with forecasting, clustering, and fraud analytics.
    """
)

# ------------------------------------------------
# SIDEBAR
# ------------------------------------------------

st.sidebar.header("Filter Options")

states = st.sidebar.multiselect(
    "Select States",
    options=sorted(master_df["State"].unique()),
    default=sorted(master_df["State"].unique())[:5]
)

filtered_df = master_df[
    master_df["State"].isin(states)
]

# ------------------------------------------------
# KPI CARDS
# ------------------------------------------------

total_transactions = (
    filtered_df["Transaction_Count"].sum()
)

total_amount = (
    filtered_df["Transaction_Amount"].sum()
)

avg_transaction = (
    filtered_df["Avg_Transaction_Value"].mean()
)

total_users = (
    filtered_df["User_Count"].sum()
)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Transactions",
    f"{total_transactions:,.0f}"
)

col2.metric(
    "Transaction Amount",
    f"₹ {total_amount:,.0f}"
)

col3.metric(
    "Average Transaction",
    f"₹ {avg_transaction:,.2f}"
)

col4.metric(
    "Total Users",
    f"{total_users:,.0f}"
)

# ------------------------------------------------
# TRANSACTION TREND
# ------------------------------------------------

st.subheader("📈 Quarterly Transaction Trend")

trend_df = filtered_df.groupby(
    ["Year", "Quarter"]
).agg({
    "Transaction_Amount": "sum"
}).reset_index()

trend_df["Period"] = (
    trend_df["Year"].astype(str)
    + "-Q"
    + trend_df["Quarter"].astype(str)
)

fig_trend = px.line(
    trend_df,
    x="Period",
    y="Transaction_Amount",
    markers=True,
    title="Quarterly Transaction Trend"
)

st.plotly_chart(
    fig_trend,
    use_container_width=True
)

# ------------------------------------------------
# TOP STATES
# ------------------------------------------------

st.subheader("🏆 Top States by Transaction Amount")

top_states = filtered_df.groupby(
    "State"
).agg({
    "Transaction_Amount": "sum"
}).reset_index()

top_states = top_states.sort_values(
    by="Transaction_Amount",
    ascending=False
)

fig_bar = px.bar(
    top_states,
    x="State",
    y="Transaction_Amount",
    color="Transaction_Amount",
    title="Top Performing States"
)

st.plotly_chart(
    fig_bar,
    use_container_width=True
)

# ------------------------------------------------
# CLUSTER VISUALIZATION
# ------------------------------------------------

st.subheader("🧠 State Clustering Analysis")

fig_cluster = px.scatter(
    cluster_df,
    x="Transaction_Count",
    y="Transaction_Amount",
    color="Cluster_Name",
    hover_name="State",
    size="User_Count",
    title="State Segmentation Using KMeans"
)

st.plotly_chart(
    fig_cluster,
    use_container_width=True
)

# ------------------------------------------------
# FRAUD DETECTION
# ------------------------------------------------

st.subheader("🚨 Suspicious Transaction Detection")

fraud_df = anomaly_df[
    anomaly_df["Anomaly"] == "Fraud/Suspicious"
]

st.dataframe(
    fraud_df[
        [
            "State",
            "Year",
            "Quarter",
            "Transaction_Amount",
            "Anomaly"
        ]
    ],
    use_container_width=True
)

# ------------------------------------------------
# FORECASTING
# ------------------------------------------------

st.subheader("🔮 Transaction Forecasting")

forecast_chart = forecast_df[
    ["ds", "yhat"]
].copy()

forecast_chart.columns = [
    "Date",
    "Predicted_Transaction_Amount"
]

forecast_chart[
    "Predicted_Transaction_Amount"
] = forecast_chart[
    "Predicted_Transaction_Amount"
].clip(lower=0)

fig_forecast = px.line(
    forecast_chart,
    x="Date",
    y="Predicted_Transaction_Amount",
    title="Future Transaction Forecast"
)

st.plotly_chart(
    fig_forecast,
    use_container_width=True
)

# ------------------------------------------------
# SUMMARY TABLE
# ------------------------------------------------

st.subheader("📋 State-Level Summary")

summary_df = filtered_df.groupby(
    "State"
).agg({
    "Transaction_Count": "sum",
    "Transaction_Amount": "sum",
    "User_Count": "sum"
}).reset_index()

st.dataframe(
    summary_df,
    use_container_width=True
)

# ------------------------------------------------
# FOOTER
# ------------------------------------------------

st.markdown("---")

st.markdown(
    """
    Built with ❤️ using Python, SQL, Machine Learning,
    Streamlit, Plotly & PhonePe Pulse Data
    """
)