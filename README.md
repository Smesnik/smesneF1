1) What it does: script is downloading data from OpenF1 api and saving it into raw/data as JSON. 
Each run has their own run ID so it can be verified what was downloaded when.
2) How to run: pip install -r requirements.txt, 
from cd ingestion please run either python src/fetch_meetings.py or python src/fetch_sessions.py
3) Output structure: meetings: data/raw/meetings/ingestion_date=.../run_id=.../meetings.json, 
sessions:data/raw/sessions/year=2026/ingestion_date=.../run_id=.../sessions.json
4) Metadata fields: if success -> source, endpoint, url, ingestion_date, run_id, retrieved_at, status_code, record_count
if failed -> error, record_count