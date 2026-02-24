<div align="center">

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=32&duration=3000&pause=1000&color=29B5E8&center=true&vCenter=true&width=600&lines=Energy+Consumption+Monitor;Cloud-Native+Analytics+Platform" alt="Typing SVG" />

<br/>

# ⚡ Energy Consumption Monitoring System
### Cloud-Native Data Warehouse & Analytics Platform

<br/>

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Snowflake](https://img.shields.io/badge/Snowflake-Cloud_DWH-29B5E8?style=for-the-badge&logo=snowflake&logoColor=white)](https://snowflake.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)](https://sqlalchemy.org)
[![Pandas](https://img.shields.io/badge/Pandas-Data_Processing-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![Deployed](https://img.shields.io/badge/Live-Streamlit_Cloud-success?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/cloud)

<br/>

> 🚀 A **production-style, cloud-native analytics system** built using **Snowflake** and **Streamlit** that ingests, models, aggregates, and visualizes energy consumption data using a **Star Schema** warehouse design.

<br/>

[🔴 Live Demo](https://energy-consumption-monitoring-system.streamlit.app/) &nbsp;·&nbsp; 

<br/>

---

</div>

## 📋 Table of Contents

- [Executive Summary](#-executive-summary)
- [Problem Statement](#-problem-statement)
- [System Architecture](#-system-architecture)
- [Data Modeling Strategy](#-data-modeling-strategy)
- [Data Flow Pipeline](#-data-flow-pipeline)
- [Core Features](#-core-features)
- [Performance](#-performance-considerations)
- [Security](#-security-architecture)
- [Scalability](#-scalability)
- [Deployment](#-deployment-strategy)
- [Tech Stack](#-technical-stack)
- [Getting Started](#-getting-started)
- [Future Work](#-future-work)
- [Key Takeaways](#-key-engineering-takeaways)

---

## 🧭 Executive Summary

This project demonstrates a **production-grade, cloud-native analytics pipeline** for energy consumption monitoring. Built with dimensional modeling principles at its core, the system handles data ingestion, transformation, aggregation, and visualization entirely within cloud infrastructure.

<br/>

<div align="center">

| 🏛️ Principle | ⚙️ Implementation |
|:------------|:-----------------|
| Dimensional Data Modeling | Star Schema — Fact & Dimension Tables |
| Cloud-Native Architecture | Snowflake on AWS + Streamlit Cloud |
| Secure Connectivity | SQLAlchemy + Environment-Based Secrets |
| Analytical Execution | All Queries Run Inside Snowflake Compute |
| Separation of Concerns | Compute, Storage & Presentation Decoupled |

</div>

<br/>

> 💡 All analytical queries are executed **inside Snowflake**. The frontend connects securely via **SQLAlchemy** — ensuring no raw data is transferred to the application layer.

---

## ❗ Problem Statement

Energy providers generate massive volumes of consumption data that must be:

- 📦 **Modeled efficiently** — using warehouse-native dimensional structures
- 🔢 **Aggregated accurately** — with performant SQL across large datasets
- ☁️ **Queried at scale** — leveraging cloud compute elasticity
- 📊 **Visualized interactively** — through a live, user-facing dashboard
- 🔐 **Secured in production** — with credential isolation and encrypted communication

> This project simulates the **modern analytics architecture** used in production data engineering environments at energy, utility, and infrastructure companies.

---

## 🏗️ System Architecture

```
╔══════════════════════════════════════════════════════════════════╗
║                      PRESENTATION LAYER                         ║
║                                                                  ║
║                  ┌──────────────────────────┐                   ║
║                  │     Streamlit Cloud       │                   ║
║                  │   Interactive Dashboard   │                   ║
║                  └────────────┬─────────────┘                   ║
╚═══════════════════════════════│══════════════════════════════════╝
                                │  HTTPS / Encrypted
╔═══════════════════════════════│══════════════════════════════════╗
║                      APPLICATION LAYER                          ║
║                                                                  ║
║  ┌──────────────┐    ┌─────────────────┐    ┌────────────────┐  ║
║  │    Python    │───▶│   SQLAlchemy    │───▶│  Secrets Mgmt  ║  ║
║  │  App Logic   │    │   Connector     │    │ (Env Variables)║  ║
║  └──────────────┘    └─────────────────┘    └────────────────┘  ║
╚═══════════════════════════════│══════════════════════════════════╝
                                │  Secure Cloud-to-Cloud
╔═══════════════════════════════│══════════════════════════════════╗
║                         DATA LAYER                              ║
║                                                                  ║
║    ┌───────────────────────────────────────────────────────┐    ║
║    │           Snowflake Cloud Data Warehouse              ║    ║
║    │                                                       ║    ║
║    │   ┌─────────────────┐     ┌──────────────────────┐   ║    ║
║    │   │ FACT_ENERGY_    │────▶│  DIM_TIME            │   ║    ║
║    │   │ USAGE           │────▶│  DIM_CUSTOMER        │   ║    ║
║    │   └─────────────────┘     └──────────────────────┘   ║    ║
║    │             Star Schema (Dimensional Model)           ║    ║
║    └───────────────────────────────────────────────────────┘    ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## 📐 Data Modeling Strategy

### Why Star Schema?

> Star Schema was selected over normalized OLTP designs because it is purpose-built for analytics — fewer joins, faster aggregation, and maximum query clarity.

<div align="center">

| ✅ Benefit | 📌 Reason |
|:----------|:---------|
| Simpler Analytical Queries | Flat structure, minimal joins |
| Faster Aggregation | Optimized for GROUP BY & window functions |
| Clear Separation | Facts (metrics) vs Dimensions (context) |
| Industry Standard | Follows Kimball dimensional modeling methodology |

</div>

<br/>

### Schema Diagram

```
                      ┌─────────────────┐
                      │    DIM_TIME     │
                      │─────────────────│
                      │ 📅 DATE (PK)   │
                      │    MONTH        │
                      │    YEAR         │
                      └────────┬────────┘
                               │ FK
                               │
 ┌─────────────────┐   ┌───────┴──────────────┐
 │  DIM_CUSTOMER   │   │  FACT_ENERGY_USAGE   │
 │─────────────────│   │──────────────────────│
 │ 👤 CUSTOMER_ID  │◀──│ CUSTOMER_ID (FK)     │
 │   CUSTOMER_TYPE │   │ DATE (FK)            │
 └─────────────────┘   │ ⚡ CONSUMPTION_KWH   │
                       │ 💰 COST              │
                       └──────────────────────┘
```

> **Normalization Decision:** Dimension tables are intentionally **denormalized** (no snowflaking) to maximize read performance. This trades minor storage overhead for significantly faster query execution — the standard trade-off in OLAP design.

---

## 🔄 Data Flow Pipeline

```
  📂 Raw Source Data
         │
         ▼
  ┌──────────────────┐
  │  Snowflake       │  ◀── COPY INTO / Direct Insert
  │  Raw Staging     │
  └────────┬─────────┘
           │ SQL Transformation
           ▼
  ┌──────────────────────────────┐
  │     Star Schema Tables       │
  │  ├── FACT_ENERGY_USAGE       │
  │  ├── DIM_TIME                │
  │  └── DIM_CUSTOMER            │
  └────────┬─────────────────────┘
           │ Aggregation Queries
           ▼
  ┌──────────────────────────────┐
  │   Aggregated Query Results   │  ◀── GROUP BY, JOINs, KPI Logic
  │   (executed in Snowflake)    │      runs entirely in warehouse
  └────────┬─────────────────────┘
           │ SQLAlchemy → Pandas
           ▼
  ┌──────────────────────────────┐
  │   📊 Streamlit Dashboard     │  ◀── Renders charts, KPIs, tables
  └──────────────────────────────┘
```

---

## ✨ Core Features

<div align="center">

| Feature | Description | Status |
|:--------|:-----------|:------:|
| 📊 Total Energy KPI | Aggregated consumption KPIs across customer base | ✅ |
| 📈 Monthly Trend Analysis | Time-series visualization of energy usage | ✅ |
| 🏆 Top Customer Ranking | Customers ranked by consumption or cost | ✅ |
| 🔗 Fact–Dimension JOIN Queries | Star schema dimensional analysis queries | ✅ |
| 🔐 Secure Cloud Deployment | No hardcoded credentials, secrets via env | ✅ |
| 👥 Role-Based Access Control | Least-privilege Snowflake roles | ✅ |
| 📦 Semi-Structured Data | VARIANT column support for JSON payloads | 🔜 |
| ⚡ Clustering & Optimization | Snowflake clustering keys for performance | 🔜 |

</div>

---

## ⚙️ Performance Considerations

The system is architected to push **all computation to the warehouse**, not the application layer:

- **⚡ Warehouse-side aggregation** — GROUP BY runs on Snowflake virtual warehouses, not Python
- **📉 Minimal data transfer** — only aggregated results returned to the frontend
- **🔗 Efficient dimensional joins** — Star Schema reduces join complexity by design
- **☁️ Cloud auto-scaling** — Snowflake scales compute independently from storage
- **🔍 Query pruning** — date/customer filters minimize scan volume on large fact tables

---

## 🔒 Security Architecture

```
╔══════════════════════════════════════════════════════╗
║              🔐 Security Layers                     ║
╠══════════════════════════════════════════════════════╣
║  ✅  Credentials stored as environment secrets      ║
║  ✅  No hardcoded passwords or connection strings   ║
║  ✅  Secure SQLAlchemy connection with SSL          ║
║  ✅  Cloud-to-cloud encrypted communication         ║
║  ✅  Principle of least privilege (Snowflake roles) ║
║  ✅  secrets.toml excluded from version control     ║
╚══════════════════════════════════════════════════════╝
```

> Secrets are injected at runtime via **Streamlit Cloud's secrets management** and accessed through `st.secrets` — credentials are never exposed in source code or version control.

---

## 📈 Scalability

<div align="center">

| Scale Dimension | Approach |
|:---------------|:---------|
| 📊 Larger Datasets | Snowflake auto-scales virtual warehouse compute |
| 🌊 Real-Time Ingestion | Add Snowpipe or Apache Kafka — no schema changes needed |
| 📉 BI Tool Integration | Power BI, Tableau, Looker connect via JDBC/ODBC directly |
| 🏗️ Schema Extension | New dimensions/facts added without touching existing queries |
| 👥 Multi-Team Access | Snowflake RBAC enables row & column level security |

</div>

---

## 🚀 Deployment Strategy

```
  👨‍💻 Developer
       │
       │  git push
       ▼
  📦 GitHub Repository
       │
       ├─────────────────────────┐
       ▼                         ▼
  🌐 Streamlit Cloud        ⚙️ GitHub Actions
  (Auto-deploys on push)    (CI/CD Pipeline)
       │
       ▼
  📊 Live Dashboard
  (Connects to Snowflake on AWS)
```

<div align="center">

| Component | Hosting |
|:----------|:--------|
| 📊 Frontend Dashboard | Streamlit Cloud |
| 🏔️ Data Warehouse | Snowflake (AWS Infrastructure) |
| 📁 Source Control | GitHub |
| 🔄 Deployment Trigger | Push to `main` branch |
| 🔐 Secret Management | Streamlit Cloud Secrets |

</div>

---

## 🛠️ Technical Stack

<div align="center">

| Layer | Technology | Purpose |
|:------|:----------|:--------|
| ☁️ Warehouse | ![Snowflake](https://img.shields.io/badge/Snowflake-29B5E8?style=flat-square&logo=snowflake&logoColor=white) | Cloud DWH, SQL execution, storage |
| 🗄️ Query Language | ![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat-square&logo=postgresql&logoColor=white) | Aggregations, joins, transformations |
| 🐍 Backend | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) | Application logic, data routing |
| 🔌 Connector | ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=flat-square&logo=sqlalchemy&logoColor=white) | Secure Snowflake connection |
| 📊 Processing | ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white) | DataFrame handling post-query |
| 🖥️ Frontend | ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white) | Interactive dashboard UI |
| 🌐 Deployment | ![Streamlit Cloud](https://img.shields.io/badge/Streamlit_Cloud-FF4B4B?style=flat-square&logo=streamlit&logoColor=white) | Hosted frontend & secrets |
| 📁 Version Control | ![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white) | Source control & CI/CD trigger |

</div>

---

## 🚦 Getting Started

### Prerequisites

- Python 3.11+
- Snowflake account ([free trial](https://signup.snowflake.com/))
- Streamlit Cloud account ([free](https://streamlit.io/cloud))

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/energy-monitoring-system.git
cd energy-monitoring-system
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Configure Secrets

Create `.streamlit/secrets.toml` for local development:

```toml
[snowflake]
account   = "your_account_identifier"
user      = "your_username"
password  = "your_password"
warehouse = "your_warehouse"
database  = "ENERGY_DB"
schema    = "PUBLIC"
role      = "your_role"
```

> ⚠️ **Never commit `secrets.toml` to version control.** Add it to `.gitignore`.

### 4️⃣ Set Up Snowflake Schema

```sql
-- Fact Table
CREATE TABLE FACT_ENERGY_USAGE (
    CUSTOMER_ID     VARCHAR,
    DATE            DATE,
    CONSUMPTION_KWH FLOAT,
    COST            FLOAT
);

-- Time Dimension
CREATE TABLE DIM_TIME (
    DATE   DATE PRIMARY KEY,
    MONTH  INT,
    YEAR   INT
);

-- Customer Dimension
CREATE TABLE DIM_CUSTOMER (
    CUSTOMER_ID   VARCHAR PRIMARY KEY,
    CUSTOMER_TYPE VARCHAR
);
```

### 5️⃣ Run Locally

```bash
streamlit run app.py
```

### 6️⃣ Deploy to Streamlit Cloud

Push to GitHub → connect repo in [Streamlit Cloud](https://streamlit.io/cloud) → add secrets under **App Settings → Secrets** → done. ✅

---

## 🔭 Future Work

<div align="center">

| Enhancement | Description | Priority |
|:-----------|:-----------|:--------:|
| 🌊 Real-Time Streaming | Snowpipe or Kafka continuous ingestion | 🔴 High |
| 🤖 ML Forecasting | Prophet / scikit-learn for consumption prediction | 🟠 Medium |
| 🗂️ Partitioning | Snowflake clustering keys on DATE column | 🟠 Medium |
| 🛡️ Advanced RBAC | Row-level security and column masking policies | 🟡 Low |
| 📊 Query Benchmarking | Analysis via `QUERY_HISTORY` view | 🟡 Low |
| 🔍 Observability | Datadog / OpenTelemetry pipeline monitoring | 🟡 Low |
| 🏗️ dbt Integration | Replace SQL transforms with dbt models | 🟠 Medium |

</div>

---

## 💡 Key Engineering Takeaways

> This project demonstrates that **production-grade data engineering** is defined not just by technology choices, but by architectural decisions.

1. **📐 Dimensional modeling** separates analytical concerns from transactional ones — enabling queries that are both performant and readable.

2. **☁️ Cloud-native infrastructure** eliminates operational overhead. Snowflake's separation of compute and storage means you scale cost-effectively.

3. **🔐 Secure secret management** is non-negotiable. Hardcoded credentials are a deployment-time bug waiting to become a security incident.

4. **🏛️ Layer separation** — presentation, application, data — is what makes a system extensible. Each layer evolves independently.

5. **⚡ Push computation to the warehouse.** The database is optimized for it. Python is not.

---

## ✅ Why This Is Production-Grade

<div align="center">

| Criterion | Status |
|:----------|:------:|
| Clear separation of architectural layers | ✅ |
| Cloud-native infrastructure (no local servers) | ✅ |
| Secure credential management (no hardcoding) | ✅ |
| All computation inside the warehouse | ✅ |
| Scalable warehouse architecture | ✅ |
| Proper dimensional data modeling | ✅ |
| Continuous deployment pipeline | ✅ |
| Extensible schema design | ✅ |

</div>


<br/>

*Made with ❤️ and ☁️*

</div>
