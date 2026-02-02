import pandas as pd
from pathlib import Path

base_dir = Path(__file__).parent.parent.parent
bronze_dir = base_dir / 'data' / 'bronze' / 'sessions' / 'year=2026'
silver_dir = base_dir / 'data' / 'silver' / 'sessions' / 'year=2026'

silver_dir.mkdir(parents=True, exist_ok=True)

raw_silver = pd.read_parquet(bronze_dir / 'sessions.parquet').sort_values(by='date_start')
df_silver = raw_silver.drop_duplicates(subset='session_key')

df_silver.to_parquet(silver_dir / 'sessions.parquet', index=False)

