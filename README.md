⚡ Energy Consumption Monitoring System

A cloud-based Energy Consumption Monitoring System built using Snowflake Data Warehouse and Streamlit, designed with a Star Schema architecture and deployed as a live cloud dashboard.

📌 Project Overview

This project demonstrates a complete end-to-end data engineering workflow:

Data ingestion

Data warehouse modeling (Star Schema)

Advanced SQL aggregation

Cloud data storage (Snowflake)

Secure cloud deployment

Interactive dashboard visualization

All analytics computations are executed inside Snowflake, and results are visualized via a live Streamlit dashboard.

🏗 System Architecture
Streamlit Cloud (Frontend + Python)
        │
        │  SQLAlchemy Connection
        ▼
Snowflake Cloud Data Warehouse
        │
        ▼
Star Schema (Fact + Dimension Tables)
🗄 Data Warehouse Design
⭐ Fact Table

FACT_ENERGY_USAGE

CUSTOMER_ID

DATE

CONSUMPTION_KWH

COST

Stores transactional energy consumption records.

📘 Dimension Tables

DIM_TIME

DATE

MONTH

YEAR

DIM_CUSTOMER

CUSTOMER_ID

CUSTOMER_TYPE

Dimension tables are used to normalize data and improve aggregation performance.

📊 Features

✔ Star Schema Data Modeling
✔ SQL Aggregations (SUM, GROUP BY, JOIN)
✔ Fact–Dimension JOIN Queries
✔ Monthly Consumption Trend Analysis
✔ Top Customer Analysis
✔ Secure Cloud-to-Cloud Integration
✔ Live Deployment
✔ Snowflake + Streamlit Integration

🚀 Live Dashboard

🔗 Live Application:
((https://energy-consumption-monitoring-system.streamlit.app/))

🔐 Security Implementation

Snowflake credentials stored securely using Streamlit Cloud Secrets

No hardcoded passwords in source code

Secure SQLAlchemy connection string

Cloud-to-cloud communication

🧠 Tech Stack

❄ Snowflake (Cloud Data Warehouse)

🐍 Python

🧮 SQL

🔗 SQLAlchemy

📊 Pandas

📈 Streamlit

🌐 Streamlit Cloud

🗂 GitHub

📈 Sample Analytics Implemented

Total Energy Consumption KPI

Monthly Consumption Trend

Top Customers by Usage

Star Schema Join Queries

🎯 Key Learning Outcomes

Designing a Star Schema Data Warehouse

Connecting Cloud Applications to Snowflake

Writing optimized SQL aggregation queries

Secure credential management

Deploying real-time cloud dashboards

📌 Why This Project Matters

This project demonstrates:

Practical data warehousing skills

Cloud-based analytics architecture

Real-world deployment experience

End-to-end data engineering workflow

It simulates how production analytics systems are built in modern cloud environments.
