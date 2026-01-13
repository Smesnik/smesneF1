import requests
from pathlib import Path
import datetime
import json

base_dir = Path(__file__).parent.parent.parent
raw_meetings = "data/raw/meetings"
current_date = datetime.datetime.now().strftime("%Y-%m-%d")
run_date = datetime.datetime.now().strftime('%Y%m%dT%H%M%SZ')
input_dir = base_dir / raw_meetings / f"ingestion_date={current_date}" / f"run_id={run_date}"


input_dir.mkdir(parents=True, exist_ok=True)


input_name = input_dir / "meetings.json"
meta_name = input_dir / "_metadata.json"


base_url = 'https://api.openf1.org/v1/'
endpoint = 'meetings'

response = requests.get(base_url+endpoint, timeout=20)

if response.status_code == 200:

    retrieved_date = datetime.datetime.now().strftime('%Y%m%dT%H%M%SZ')

    _meta = {"source":"openF1",
             "endpoint":endpoint,
             "url":base_url+endpoint,
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
                   "record_count":len(response.json())}

    with open(meta_name, 'w') as file:
        json.dump(_meta_error, file, indent=2)

    print(f'Error code: {response.status_code}')




