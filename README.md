# GCP Alshaya Medallion

Enterprise-grade Retail Data Platform built on **Google Cloud Platform (GCP)** using the **Medallion Architecture (Bronze → Silver → Gold)**.

> **Status:** 🚧 In Development

---

# Project Objective

This project demonstrates the implementation of an end-to-end Retail Data Platform using Google Cloud Platform.

The objective is to build a scalable data engineering solution that ingests raw retail data into Google Cloud Storage, processes it through the Medallion Architecture, stores curated datasets in BigQuery, and visualizes business insights using Looker Studio.

---

# Technology Stack

| Category | Technology |
|----------|------------|
| Cloud | Google Cloud Platform |
| Storage | Google Cloud Storage |
| Processing | Dataproc (PySpark) |
| Data Warehouse | BigQuery |
| Orchestration | Cloud Composer (Airflow) |
| Visualization | Looker Studio |
| Language | Python |
| Version Control | GitHub |

---

# Project Structure

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

# Dataset

This project uses the **Brazilian E-Commerce Public Dataset by Olist**, available on Kaggle.

The dataset contains information about:

- Customers
- Orders
- Order Items
- Payments
- Products
- Sellers
- Reviews
- Geolocations

It closely resembles a real-world retail transactional system, making it an excellent dataset for implementing the Medallion Architecture.

---

# Dataset Schema

The following diagram illustrates the relationships between the source datasets.

> Place the image in `docs/images/olist-dataset-schema.png`

<p align="center">
    <img src="docs/images/olist-dataset-schema.png" width="900">
</p>

---

# Current Progress

## ✅ Completed

- Repository setup
- Initial project structure
- Downloaded Olist dataset
- Dataset added locally under

```
data/sample/kaggle/olist/
```

---

## 🚧 In Progress

- Understanding dataset relationships
- Designing Medallion Architecture

---

# Development Roadmap

- [x] Repository Setup
- [x] Download Olist Dataset
- [ ] Dataset Analysis
- [ ] Data Model Design
- [ ] Create GCP Project
- [ ] Create GCS Buckets
- [ ] Upload Raw Data
- [ ] Bronze Layer
- [ ] Silver Layer
- [ ] Gold Layer
- [ ] BigQuery
- [ ] Airflow
- [ ] Looker Studio Dashboard

---

# High-Level Architecture

```
                Kaggle (Olist Dataset)
                         │
                         ▼
               Google Cloud Storage
                         │
                         ▼
                 Bronze (Raw Layer)
                         │
                PySpark Transformations
                         ▼
                Silver (Clean Layer)
                         │
                Business Transformations
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

# Next Milestone

The next milestone is to analyze the Olist dataset and design the Medallion data model.

This includes:

- Identifying source entities
- Understanding primary and foreign keys
- Classifying fact and dimension tables
- Defining Bronze, Silver, and Gold datasets
- Designing the BigQuery target model

