import requests
from pathlib import Path
import datetime
import json

base_dir = Path(__file__).parent.parent.parent
raw_meetings = "data/raw/meetings"
input_dir = base_dir / raw_meetings


input_dir.mkdir(parents=True, exist_ok=True)

current_date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

test_file = input_dir / f"ingestion_date={current_date}.json"

base_url = 'https://api.openf1.org/v1/'
endpoint = 'meetings'

response = requests.get(base_url+endpoint, timeout=20)

if response.status_code == 200:
    with open(test_file,'w', encoding='utf-8') as file:
        json.dump(response.json(), file, indent=2)
else:
    print(f'Error code: {response.status_code}')

print(response.json())


