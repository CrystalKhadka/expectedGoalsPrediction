import pandas as pd
import sqlite3
from sqlalchemy import create_engine, types


def create_sqlite_db():
    # Create SQLite database connection
    engine = create_engine('sqlite:///manchester_city.db')

    # Dictionary to store data type mappings for each table
    dtype_mappings = {
        'haaland_assists': {
            'Date': types.String,
            'Opponent': types.String,
            'Comp': types.String,
            'Venue': types.String,
            'Result': types.String,
            'GF': types.Integer,
            'GA': types.Integer,
            'Minute': types.Integer,
            'Scorer': types.String,
            'Body Part': types.String,
            'AssistContributionAction': types.String,
            'ActionType': types.String,
            'Goalkeeper': types.String,
            'match_id': types.Integer
        },
        'haaland_goals': {
            'Date': types.String,
            'Opponent': types.String,
            'Comp': types.String,
            'Venue': types.String,
            'Result': types.String,
            'GF': types.Integer,
            'GA': types.Integer,
            'Goal_xG': types.Float,
            'Match_xG': types.Float,
            'Minute': types.String,
            'Body Part': types.String,
            'Assist': types.String,
            'GoalContributionAction': types.String,
            'ActionType': types.String,
            'Goalkeeper': types.String,
            'match_id': types.Integer
        },
        'haaland_shots': {
            'minute': types.Integer,
            'result': types.String,
            'X': types.Float,
            'Y': types.Float,
            'xG': types.Float,
            'player': types.String,
            'situation': types.String,
            'season': types.Integer,
            'shotType': types.String,
            'Date': types.String,
            'player_assisted': types.String,
            'lastAction': types.String,
            'time': types.String,
            'squad': types.String,
            'opponent': types.String,
            'venue': types.String,
            'GF': types.Integer,
            'GA': types.Integer,
            'match_id': types.Integer
        },
        'man_city_fixtures': {
            'Date': types.String,
            'Time': types.String,
            'Comp': types.String,
            'Round': types.String,
            'Day': types.String,
            'Venue': types.String,
            'Result': types.String,
            'GF': types.Integer,
            'GA': types.Integer,
            'Opponent': types.String,
            'xG': types.Float,
            'xGA': types.Float,
            'Poss': types.Integer,
            'Captain': types.String,
            'Formation': types.String,
            'Opp Formation': types.String,
            'match_id': types.Integer
        },
        'man_city_shots_normalized': {
            'Date': types.String,
            'Time': types.String,
            'Comp': types.String,
            'Round': types.String,
            'Day': types.String,
            'Venue': types.String,
            'Result': types.String,
            'Goals For': types.Integer,
            'Goals Against': types.Integer,
            'Opponent': types.String,
            'Goals': types.Float,
            'Shots': types.Float,
            'Shots on Target': types.Float,
            'SoT%': types.Float,
            'Goals per Shot': types.Float,
            'Goals per SoT': types.Float,
            'Shot Distance': types.Float,
            'Free Kicks': types.Float,
            'Penalty Goals': types.Float,
            'Penalty Attempts': types.Float,
            'Expected Goals': types.Float,
            'Non-Penalty xG': types.Float,
            'NP xG per Shot': types.Float,
            'G-xG': types.Float,
            'NP:G-xG': types.Float,
            'Match ID': types.Integer
        },
        'match_information': {
            'Unnamed: 0': types.Integer,
            'Date': types.String,
            'Day': types.String,
            'Comp': types.String,
            'Round': types.String,
            'Venue': types.String,
            'Squad': types.String,
            'Opponent': types.String,
            'Time': types.String,
            'Result_y': types.String,
            'GF': types.Integer,
            'GA': types.Integer,
            'Game_xG': types.Float,
            'xGA': types.Float,
            'Poss': types.Integer,
            'Captain': types.String,
            'Formation': types.String,
            'Opp Formation': types.String,
            'match_id': types.Integer
        },
        'player_statistics': {
            'Unnamed: 0': types.Integer,
            'Date': types.String,
            'Squad': types.String,
            'Opponent': types.String,
            'Min': types.Integer,
            'Gls': types.Integer,
            'Ast': types.Integer,
            'PK': types.Integer,
            'PKatt': types.Integer,
            'Sh': types.Integer,
            'SoT': types.Integer,
            'CrdY': types.Integer,
            'CrdR': types.Integer,
            'Touches': types.Integer,
            'Tkl': types.Integer,
            'Int': types.Integer,
            'Blocks': types.Integer,
            'Player_xG': types.Float,
            'npxG': types.Float,
            'xAG': types.Float,
            'SCA': types.Integer,
            'GCA': types.Integer,
            'PassCmp': types.Integer,
            'PassAttm': types.Integer,
            'PassCmp%': types.Float,
            'PrgPass': types.Integer,
            'Carries': types.Integer,
            'PrgCarries': types.Integer,
            'TakeonsAtt': types.Integer,
            'TakeonsSucc': types.Integer,
            'match_id': types.Integer
        }
    }

    # CSV files to process
    csv_files = {
        'haaland_assists': 'haaland_assists_with_match_id.csv',
        'haaland_goals': 'haaland_goals_with_match_id.csv',
        'haaland_shots': 'haaland_shots_with_match_id.csv',
        'man_city_fixtures': 'man_city_fixtures_with_match_id.csv',
        'man_city_shots_normalized': 'man_city_shots_normalized_with_match_id.csv',
        'match_information': 'match_information_with_id.csv',
        'player_statistics': 'player_statistics_with_match_id.csv'
    }

    try:
        # Process each CSV file
        for table_name, file_name in csv_files.items():
            print(f"Processing {file_name}...")

            # Read CSV file
            df = pd.read_csv(file_name)

            # Write to SQLite database
            df.to_sql(
                table_name,
                engine,
                if_exists='replace',
                index=False,
                dtype=dtype_mappings[table_name]
            )

            print(f"Successfully imported {file_name} to table {table_name}")

        print("\nDatabase creation completed successfully!")

        # Verify the tables
        with engine.connect() as conn:
            for table_name in csv_files.keys():
                result = conn.execute(f"SELECT COUNT(*) FROM {table_name}")
                count = result.scalar()
                print(f"Table {table_name} contains {count} rows")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    create_sqlite_db()