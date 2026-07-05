# Architecture

## Overview

The platform follows the Medallion Architecture.

Local Dataset
    ↓
Google Cloud Storage (Raw)
    ↓
Bronze (Standardized)
    ↓
Silver (Curated)
    ↓
Gold (Analytics)
    ↓
BigQuery
    ↓
Looker Studio

## Design Principles

- Metadata-driven ingestion
- Configuration over hardcoding
- Reusable components
- Separation of responsibilities
- Layered data architecture

## Current Status

Foundation and Raw ingestion are complete.
Bronze development is the next milestone.
