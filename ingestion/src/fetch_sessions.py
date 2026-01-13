import requests
from pathlib import Path
import datetime
import json


current_date = datetime.datetime.now().strftime("%Y-%m-%d")
run_date = datetime.datetime.now().strftime('%Y%m%dT%H%M%SZ')

base_url = 'https://api.openf1.org/v1/'
endpoint = 'sessions'
params = {"year":2026}

base_dir = Path(__file__).parent.parent.parent
raw_sessions = "data/raw/sessions"
input_dir = base_dir / raw_sessions / f"year={params['year']}" / f"ingestion_date={current_date}" / f"run_id={run_date}"
input_dir.mkdir(parents=True, exist_ok=True)
input_name = input_dir / "sessions.json"
meta_name = input_dir / "_metadata.json"





response = requests.get(base_url+endpoint, params=params, timeout=20)

if response.status_code == 200:

    retrieved_date = datetime.datetime.now().strftime('%Y%m%dT%H%M%SZ')

    _meta = {"source":"openF1",
             "endpoint":endpoint,
             "url":base_url+endpoint,
             "params":params,
             "ingestion_date":current_date,
             "run_id":run_date,
             "retrieved_at":retrieved_date,
             "status_code":response.status_code,
             "record_count":len(response.json())}

    with open(input_name,'w', encoding='utf-8') as file:
        json.dump(response.json(), file, indent=2)
    with open(meta_name, 'w') as file:
        json.dump(_meta,file, indent=2)
else:

    _meta_error = {"error":response.status_code,
                   "record_count":0}

    with open(meta_name, 'w') as file:
        json.dump(_meta_error, file, indent=2)

    print(f'Error code: {response.status_code}')




