import pandas as pd
from pathlib import Path

base_dir = Path(__file__).parent.parent.parent
bronze_dir = base_dir / 'data' / 'bronze' / 'drivers'
silver_dir = base_dir / 'data' / 'silver' / 'drivers'

silver_dir.mkdir(parents=True, exist_ok=True)


raw_silver = pd.read_parquet(bronze_dir / 'drivers.parquet').sort_values(by='run_id')


df_silver = raw_silver.drop_duplicates(subset='driver_number', keep='last')

df_silver.to_parquet(silver_dir / 'drivers.parquet', index=False)
