#%%
import pandas as pd

# Load the dataset
file_path = "../data/processed/haaland_match_logs_final.csv"  # Replace with your actual file path
df = pd.read_csv(file_path)

# Display the first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Columns related to Match Information
match_info_columns = ['Unnamed: 0', 'Date', 'Day', 'Comp', 'Round', 'Venue', 'Squad', 'Opponent', 'Time', 'Result_y',
                      'GF', 'GA', 'Game_xG', 'xGA', 'Poss', 'Captain', 'Formation', 'Opp Formation']

# Columns related to Player Statistics
player_stats_columns = ['Unnamed: 0', 'Date', 'Squad', 'Opponent', 'Min', 'Gls', 'Ast', 'PK', 'PKatt', 'Sh', 'SoT',
                       'CrdY', 'CrdR', 'Touches', 'Tkl', 'Int', 'Blocks', 'Player_xG', 'npxG', 'xAG', 'SCA', 'GCA',
                       'PassCmp', 'PassAttm', 'PassCmp%', 'PrgPass', 'Carries', 'PrgCarries', 'TakeonsAtt', 'TakeonsSucc']

# Split into Match Information and Player Statistics
match_info_df = df[match_info_columns]
player_stats_df = df[player_stats_columns]

# Adding a unique match_id to Match Information
match_info_df['match_id'] = range(1, len(match_info_df) + 1)

# Merge match_id with player_stats_df
player_stats_df = player_stats_df.merge(match_info_df[['match_id', 'Date']], on='Date', how='left')

# Save to CSV
match_info_df.to_csv("../data/normalized_data/match_information_with_id.csv", index=False)
player_stats_df.to_csv("../data/normalized_data/player_statistics_with_match_id.csv", index=False)

print("\nCSV files saved successfully.")

#%%
import pandas as pd

# Load the datasets
shots_df = pd.read_csv("../data/processed/haaland_shots_cleaned_2023_2024.csv")
matches_df = pd.read_csv("../data/normalized_data/match_information_with_id.csv")


# Merge the match_id from matches_df into shots_df based on the Date column
merged_df = pd.merge(shots_df, matches_df[['Date', 'match_id']], on='Date', how='left')

# Save the updated dataframe to a new CSV
merged_df.to_csv("../data/normalized_data/haaland_shots_with_match_id.csv", index=False)

print("Match ID successfully added to haaland_shots_cleaned_2023_2024.csv!")

#%%
import pandas as pd

# Load the datasets
haaland_assists = pd.read_csv('../data/processed/haaland_goals_cleaned.csv')  # Replace with the actual path to your file
match_info = pd.read_csv('../data/normalized_data/match_information_with_id.csv')  # Replace with the actual path to your file

# Ensure the Date and Opponent columns are consistent for merging
haaland_assists['Date'] = pd.to_datetime(haaland_assists['Date'])
match_info['Date'] = pd.to_datetime(match_info['Date'])

# Merge the datasets on Date and Opponent to add match_id
haaland_goals_with_match_id = haaland_assists.merge(
    match_info[['Date', 'Opponent', 'match_id']],
    on=['Date', 'Opponent'],
    how='left'
)

# Save the updated dataset
haaland_goals_with_match_id.to_csv('../data/normalized_data/haaland_goals_with_match_id.csv', index=False)

print("Match IDs added successfully! The updated dataset is saved as 'haaland_goals_with_match_id.csv'.")

#%%
import pandas as pd

# Load the datasets
haaland_assists = pd.read_csv('../data/processed/haaland_assists_cleaned.csv')  # Replace with the actual path to your file
match_info = pd.read_csv('../data/normalized_data/match_information_with_id.csv')  # Replace with the actual path to your file

# Ensure the Date and Opponent columns are consistent for merging
haaland_assists['Date'] = pd.to_datetime(haaland_assists['Date'])
match_info['Date'] = pd.to_datetime(match_info['Date'])

# Merge the datasets on Date and Opponent to add match_id
haaland_goals_with_match_id = haaland_assists.merge(
    match_info[['Date', 'Opponent', 'match_id']],
    on=['Date', 'Opponent'],
    how='left'
)

# Save the updated dataset
haaland_goals_with_match_id.to_csv('../data/normalized_data/haaland_assists_with_match_id.csv', index=False)

print("Match IDs added successfully! The updated dataset is saved as 'haaland_goals_with_match_id.csv'.")

#%%
import pandas as pd

# Load the datasets
fixtures = pd.read_csv('../data/processed/man_city_cleaned_fixtures.csv')  # Replace with the correct file path
match_info = pd.read_csv('../data/normalized_data/match_information_with_id.csv')  # Replace with the correct file path

# Ensure consistent date format (if Date exists in both datasets)
fixtures['Date'] = pd.to_datetime(fixtures['Date'])
match_info['Date'] = pd.to_datetime(match_info['Date'])

# Merge datasets on common fields (e.g., Date and Opponent)
merged_data = pd.merge(
    fixtures,
    match_info[['Date', 'Opponent', 'match_id']],  # Select relevant columns from match_info
    on=['Date', 'Opponent'],  # Merge on Date and Opponent
    how='left'  # Use 'left' to keep all rows in the fixtures dataset
)

# Save the merged data
merged_data.to_csv('../data/normalized_data/man_city_fixtures_with_match_id.csv', index=False)

print("Match IDs integrated successfully! Saved as 'man_City_fixtures_with_match_id.csv'.")

#%%
