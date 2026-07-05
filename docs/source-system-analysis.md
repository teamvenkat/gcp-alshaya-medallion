# Source System Analysis

## Overview

This document provides an overview of the source system used in this project.

The project uses the **Brazilian E-Commerce Public Dataset by Olist**, which simulates a real-world retail e-commerce platform consisting of multiple related entities.

Understanding the source system is essential before designing the Medallion Architecture.

---

# Source Dataset

Source

- Kaggle
- Brazilian E-Commerce Public Dataset by Olist

Number of Source Tables

| Dataset | Description |
|----------|-------------|
| Customers | Customer master data |
| Orders | Order header information |
| Order Items | Order line items |
| Products | Product master |
| Sellers | Seller master |
| Order Payments | Payment details |
| Order Reviews | Customer reviews |
| Geolocation | Customer/Seller postal code information |
| Product Category Translation | Portuguese to English product category mapping |

---

# Source System ER Diagram

![Olist Dataset](images/olist-dataset-schema.png)

---

# Dataset Analysis

| Dataset | Business Purpose | Primary Key | Foreign Keys | Classification |
|----------|------------------|-------------|--------------|----------------|
| Customers | Stores customer information | customer_id | — | Master Data |
| Orders | Stores customer orders | order_id | customer_id | Transaction |
| Order Items | Stores products purchased within an order | order_id + order_item_id | product_id, seller_id | Transaction |
| Products | Product catalog | product_id | — | Master Data |
| Sellers | Seller information | seller_id | — | Master Data |
| Order Payments | Payment information | order_id + payment_sequential | order_id | Transaction |
| Order Reviews | Customer feedback | review_id | order_id | Transaction |
| Geolocation | Postal code lookup | geolocation_zip_code_prefix | — | Reference |
| Product Category Translation | Category lookup | product_category_name | — | Reference |

---

# Dataset Relationships

The dataset follows a typical retail transactional model.

```
Customer
    │
    ▼
 Orders
    │
    ▼
Order Items
    │
 ┌──┴──────┐
 ▼         ▼
Product   Seller

Orders
   │
   ├────────► Payments
   │
   └────────► Reviews
```

---

# Medallion Mapping

## Bronze Layer

The Bronze layer stores raw copies of every source dataset.

| Source Dataset | Bronze Table |
|----------------|--------------|
| Customers | bronze_customers |
| Orders | bronze_orders |
| Order Items | bronze_order_items |
| Products | bronze_products |
| Sellers | bronze_sellers |
| Payments | bronze_order_payments |
| Reviews | bronze_order_reviews |
| Geolocation | bronze_geolocation |
| Category Translation | bronze_category_translation |

---

## Silver Layer

The Silver layer contains cleaned and standardized datasets.

| Bronze | Silver |
|----------|---------|
| bronze_customers | silver_customers |
| bronze_orders | silver_orders |
| bronze_order_items | silver_order_items |
| bronze_products | silver_products |
| bronze_sellers | silver_sellers |
| bronze_order_payments | silver_order_payments |
| bronze_order_reviews | silver_order_reviews |
| bronze_geolocation | silver_geolocation |
| bronze_category_translation | silver_category_translation |

Typical transformations include:

- Remove duplicates
- Handle null values
- Standardize data types
- Validate business keys
- Apply naming standards

---

## Gold Layer

The Gold layer contains business-ready analytical datasets.

| Gold Dataset | Description |
|--------------|-------------|
| fact_sales | Sales fact table |
| dim_customer | Customer dimension |
| dim_product | Product dimension |
| dim_seller | Seller dimension |
| dim_date | Date dimension |
| fact_payments | Payment analytics |
| fact_reviews | Customer review analytics |

---

# Target Architecture

```
                Kaggle Dataset
                      │
                      ▼
               Google Cloud Storage
                      │
          raw/olist/*.csv
                      │
                      ▼
            Bronze (Raw PySpark)
                      │
                      ▼
          Silver (Clean PySpark)
                      │
                      ▼
         Gold (Business Models)
                      │
                      ▼
                BigQuery
                      │
                      ▼
              Looker Studio
```

