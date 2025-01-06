import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL connection details
postgres_user = 'postgres'
postgres_password = ''
postgres_host = 'localhost'
postgres_port = '5432'
postgres_db = 'football'

# File paths for the CSV files
fixtures_csv_path = "man_city_fixtures_with_match_id.csv"
shots_csv_path = "man_city_shots_normalized_with_match_id.csv"
player_csv_path = "player_statistics_with_match_id.csv"
haaland_shots_path = "haaland_shots_with_match_id.csv"
haaland_goals_path = "haaland_goals_with_match_id.csv"
haaland_assists_path = "haaland_assists_with_match_id.csv"

# Read CSV files into DataFrames
fixtures_df = pd.read_csv(fixtures_csv_path)
shots_df = pd.read_csv(shots_csv_path)
player_stats_df = pd.read_csv(player_csv_path)
haaland_shots_df = pd.read_csv(haaland_shots_path)
haaland_goals_df = pd.read_csv(haaland_goals_path)
haaland_assists_df = pd.read_csv(haaland_assists_path)

# Create a PostgreSQL connection using SQLAlchemy
postgres_uri = f'postgresql://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_db}'
engine = create_engine(postgres_uri)

# Insert DataFrames into PostgreSQL tables
try:
    # Write data to respective tables (without defining column names explicitly)
    fixtures_df.to_sql('man_city_fixtures_with_match_id', engine, if_exists='replace', index=False)
    shots_df.to_sql('man_city_shots_normalized_with_match_id', engine, if_exists='replace', index=False)
    player_stats_df.to_sql('haaland_statistics', engine, if_exists='replace', index=False)
    haaland_shots_df.to_sql('haaland_shots', engine, if_exists='replace', index=False)
    haaland_goals_df.to_sql('haaland_goals', engine, if_exists='replace', index=False)
    haaland_assists_df.to_sql('haaland_assists', engine, if_exists='replace', index=False)

    print("Data successfully inserted into PostgreSQL")

except Exception as e:
    print("Error importing data:", e)

finally:
    engine.dispose()
