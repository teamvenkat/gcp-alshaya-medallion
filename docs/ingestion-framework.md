# Ingestion Framework

## Current Components

1. Configuration Manager
2. File Validator
3. Storage Initializer
4. Dataset Registry
5. GCS Uploader
6. Upload Orchestrator

## Upload Flow

Dataset Metadata (YAML)
        ↓
Dataset Registry
        ↓
File Validation
        ↓
GCS Uploader
        ↓
Raw Layer

## Features

- Metadata-driven
- Retry mechanism
- Centralized logging
- Configuration-driven
