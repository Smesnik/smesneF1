import pandas as pd
from pathlib import Path

base_dir = Path(__file__).parent.parent.parent
bronze_dir = base_dir / 'data' / 'bronze' / 'meetings'
silver_dir = base_dir / 'data' / 'silver' / 'meetings'

silver_dir.mkdir(parents=True, exist_ok=True)


raw_silver = pd.read_parquet(bronze_dir / 'meetings.parquet').sort_values(by='run_id')


df_silver = raw_silver.drop_duplicates(subset='meeting_key', keep='last')

df_silver.to_parquet(silver_dir / 'meetings.parquet', index=False)
