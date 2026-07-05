# GCP Alshaya Medallion

Enterprise-grade Retail Data Platform built on **Google Cloud Platform (GCP)** using the **Medallion Architecture (Raw → Bronze → Silver → Gold)**.

> **Status:** Sprint 1 Completed (Foundation + Raw Data Ingestion)

---

# Project Overview

This project demonstrates the design and implementation of an enterprise-style Retail Data Platform on Google Cloud Platform.

The platform is being developed incrementally using software engineering best practices and modern data engineering principles.

## Objectives

- Build a metadata-driven ingestion framework
- Implement the Medallion Architecture
- Process data using PySpark on Dataproc
- Publish curated datasets to BigQuery
- Visualize business insights using Looker Studio
- Follow production-oriented coding and repository standards

---

# High-Level Architecture

```text
Local CSV Files
      │
      ▼
Google Cloud Storage
      │
      ├── Raw
      ├── Bronze
      ├── Silver
      └── Gold
              │
              ▼
          BigQuery
              │
              ▼
        Looker Studio
```

---

# Technology Stack

| Category | Technology |
|----------|------------|
| Cloud | Google Cloud Platform |
| Data Lake | Google Cloud Storage |
| Processing | Dataproc (PySpark) |
| Warehouse | BigQuery |
| Orchestration | Cloud Composer (Airflow - Planned) |
| Language | Python |
| Infrastructure | Terraform (Planned) |
| CI/CD | Jenkins + Harness (Planned) |
| Reporting | Looker Studio |

---

# Source Dataset

Dataset: **Brazilian E-Commerce Public Dataset by Olist**

Kaggle:
https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

Entities

- Customers
- Orders
- Order Items
- Order Payments
- Order Reviews
- Products
- Sellers
- Geolocation
- Product Category Translation

## Entity Relationship Diagram

The following diagram illustrates the relationships between the source datasets.

<p align="center">
    <img src="docs/images/olist-dataset-schema.png" width="900">
</p>

Local dataset location:

```text
data/sample/kaggle/olist/
```

---

# Google Cloud Foundation

| Property | Value |
|----------|-------|
| Project | gcp-alshaya-medallion |
| Region | asia-south1 |
| Storage Bucket | gcp-alshaya-medallion-data |

Authentication uses Application Default Credentials (ADC).

---

# Repository Structure

```text
gcp-alshaya-medallion/
├── config/
│   ├── datasets/
│   └── gcp_config.yaml
├── data/
├── docs/
│   └── images/
├── logs/
├── scripts/
├── src/
│   └── retail_platform/
│       ├── common/
│       ├── cloud/
│       ├── ingestion/
│       ├── bronze/
│       ├── silver/
│       └── gold/
├── tests/
├── requirements.txt
├── pyproject.toml
└── README.md
```

---

# Configuration

## Main Configuration

```text
config/gcp_config.yaml
```

Contains:

- Project
- Region
- Bucket
- Local dataset path
- Upload retry configuration

## Dataset Metadata

```text
config/datasets/
```

Each dataset has an individual YAML file describing:

- Dataset name
- Source file
- Target file
- Target path
- Load type
- Primary key
- Watermark column

---

# Current Implementation

## Sprint 0 - Foundation

- Repository setup
- Python package structure
- Configuration framework
- Centralized logging
- File validation
- Google Cloud SDK setup
- Application Default Credentials
- Storage bucket creation
- Data Lake initialization

## Sprint 1 - Raw Data Ingestion

- Dataset Registry
- Metadata-driven ingestion
- GCS uploader
- Upload retry mechanism
- Upload orchestrator
- Raw data upload

---

# Data Lake Structure

```text
gs://gcp-alshaya-medallion-data/

raw/
bronze/
silver/
gold/
archive/
logs/
```

Current Raw layout:

```text
raw/
└── olist/
    ├── customers/
    ├── orders/
    ├── order_items/
    ├── order_payments/
    ├── order_reviews/
    ├── products/
    ├── sellers/
    ├── geolocation/
    └── category_translation/
```

---

# Implemented Components

| Component | Purpose | Status |
|-----------|---------|--------|
| Configuration Manager | Central configuration | ✅ |
| Logger | Standard logging | ✅ |
| File Validator | Validate source files | ✅ |
| Storage Initializer | Initialize data lake folders | ✅ |
| Dataset Registry | Load dataset metadata | ✅ |
| GCS Uploader | Upload with retry | ✅ |
| Upload Orchestrator | Upload all configured datasets | ✅ |

---

# Getting Started

## Install

```bash
pip install -r requirements.txt
pip install -e .
```

## Authenticate

```bash
gcloud auth login
gcloud auth application-default login
```

## Provision Foundation

```powershell
./scripts/01-gcp-foundation.ps1
```

## Verify Configuration

```bash
python -m retail_platform.common.test_config
```

## Verify Storage

```bash
python -m retail_platform.cloud.storage.test_storage_initializer
```

## Test GCS Upload

```bash
python -m retail_platform.cloud.storage.test_gcs_uploader
```

## Upload Raw Datasets

```bash
python -m retail_platform.ingestion.upload_to_gcs
```

---

# Roadmap

| Sprint | Deliverable | Status |
|--------|-------------|--------|
| Sprint 0 | Foundation | ✅ |
| Sprint 1 | Raw Data Ingestion | ✅ |
| Sprint 2 | Bronze Layer | ⬜ |
| Sprint 3 | Silver Layer | ⬜ |
| Sprint 4 | Gold Layer | ⬜ |
| Sprint 5 | BigQuery | ⬜ |
| Sprint 6 | Airflow | ⬜ |
| Sprint 7 | Terraform | ⬜ |
| Sprint 8 | CI/CD | ⬜ |

---

# Documentation

```text
docs/
├── architecture.md
├── data-lake.md
├── ingestion-framework.md
└── project-progress.md
```

---

# Future Enhancements

- Incremental ingestion
- Watermark processing
- Deduplication
- Schema validation
- Audit framework
- Data quality checks
- Airflow orchestration
- Terraform provisioning
- CI/CD automation

---

# License

This repository is intended for learning and portfolio purposes.
