⚡ Energy Consumption Monitoring System

A cloud-based Energy Consumption Monitoring System built using Snowflake (Cloud Data Warehouse) and Streamlit.
This project demonstrates a complete end-to-end data engineering workflow including data modeling, SQL analytics, cloud integration, and live dashboard deployment.

📌 Project Overview

This system stores and processes energy usage data inside Snowflake using a Star Schema design.
All heavy computations (aggregations, joins, grouping) are performed inside Snowflake, and results are visualized through a live Streamlit dashboard.

The application is deployed on Streamlit Cloud and securely connects to Snowflake using SQLAlchemy.

🏗 System Architecture

Streamlit Cloud (Frontend + Python App)
→ SQLAlchemy Connection
→ Snowflake Cloud Data Warehouse
→ Star Schema (Fact + Dimension Tables)

🗄 Data Warehouse Design
Fact Table

FACT_ENERGY_USAGE

CUSTOMER_ID

DATE

CONSUMPTION_KWH

COST

This table stores transactional energy consumption records.

Dimension Tables

DIM_TIME

DATE

MONTH

YEAR

DIM_CUSTOMER

CUSTOMER_ID

CUSTOMER_TYPE

Dimension tables are used to normalize time and customer data and support efficient aggregation queries.

📊 Implemented Features

Star Schema data modeling

Fact and dimension table joins

Monthly energy consumption trend analysis

Top customers by energy usage

Total energy KPI calculation

Secure Snowflake connection using environment secrets

Cloud-to-cloud deployment (Streamlit → Snowflake)

🚀 Live Dashboard

Live Application Link:
(Add your Streamlit link here)

🔐 Security

Snowflake credentials are stored securely using Streamlit Cloud Secrets.

No hardcoded credentials in the repository.

Secure SQLAlchemy-based connection.

All processing happens inside Snowflake.

🧠 Tech Stack

Snowflake (Cloud Data Warehouse)

SQL

Python

SQLAlchemy

Pandas

Streamlit

GitHub

Streamlit Cloud

📈 Analytics Demonstrated

Total Energy Consumption (KPI)

Monthly Consumption Trend

Top Customers by Usage

Star Schema JOIN queries

🎯 Key Learning Outcomes

Designing a Star Schema Data Warehouse

Writing aggregation queries in Snowflake

Cloud database integration using SQLAlchemy

Secure secret management

Deploying real-time dashboards

This project simulates a real-world cloud-based analytics system used in modern data engineering environments.
