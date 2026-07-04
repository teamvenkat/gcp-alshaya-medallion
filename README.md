# GCP Alshaya Medallion

Enterprise-grade Retail Data Platform built on **Google Cloud Platform (GCP)** using the **Medallion Architecture (Bronze → Silver → Gold)**.

> **Current Status:** 🚧 In Development

---

## Project Objective

This project demonstrates the implementation of an end-to-end retail data platform using Google Cloud Platform and the Medallion Architecture.

The objective is to build a scalable data engineering solution that ingests raw retail data, transforms it through Bronze, Silver, and Gold layers, and exposes business-ready datasets for analytics.

---

## Technology Stack

| Category        | Technology                      |
| --------------- | ------------------------------- |
| Cloud           | Google Cloud Platform (GCP)     |
| Storage         | Google Cloud Storage            |
| Processing      | Dataproc (PySpark)              |
| Data Warehouse  | BigQuery                        |
| Orchestration   | Cloud Composer (Apache Airflow) |
| Reporting       | Looker Studio                   |
| Language        | Python                          |
| Version Control | Git & GitHub                    |

---

## Repository Structure

```text
gcp-alshaya-medallion/
│
├── airflow/
├── config/
├── data/
│   ├── sample/
│   └── schemas/
├── docs/
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
├── LICENSE
├── requirements.txt
└── bootstrap.py
```

---

## Development Roadmap

* [x] Repository Setup
* [ ] Retail Dataset Selection
* [ ] GCS Data Ingestion
* [ ] Bronze Layer
* [ ] Silver Layer
* [ ] Gold Layer
* [ ] BigQuery Integration
* [ ] Airflow Orchestration
* [ ] Looker Studio Dashboard

---

## Architecture

```text
Retail Dataset
       │
       ▼
Google Cloud Storage
       │
       ▼
Bronze Layer
       │
       ▼
Silver Layer
       │
       ▼
Gold Layer
       │
       ▼
BigQuery
       │
       ▼
Looker Studio
```

---

## Current Focus

The current phase focuses on delivering a working Medallion Architecture before introducing advanced engineering practices such as Infrastructure as Code, CI/CD, monitoring, and automated testing.

These capabilities will be added incrementally after the core data platform is complete.
