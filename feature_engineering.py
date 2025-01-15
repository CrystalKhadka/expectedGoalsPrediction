# Feature Engineering for Combined Football Data
import pandas as pd
from sqlalchemy import create_engine

# Connect to PostgreSQL
def connect_to_db(username, password, database_name, host, port):
    connection_url = f'postgresql://{username}:{password}@{host}:{port}/{database_name}'
    return create_engine(connection_url)

# Load data from PostgreSQL
def load_data(engine, query):
    return pd.read_sql(query, engine)

# Add new features to the data
def add_features(data):
    # Match-Level Features
    data['goals_per_match'] = data['GF'] / data['match_id'].nunique()
    data['shots_per_match'] = data['Shots'] / data['match_id'].nunique()
    data['goals_per_shot'] = data['Goals'] / data['Shots']
    data['soT_percentage'] = (data['Shots on Target'] / data['Shots']) * 100
    data['expected_goals'] = data['Expected Goals'] / data['match_id'].nunique()
    data['npxg'] = data['Non-Penalty xG'] / data['match_id'].nunique()

    # Haaland-Specific Features
    haaland_data = data[data['player'] == 'Erling Haaland']
    data['haaland_goals_per_game'] = haaland_data.groupby('match_id')['Goals'].transform('sum') / data['match_id'].nunique()
    data['haaland_shots_per_game'] = haaland_data.groupby('match_id')['Shots'].transform('sum') / data['match_id'].nunique()
    data['haaland_xg_per_game'] = haaland_data.groupby('match_id')['Expected Goals'].transform('sum') / data['match_id'].nunique()
    data['haaland_sot_percentage'] = haaland_data.groupby('match_id')['Shots on Target'].transform('sum') / haaland_data.groupby('match_id')['Shots'].transform('sum') * 100

    # Match Context Features
    data['is_home'] = data['Venue'].apply(lambda x: 1 if x == 'Home' else 0)
    data['match_result'] = data['Result'].apply(lambda x: 1 if x == 'W' else 0)
    data['possession_diff'] = data['Poss'] - (100 - data['Poss'])

    # Advanced Features
    data['avg_shot_distance'] = data['Shot Distance'] / data['Shots']
    data['touches_in_box'] = data['Touches']
    data['crosses_completed'] = data['PassCmp']
    data['pass_completion_rate'] = data['PassCmp'] / data['PassAttm'] * 100
    data['takeons_success_rate'] = data['TakeonsSucc'] / data['TakeonsAtt'] * 100

    # Rolling Averages
    data['rolling_xG_last_3'] = data['Expected Goals'].rolling(3).mean()
    data['avg_goals_last_3'] = data['Goals'].rolling(3).mean()

    # Interaction Features
    data['attack_efficiency'] = data['goals_per_match'] * data['Poss']
    data['defense_to_attack_ratio'] = (data['Tkl'] + data['Int']) / data['Shots']

    # Additional Metrics
    data['penalty_conversion_rate'] = data['Penalty Goals'] / data['Penalty Attempts'].replace(0, pd.NA).fillna(1)
    data['defensive_actions'] = data['Tkl'] + data['Int'] + data['Blocks']
    data['progressive_actions'] = data['PrgPass'] + data['PrgCarries']
    data['goal_contribution'] = data['Goals'] + data['Ast']
    data['average_pass_length'] = data['PassCmp'] / data['Touches'].replace(0, pd.NA).fillna(1)
    data['duel_success_rate'] = data['TakeonsSucc'] / data['TakeonsAtt'].replace(0, pd.NA).fillna(1) * 100

    # Match Impact Features
    data['impact_goals'] = data.apply(lambda x: 1 if x['minute'] > 75 and x['Goals'] > 0 else 0, axis=1)
    data['early_goals'] = data.apply(lambda x: 1 if x['minute'] < 15 and x['Goals'] > 0 else 0, axis=1)

    # Team and Opponent Analysis
    data['team_pass_ratio'] = data['PassCmp'] / (data['PassAttm'])


    # Per-Game Metrics
    data['passes_per_game'] = data['PassCmp'] / data['match_id'].nunique()
    data['defensive_work_rate'] = data['Tkl'] / data['match_id'].nunique()

    # Tactical Features
    data['formation_width'] = data['Formation'].apply(lambda x: int(x.split('-')[0]))
    data['opponent_formation_width'] = data['Opp Formation'].apply(lambda x: int(x.split('-')[0]))

    # Positional Analysis
    data['average_position_x'] = data['X'] / data['Touches']
    data['average_position_y'] = data['Y'] / data['Touches']

    # Scoring Trends
    data['goals_after_75'] = data.apply(lambda x: 1 if x['minute'] > 75 else 0, axis=1)
    data['goals_before_15'] = data.apply(lambda x: 1 if x['minute'] < 15 else 0, axis=1)

    return data

# Main workflow
if __name__ == "__main__":
    # Database credentials
    username = 'postgres'
    password = ''
    database_name = 'football'
    host = 'localhost'
    port = '5432'

    # Connection setup
    engine = connect_to_db(username, password, database_name, host, port)

    # Load combined data
    query = "SELECT * FROM combined_data"
    combined_data = load_data(engine, query)

    # Check for missing values
    numeric_columns = combined_data.select_dtypes(include=['float64', 'int64']).columns
    combined_data[numeric_columns] = combined_data[numeric_columns].fillna(0)
    string_columns = combined_data.select_dtypes(include=['object']).columns
    combined_data[string_columns] = combined_data[string_columns].fillna('None')

    # Add features
    combined_data = add_features(combined_data)

    # Save the feature-engineered data back to PostgreSQL
    try:
        combined_data.to_sql('combined_data_features', engine, if_exists='replace', index=False)
        print("Feature engineering complete and data saved to database!")
    except Exception as e:
        print(f"Error saving feature-engineered data: {e}")
