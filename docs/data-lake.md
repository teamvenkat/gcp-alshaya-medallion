# Data Lake Design

## Storage Strategy

A single Google Cloud Storage bucket is used as the enterprise data lake.

Logical folders:

- raw
- bronze
- silver
- gold
- archive
- logs

## Current Raw Layout

Each dataset is stored independently.

Example:

raw/
└── olist/
    ├── customers/
    ├── orders/
    ├── products/
    └── ...

This structure prepares the platform for future partitioned and incremental ingestion.
