import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

# URL for Erling Haaland's Understat page
url = "https://understat.com/player/8260"

# Fetch the page content
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Find the script containing shot data
scripts = soup.find_all("script")
shot_data_script = None
for script in scripts:
    if "shotsData" in script.text:
        shot_data_script = script.text
        break

# Decode the Unicode sequences
raw_data = bytes(shot_data_script, "utf-8").decode("unicode_escape")

print(raw_data)



# Extract the JSON part (between the quotes following JSON.parse)
start_index = raw_data.find('[')  # Find the start of the JSON array
end_index = raw_data.rfind(']') + 1  # Find the end of the JSON array
json_string = raw_data[start_index:end_index]  # Slice the JSON part

# Parse the JSON string
try:
    shots_data = json.loads(json_string)
except json.JSONDecodeError as e:
    print(f"JSON parsing error: {e}")
    shots_data = []

# Convert to pandas DataFrame if data exists
if shots_data:
    df = pd.DataFrame(shots_data)

    # Save to CSV
    output_file = "../data/raw/haaland_shot_map.csv"
    df.to_csv(output_file, index=False)

    print(f"Data saved successfully to {output_file}")

    # Display the first few rows
    print(df.head())
else:
    print("No data to process.")
