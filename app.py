import streamlit as st
import pandas as pd

st.set_page_config(page_title="Energy Monitoring System", layout="wide")

st.title("⚡ Energy Consumption Monitoring Dashboard")

st.markdown("End-to-End Data Engineering Project Demo")

# Load aggregated data
df = pd.read_csv("monthly_aggregated.csv")

# KPI
total_energy = df["total_consumption"].sum()
st.metric("Total Energy Consumption (kWh)", round(total_energy, 2))

st.divider()

# Layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("Monthly Energy Consumption Trend")
    st.line_chart(df["total_consumption"])

with col2:
    st.subheader("Monthly Consumption Distribution")
    st.bar_chart(df.set_index("month")["total_consumption"])

st.divider()

st.success("Project Architecture: CSV → ETL → PostgreSQL → SQL → Spark → Streamlit")