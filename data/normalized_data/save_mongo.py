import pandas as pd
from pymongo import MongoClient

# MongoDB connection details
mongo_uri = "mongodb+srv://khadkacrystal:YaPsCKTOT2WFyH0f@football.56bma.mongodb.net/?retryWrites=true&w=majority&appName=Football"
database_name = "football"
fixtures_collection_name = "man_city_fixtures_with_match_id"
shots_collection_name = "man_city_shots_normalized_with_match_id"
haaland_collection_name="haaland_statistics"
haaland_shots_collection_name="haaland_shots"
haaland_goals_collection_name="haaland_goals"
haaland_assists_collection_name="haaland_assists"


# File paths for the CSV files
fixtures_csv_path = "man_city_fixtures_with_match_id.csv"
shots_csv_path = "man_city_shots_normalized_with_match_id.csv"
player_csv_path="player_statistics_with_match_id.csv"
haaland_shots_path="haaland_shots_with_match_id.csv"
haaland_goals_path="haaland_goals_with_match_id.csv"
haaland_assists_path="haaland_assists_with_match_id.csv"

# Read CSV files into DataFrames
fixtures_df = pd.read_csv(fixtures_csv_path)
shots_df = pd.read_csv(shots_csv_path)
player_stats_df=pd.read_csv(player_csv_path)
haaland_shots_df=pd.read_csv(haaland_shots_path)
haaland_goals_df=pd.read_csv(haaland_goals_path)
haaland_assists_df=pd.read_csv(haaland_assists_path)

# Convert DataFrames to dictionaries for MongoDB
fixtures_data = fixtures_df.to_dict(orient="records")
shots_data = shots_df.to_dict(orient="records")
player_stats_data=player_stats_df.to_dict(orient="records")
haaland_shots_data=haaland_shots_df.to_dict(orient="records")
haaland_goals_data=haaland_goals_df.to_dict(orient="records")
haaland_assists_data=haaland_assists_df.to_dict(orient="records")

# Connect to MongoDB
client = MongoClient(mongo_uri)
db = client[database_name]

try:
    # Insert data into respective collections
    fixtures_collection = db[fixtures_collection_name]
    shots_collection = db[shots_collection_name]
    player_stats_collection = db[haaland_collection_name]
    haaland_shots_collection = db[haaland_shots_collection_name]
    haaland_goals_collection = db[haaland_goals_collection_name]
    haaland_assists_collection = db[haaland_assists_collection_name]

    # Clear collections if they already exist
    fixtures_collection.delete_many({})
    shots_collection.delete_many({})
    player_stats_collection.delete_many({})
    haaland_goals_collection.delete_many({})
    haaland_assists_collection.delete_many({})
    haaland_shots_collection.delete_many({})

    # Insert documents
    fixtures_collection.insert_many(fixtures_data)
    shots_collection.insert_many(shots_data)
    player_stats_collection.insert_many(player_stats_data)
    haaland_shots_collection.insert_many(haaland_shots_data)
    haaland_goals_collection.insert_many(haaland_goals_data)
    haaland_assists_collection.insert_many(haaland_assists_data)




except Exception as e:
    print("Error importing data:", e)
finally:
    client.close()
# # Perform $lookup to link the collections
# pipeline = [
#     {
#         "$lookup": {
#             "from": shots_collection_name,  # The collection to join with
#             "localField": "match_id",  # Field from the current collection
#             "foreignField": "Match ID",  # Field from the other collection
#             "as": "shots_data"  # The name of the array containing joined data
#         }
#     }
# ]
#
# # Fetch the linked data
# linked_data = list(fixtures_collection.aggregate(pipeline))
#
# # Output linked data
# print("Linked Data:")
# for item in linked_data:
#     print(item)
