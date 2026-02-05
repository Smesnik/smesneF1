flowchart LR

    A[OpenF1 API] --> B[Python Ingestion]

    B --> C[RAW Layer<br/>JSON + metadata<br/>run_id, ingestion_date]

    C --> D[Bronze Layer<br/>Parquet<br/>run-aware]

    D --> E[Silver Layer<br/>Cleaned & Deduplicated<br/>latest run_id]

    E --> F[Gold Layer<br/>mart_schedule<br/>Session-level grain]

    subgraph Source
        A
    end

    subgraph Ingestion
        B
    end

    subgraph RAW
        C
    end

    subgraph Bronze
        D
    end

    subgraph Silver
        E
    end

    subgraph Gold
        F
    end
