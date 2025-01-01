from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import os

# Set up the WebDriver
driver = webdriver.Chrome()  # Ensure chromedriver is in PATH or provide its full path

# Base URL for Manchester City 2023-2024 fixtures
base_url = 'https://fbref.com/en/squads/b8fd03ef/2023-2024/Manchester-City-Stats#all_matchlogs'
driver.get(base_url)

# Wait for the page to load completely
try:
    # Wait until the match log table is loaded by checking the presence of the table with id 'matchlogs_for'
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'matchlogs_for'))
    )

    # Locate the match log table with the id 'matchlogs_for'
    matchlog_table = driver.find_element(By.ID, 'matchlogs_for')

    # Convert the table to DataFrame
    matchlog_df = pd.read_html(matchlog_table.get_attribute('outerHTML'))[0]
    print(matchlog_df)

    # List to store match dates, opponents, and URLs for detailed match pages
    match_dates_opponents = []

    # Find all match report links in the table (in column 17)
    match_report_links = matchlog_table.find_elements(By.CSS_SELECTOR, 'a[href^="/en/matches/"]')

    # Loop through each row of the match log table
    for index, row in matchlog_df.iterrows():
        # Extract the match date and opponent
        match_date = row['Date']
        opponent = row['Opponent']

        # Find the corresponding match report link
        match_report_link = match_report_links[index].get_attribute('href')

        # Append the match details to the list
        match_dates_opponents.append((match_date, opponent, match_report_link))

    # Loop through each match to visit the match report page and collect shot data
    for match in match_dates_opponents:
        match_date, opponent, match_link = match
        print(f"Processing match on {match_date} against {opponent}...")

        # Visit the match page
        driver.get(match_link)

        try:
            # Wait for the shot log table to load (if it exists)
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'stats_b8fd03ef_summary'))
            )

            # Check if the shot log table exists
            if driver.find_elements(By.ID, 'stats_b8fd03ef_summary'):
                # Locate the shot log table
                shot_table = driver.find_element(By.ID, 'stats_b8fd03ef_summary')

                # Extract the table's HTML
                table_html = shot_table.get_attribute('outerHTML')

                # Use pandas to parse the table
                df = pd.read_html(table_html)[0]

                # Save the shot log to a CSV file named by the match date
                file_name = f"../data/raw/man_city_shot_data_2023_2024/{match_date.replace('-', '_')}_shots.csv"
                df.to_csv(file_name, index=False)

                print(f"Saved shot log for {match_date} against {opponent} as {file_name}")
            else:
                print(f"No shot log data available for match on {match_date} against {opponent}. Skipping...")

        except Exception as e:
            print(f"Error processing match on {match_date} against {opponent}: {e}")

        # Pause to avoid overwhelming the server with requests (optional)
        time.sleep(2)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser after processing all matches
    driver.quit()

print("Match report and shot logs collection complete.")
