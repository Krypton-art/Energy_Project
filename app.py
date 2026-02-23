import streamlit as st
import pandas as pd
import psycopg2

st.title("Energy Consumption Monitoring Dashboard")

# Database connection
conn = psycopg2.connect(
    dbname="energy_dw",
    user="postgres",
    password="yeahitsme",
    host="localhost",
    port="5432"
)

# Total consumption
query_total = """
SELECT SUM(consumption_kwh) FROM fact_energy_usage;
"""
total = pd.read_sql(query_total, conn)

st.metric("Total Energy Consumption (kWh)", round(total.iloc[0,0],2))

# Monthly trend
query_monthly = """
SELECT dt.year, dt.month, SUM(f.consumption_kwh) as total
FROM fact_energy_usage f
JOIN dim_time dt ON f.time_id = dt.time_id
GROUP BY dt.year, dt.month
ORDER BY dt.year, dt.month;
"""

monthly = pd.read_sql(query_monthly, conn)
st.line_chart(monthly["total"])

# Top 5 customers
query_top = """
SELECT customer_id, SUM(consumption_kwh) as total_usage
FROM fact_energy_usage
GROUP BY customer_id
ORDER BY total_usage DESC
LIMIT 5;
"""

top_customers = pd.read_sql(query_top, conn)
st.bar_chart(top_customers.set_index("customer_id"))

conn.close()