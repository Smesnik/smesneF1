Data insights:
meetings:
PK: meeting_key
Time fields: date_start
Business fields: meeting_name, year
Partition candidate: year

sessions:
PK: session_key
Time fields: date_start, date_end
Business fields: session_name, session_type, year, meeting_key
Partition candidate: year

drivers:
PK: driver_number
Time fields: none
Business fields: first_name, last_name, team_name
Partition candidate: none (dimension table)

1. Source: Open FI API, data: meetings, sessions, drivers
2. Ingestion: raw files from API as json saved locally
3. Storage: locally (TBA: datalake in Azure)
4. Layers: Bronze(raw/landing), Silver(cleaned,typed,dedup), Gold(analytical models dbt)
5. Orchestration: manually and locally (TBA: Airflow/ADF)
6. Partitioning: meetings: year, sessions:year, drivers:none