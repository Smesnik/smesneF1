import pandas as pd
from pathlib import Path

base_dir = Path(__file__).parent.parent.parent
silver_dir = base_dir / 'data' / 'silver'
gold_dir = base_dir / 'data' / 'gold' / 'mart_schedule' / 'year=2026'
gold_dir.mkdir(parents=True,exist_ok=True)
meet_dir = silver_dir / 'meetings'
sess_dir = silver_dir / 'sessions' / 'year=2026'


meet_df = pd.read_parquet(meet_dir / 'meetings.parquet')
sess_df = pd.read_parquet(sess_dir / 'sessions.parquet')

mart_df = pd.merge(sess_df,meet_df, on='meeting_key', how='inner')
mart_df.rename(columns={'date_start_x': 'date_start', 'date_end_x': 'date_end', 'location_y': 'location', 'country_name_y': 'country_name', 'year_y': 'year'}, inplace=True)
mart_df = mart_df[['session_key','session_name','session_type', 'date_start','date_end','meeting_key','meeting_name','location','country_name','year']]

mart_df.to_parquet(gold_dir / 'mart_schedule.parquet', index=False)
