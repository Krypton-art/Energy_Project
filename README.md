⚡ Energy Consumption Monitoring System

A cloud-based data warehousing and analytics system built using Snowflake and Streamlit.
This project demonstrates real-world data engineering concepts, including Star Schema design, SQL analytics, and secure cloud deployment.

🚀 Project Overview

This system:

Stores energy consumption data inside Snowflake

Implements a Star Schema Data Warehouse

Performs aggregations directly in the warehouse

Connects securely using SQLAlchemy

Displays insights through a live Streamlit dashboard

All heavy computations are executed inside Snowflake — not locally.

🏗 System Architecture
Streamlit Cloud (Frontend + Python App)
            │
            ▼
     SQLAlchemy Connection
            │
            ▼
   Snowflake Cloud Data Warehouse
            │
            ▼
     Star Schema (Fact + Dimensions)
🗄 Data Warehouse Design
⭐ Fact Table

FACT_ENERGY_USAGE

Column	Description
CUSTOMER_ID	Unique customer identifier
DATE	Energy usage date
CONSUMPTION_KWH	Energy consumed (kWh)
COST	Cost of consumption

Stores transactional energy usage records.

📘 Dimension Tables
DIM_TIME

DATE

MONTH

YEAR

Used for time-based aggregations.

DIM_CUSTOMER

CUSTOMER_ID

CUSTOMER_TYPE

Used for customer-level analytics.

📊 Implemented Features

✔ Total Energy Consumption KPI
✔ Monthly Consumption Trend (Fact–Dimension JOIN)
✔ Top Customers by Usage
✔ SQL Aggregations (SUM, GROUP BY)
✔ Cloud-to-Cloud Integration
✔ Secure Secrets Management
✔ Live Dashboard Deployment

🔐 Security Implementation

Credentials stored using Streamlit Cloud Secrets

No hardcoded passwords in the repository

Secure SQLAlchemy connection string

All processing handled inside Snowflake

🧠 Tech Stack

❄ Snowflake (Cloud Data Warehouse)

🐍 Python

🧮 SQL

🔗 SQLAlchemy

📊 Pandas

📈 Streamlit

🌐 Streamlit Cloud

🗂 GitHub

📈 Analytics Performed

Total consumption calculation

Monthly aggregation using Star Schema JOIN

Customer-level ranking

Cloud-executed SQL queries

🎯 Key Highlights

Implements Star Schema Data Modeling

Uses cloud-native data warehousing

Demonstrates real-time dashboard deployment

Follows secure credential management practices

Simulates a production-grade analytics pipeline

🌐 Live Application

🔗 (https://energy-consumption-monitoring-system.streamlit.app/)

📌 Why This Project Matters

This project demonstrates practical knowledge of:

Data Warehousing Concepts

Cloud Database Integration

SQL-Based Analytics

Secure Deployment Practices

End-to-End Data Engineering Workflow

It reflects how modern analytics systems are built in real production environments.
