# GCP Alshaya Medallion

Enterprise-grade Retail Data Platform built on **Google Cloud Platform (GCP)** using the **Medallion Architecture (Bronze → Silver → Gold)**.

> **Project Status:** 🚧 Phase 1 - Dataset Discovery & Data Modeling

---

# Project Objective

This project demonstrates the design and implementation of an end-to-end Retail Data Platform on Google Cloud Platform.

The platform follows the Medallion Architecture to transform raw retail data into analytics-ready datasets using cloud-native technologies.

---

# Technology Stack

| Category | Technology |
|----------|------------|
| Cloud Platform | Google Cloud Platform (GCP) |
| Storage | Google Cloud Storage |
| Processing | Dataproc (PySpark) |
| Data Warehouse | BigQuery |
| Orchestration | Cloud Composer (Airflow) |
| Visualization | Looker Studio |
| Programming | Python |
| Version Control | Git & GitHub |

---

# Medallion Architecture

```
                     Raw Retail Data
                            │
                            ▼
                Google Cloud Storage
                            │
                            ▼
                  Bronze (Raw Layer)
                            │
                    Data Validation
                            │
                            ▼
                 Silver (Clean Layer)
                            │
                 Business Transformations
                            │
                            ▼
                 Gold (Analytics Layer)
                            │
                            ▼
                      BigQuery
                            │
                            ▼
                    Looker Studio
```

---

# Dataset

This project uses the **Brazilian E-Commerce Public Dataset by Olist** available on Kaggle.

The dataset consists of multiple related entities representing a real-world retail platform.

### Dataset Entities

- Customers
- Orders
- Order Items
- Payments
- Products
- Sellers
- Reviews
- Geolocation
- Product Category Translation

---

### Dataset Schema

The following diagram illustrates the relationships between the source datasets.


<p align="center">
    <img src="docs/images/olist-dataset-schema.png" width="900">
</p>

Check out [Kaggle DataSet Link](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) for more details.

---

# Repository Structure

```text
gcp-alshaya-medallion/
│
├── airflow/
├── config/
├── data/
│   ├── sample/
│   │   └── kaggle/
│   │       └── olist/
│   └── schemas/
├── docs/
│   └── images/
├── sql/
├── src/
│   ├── common/
│   │   └── dataset_profiler.py
│   ├── ingestion/
│   ├── bronze/
│   ├── silver/
│   └── gold/
├── tests/
│
├── README.md
├── bootstrap.py
├── requirements.txt
└── .gitignore
```

---

# Current Progress

## ✅ Completed

- Repository setup
- Initial project structure
- Bootstrap utility
- Downloaded Olist dataset
- Added dataset schema diagram
- Created Dataset Profiler utility

---

# Dataset Location

The downloaded Kaggle dataset is stored locally under:

```text
data/sample/kaggle/olist/
```

> The dataset is ignored by Git and will **not** be committed to the repository.

---

# Dataset Profiler

To better understand the source system before building ETL pipelines, a lightweight dataset profiling utility has been created.

### Features

- Reads every CSV file
- Displays row count
- Displays column count
- Lists data types
- Shows null counts
- Prints sample records

### Run

```bash
python src/common/dataset_profiler.py
```

Example Output

```text
================================================================================
Dataset : olist_orders_dataset.csv
================================================================================

Rows    : 99,441
Columns : 8

Column Information

Column                      Data Type    Null Count
---------------------------------------------------
order_id                    object              0
customer_id                 object              0
order_status                object              0
...
```

---

# Development Roadmap

- [x] Repository Setup
- [x] Download Olist Dataset
- [x] Dataset Profiling
- [ ] Source System Analysis
- [ ] Data Modeling
- [ ] Create GCP Project
- [ ] Create Google Cloud Storage Buckets
- [ ] Raw Data Ingestion
- [ ] Bronze Layer
- [ ] Silver Layer
- [ ] Gold Layer
- [ ] BigQuery
- [ ] Airflow Orchestration
- [ ] Looker Studio Dashboard

---

# Next Milestone

The next milestone is to perform a detailed analysis of the Olist source system.

Activities include:

- Identify primary keys
- Identify foreign keys
- Understand relationships
- Identify fact and dimension tables
- Design Bronze layer
- Design Silver layer
- Design Gold layer

This analysis will become the blueprint for implementing the Medallion Architecture.

---

# License

This project is intended for learning and portfolio purposes.