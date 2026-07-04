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
- [x] Create GCP Project
- [x] Create Google Cloud Storage Buckets
- [ ] Raw Data Ingestion
- [ ] Bronze Layer
- [ ] Silver Layer
- [ ] Gold Layer
- [ ] BigQuery
- [ ] Airflow Orchestration
- [ ] Looker Studio Dashboard

---

# Google Cloud Foundation

The Google Cloud foundation for the project has been provisioned using the Google Cloud CLI.

## GCP Project

| Property | Value |
|----------|-------|
| Project Name | gcp-alshaya-medallion |
| Platform | Google Cloud Platform |

---

## Enabled Services

The following Google Cloud services are enabled.

| Service | Purpose |
|----------|----------|
| Cloud Resource Manager API | Project management |
| Cloud Storage API | Data Lake Storage |
| BigQuery API | Analytical Data Warehouse |
| Dataproc API | Distributed PySpark Processing |

---

## Data Lake

A single Google Cloud Storage bucket is used as the Data Lake.

```text
gs://gcp-alshaya-medallion-data
```

### Bucket Structure

```text
gs://gcp-alshaya-medallion-data/

raw/
bronze/
silver/
gold/
archive/
logs/
```

The bucket follows the Medallion Architecture using logical prefixes rather than multiple buckets.

---

# Infrastructure Automation

Google Cloud resources are provisioned using the Google Cloud CLI.

Infrastructure scripts are maintained under:

```text
scripts/
```

Current scripts

```text
01-gcp-foundation.ps1
```

Additional automation scripts will be added as the platform evolves.

---

# Current Progress

## Completed

- ✅ Repository Setup
- ✅ Olist Dataset Download
- ✅ Source System Analysis
- ✅ Google Cloud Project
- ✅ Cloud SDK Configuration
- ✅ Required APIs Enabled
- ✅ Google Cloud Storage Bucket Created

---

## Next Milestone

Upload the raw Olist datasets into the Data Lake.

Target location:

```text
gs://gcp-alshaya-medallion-data/raw/olist/
```

After uploading the data, the Bronze layer implementation will begin using PySpark on Dataproc.

---

## Configuration

Project configuration is externalized using YAML files.

```text
config/
└── gcp_config.yaml
```

The configuration currently manages:

- Google Cloud Project
- Storage Bucket
- Local Dataset Location
- GCS Layer Paths
- Ingestion Settings

This approach keeps the application code environment-independent and simplifies future enhancements such as multi-environment deployments and metadata-driven ingestion.

---

## Configuration Management

Application configuration is centralized through a configuration manager.

```
config/
    gcp_config.yaml
```

Every Python module accesses configuration through:

```python
from common.config import config
```

rather than hardcoding values inside the application.

This design improves maintainability and prepares the project for future multi-environment deployments.

---

## Logging

A centralized logging framework has been implemented for the project.

Location:

```text
src/common/logger.py
```

Features:

- Console logging
- File logging
- Standardized log format
- Reusable across all project modules

Application logs are written to:

```text
logs/application.log
```

Future enhancements will include:

- Log rotation
- Separate audit logs
- Structured JSON logging
- Cloud Logging integration