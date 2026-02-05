# OpenF1 Data Engineering Pipeline

End-to-end Data Engineering project built on top of the OpenF1 API.  
The goal of this project is to demonstrate how to design and implement a modern, layered data pipeline (RAW → Bronze → Silver → Gold) with production-oriented patterns such as metadata tracking, idempotent ingestion, deduplication and analytical modeling.

---

## Project overview

This pipeline ingests motorsport data from the OpenF1 public API, processes it through multiple data layers, and produces a clean analytical dataset (Gold layer) that can be directly used for reporting or further analytics.

Key focuses of the project:
- clear separation of data layers
- reproducible ingestion with metadata
- deterministic deduplication logic
- explicit data modeling decisions
- readable, interview-ready codebase

---

## Architecture

**Layers:**
- **RAW** – immutable JSON files exactly as received from the API, stored per run with metadata
- **Bronze** – unified Parquet snapshots enriched with `run_id`
- **Silver** – cleaned and deduplicated datasets using business keys and latest `run_id`
- **Gold** – analytical marts built from Silver data

## Data sources

OpenF1 API endpoints:
- `meetings`
- `sessions`
- `drivers`

> The `data/` directory is local-only and gitignored.

---

## How to run the pipeline (local)

### 1. Ingestion (RAW)

python ingestion/src/fetch_meetings.py
python ingestion/src/fetch_sessions.py
python ingestion/src/fetch_drivers.py

### 2. Bronze Layer

python bronze/src/meetings_to_parquet.py
python bronze/src/sessions_to_parquet.py
python bronze/src/drivers_to_parquet.py

### 3. Silver Layer

python silver/src/meetings_clean.py
python silver/src/sessions_clean.py
python silver/src/drivers_clean.py

### 4. Gold Layer

python gold/src/build_mart_schedule.py