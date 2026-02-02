from pathlib import Path
import pandas as pd

subdirs = "year=2026"
base_dir = Path(__file__).parent.parent.parent
raw_dir = base_dir / 'data' / 'raw' / 'sessions' / subdirs
bronze_dir = base_dir / 'data' / 'bronze' / 'sessions' / subdirs
raw_dir = raw_dir.rglob('*sessions.json')

bronze_dir.mkdir(parents=True, exist_ok=True)

df1 = pd.DataFrame()
for file in raw_dir:
        df2 = pd.read_json(file)
        run_id = file.parent.name
        df2['run_id'] = run_id[7:]
        df1 = pd.concat([df1, df2])

df1.to_parquet(bronze_dir / 'sessions.parquet', index=False)



