# Energy_Project
End-to-End Data Engineering Pipeline for Energy Consumption Analytics
# ⚡ Energy Consumption Monitoring System

## 📌 Overview
This project implements an end-to-end data engineering pipeline for analyzing energy consumption data. It demonstrates data warehousing, ETL processing, advanced SQL analytics, batch processing with Spark, and interactive dashboard visualization.

---

## 🏗 Architecture

Energy CSV → Python ETL → PostgreSQL Data Warehouse → Advanced SQL → PySpark Batch Processing → Streamlit Dashboard

---

## 🗄 Data Warehouse Design

- Star Schema Model
- Fact Table: `fact_energy_usage`
- Dimension Tables:
  - `dim_customer`
  - `dim_time`
  - `dim_location`

---

## 🔄 ETL Pipeline

- Data extraction from CSV
- Cleaning & transformation using Pandas
- Loading into PostgreSQL using Psycopg2

---

## 📊 Advanced SQL

- Common Table Expressions (CTE)
- Window Functions (RANK, Moving Average)
- Indexing & Performance Optimization
- Query Profiling using EXPLAIN ANALYZE

---

## ⚡ Apache Spark

- Batch processing in local mode
- Monthly aggregation
- Scalable architecture simulation

---

## 📈 Dashboard

Built using Streamlit:
- KPI Metrics
- Monthly Trends
- Top Customers
- Interactive Visualization

---

## 🚀 Technologies Used

- Python
- PostgreSQL
- Apache Spark
- Streamlit
- Pandas
- Advanced SQL

---

## 🔮 Future Improvements

- Real-time streaming with Kafka
- Cloud warehouse (Snowflake/BigQuery)
- Machine Learning for consumption forecasting
- Docker containerization

---

## 👨‍💻 Author
Somya
