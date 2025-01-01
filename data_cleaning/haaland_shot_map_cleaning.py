import pandas as pd
import os

# Define the path to the raw data CSV file
raw_data_path = '../data/raw/haaland_shot_map.csv'  # Adjust the path to your file location
output_file = '../data/cleaned/haaland_shots_cleaned_2023_2024.csv'  # Save cleaned data for the 2023-2024 season

# Load the raw data CSV file
df = pd.read_csv(raw_data_path)

# Convert the 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Filter for the 2023-2024 season (assuming the season starts in August 2023 and ends in May 2024)
start_date = '2023-08-01'
end_date = '2024-05-31'
df_filtered = df[(df['date'] >= start_date) & (df['date'] <= end_date)]

# 1. Filter data for Manchester City (home and away)
df_filtered = df_filtered[(df_filtered['h_team'] == 'Manchester City') | (df_filtered['a_team'] == 'Manchester City')]

# 2. Separate date and time
df_filtered['time'] = df_filtered['date'].dt.strftime('%H:%M:%S')
df_filtered['date'] = df_filtered['date'].dt.date

# 3. Drop unnecessary columns (you specified which columns to drop)
columns_to_drop = ['id', 'player_id', 'match_id']
df_cleaned = df_filtered.drop(columns=columns_to_drop)

# 4. Create a column for squad, opponent, and venue
df_cleaned['squad'] = df_cleaned['h_team'].where(df_cleaned['h_a'] == 'h', df_cleaned['a_team'])
df_cleaned['opponent'] = df_cleaned['a_team'].where(df_cleaned['h_a'] == 'h', df_cleaned['h_team'])
df_cleaned['venue'] = df_cleaned['h_a'].replace({'h': 'Home', 'a': 'Away'})

# 5. Update GF and GA based on whether it is a home or away match
df_cleaned['GF'] = df_cleaned['h_goals'].where(df_cleaned['h_a'] == 'h', df_cleaned['a_goals'])
df_cleaned['GA'] = df_cleaned['a_goals'].where(df_cleaned['h_a'] == 'h', df_cleaned['h_goals'])

# 6. Drop original goal columns (h_goals, a_goals)
df_cleaned = df_cleaned.drop(columns=['h_goals', 'a_goals'])

# 7. Drop original team columns (h_team, a_team)
df_cleaned = df_cleaned.drop(columns=['h_team', 'a_team', 'h_a'])

# Create the cleaned directory if it doesn't exist
os.makedirs(os.path.dirname(output_file), exist_ok=True)

# Save the cleaned data to a CSV file
df_cleaned.to_csv(output_file, index=False)

print(f"Cleaned 2023-2024 data saved successfully to {output_file}")

# Now the data is ready for visualization!
