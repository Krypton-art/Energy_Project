import streamlit as st
import pandas as pd
import os
from sqlalchemy import create_engine

st.set_page_config(page_title="Energy Monitoring System", layout="wide")

st.title("⚡ Energy Consumption Monitoring System")

# -------------------------------
# Snowflake Connection
# -------------------------------

@st.cache_resource
def get_engine():
    user = os.getenv("SNOWFLAKE_USER")
    password = os.getenv("SNOWFLAKE_PASSWORD")
    account = os.getenv("SNOWFLAKE_ACCOUNT")
    warehouse = os.getenv("SNOWFLAKE_WAREHOUSE")
    database = os.getenv("SNOWFLAKE_DATABASE")
    schema = os.getenv("SNOWFLAKE_SCHEMA")

    connection_string = (
        f"snowflake://{user}:{password}@{account}/"
        f"{database}/{schema}?warehouse={warehouse}"
    )

    engine = create_engine(connection_string)
    return engine

engine = get_engine()

# -------------------------------
# Queries
# -------------------------------

query_total = """
SELECT SUM(CONSUMPTION_KWH) AS TOTAL_CONSUMPTION
FROM FACT_ENERGY_USAGE;
"""

query_monthly = """
SELECT 
    YEAR(DATE) AS YEAR,
    MONTH(DATE) AS MONTH,
    SUM(CONSUMPTION_KWH) AS MONTHLY_CONSUMPTION
FROM FACT_ENERGY_USAGE
GROUP BY YEAR(DATE), MONTH(DATE)
ORDER BY YEAR, MONTH;
"""

query_top = """
SELECT 
    CUSTOMER_ID,
    SUM(CONSUMPTION_KWH) AS TOTAL_USAGE
FROM FACT_ENERGY_USAGE
GROUP BY CUSTOMER_ID
ORDER BY TOTAL_USAGE DESC
LIMIT 5;
"""

# -------------------------------
# Fetch Data
# -------------------------------

try:
    total_df = pd.read_sql(query_total, engine)
    monthly_df = pd.read_sql(query_monthly, engine)
    top_df = pd.read_sql(query_top, engine)

    # -------------------------------
    # Dashboard Layout
    # -------------------------------

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Total Energy Consumption (kWh)",
            f"{int(total_df.iloc[0,0])}"
        )

    with col2:
        st.dataframe(top_df)

    st.subheader("📊 Monthly Consumption Trend")
    # -----------------------------
    # Monthly Consumption Trend
    # -----------------------------

    st.subheader("📊 Monthly Consumption Trend")

    query_monthly = """
    SELECT 
        T.MONTH,
        SUM(F.CONSUMPTION_KWH) AS TOTAL_USAGE
    FROM FACT_ENERGY_USAGE F
    JOIN DIM_TIME T
        ON F.DATE = T.DATE
    GROUP BY T.MONTH
    ORDER BY T.MONTH

    """

    monthly_df = pd.read_sql(query_monthly, engine)


    monthly_df.columns = monthly_df.columns.str.upper()

    st.line_chart(
        monthly_df.set_index(monthly_df.columns[0])[monthly_df.columns[1]]
    )

except Exception as e:
    st.error("Error connecting to Snowflake")
    st.write(e)