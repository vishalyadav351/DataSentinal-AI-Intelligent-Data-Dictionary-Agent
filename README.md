# 🛡️ DataSentinel: Intelligent Data Dictionary & Ingestion Agent

*DataSentinel* is an enterprise-grade backend solution engineered with *FastAPI* and *SQLAlchemy. It automates dynamic data ingestion from CSV files into **MySQL* while providing real-time schema exploration and automated Data Dictionary generation.

---

## 🏗️ System Architecture
The platform is designed with a decoupled architecture to ensure high availability and security:
* *Ingestion Engine*: Handles multi-part stream processing for large CSV files.
* *Schema Intelligence*: Dynamically reflects database metadata using SQLAlchemy inspect.
* *Security Layer*: Implements environment-based abstraction for sensitive database credentials.
* *Cross-Origin Resource Sharing (CORS)*: Pre-configured for seamless frontend-backend handshake.



---

## 🚀 Key Features
* *Dynamic Ingestion*: Automated mapping of CSV headers to MySQL table columns with batch insert optimization.
* *Metadata API*: Dedicated endpoints to fetch live table structures, column types, and constraints.
* *Automated Data Dictionary*: Generates a structured view of the database schema for developers and analysts.
* *Production-Ready Logging*: Detailed error handling and transaction rollback mechanisms.

---

## 🛠️ Tech Stack & Tools
| Layer | Technology | Purpose |
| :--- | :--- | :--- |
| *Backend* | Python / FastAPI | High-performance asynchronous API framework |
| *Database* | MySQL | Robust relational data storage |
| *ORM* | SQLAlchemy | Advanced Object-Relational Mapping |
| *Security* | Python-Dotenv | Environment variable management |
| *Web Server* | Uvicorn | ASGI server implementation |

---

## 📁 Repository Structure
```text
DataSentinel-AI/
├── mycode/                # Core Application Logic
│   ├── main.py            # API Routes & Business Logic
│   └── database.py        # Database Engine & Session Config
├── .gitignore             # Git exclusion rules for security
├── requirements.txt       # Project dependencies

👥 Engineering Team
Vishal Yadav - Backend Architecture & Database Optimization
Shreyanshh Shrivastava - Lead Architect
Vibhanshu Shrivastava  - Frontend Integration & UI/UX Design

└── README.md              # Technical Documentation
