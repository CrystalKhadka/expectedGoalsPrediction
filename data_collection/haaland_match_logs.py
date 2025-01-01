from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# Set up Selenium WebDriver
driver = webdriver.Chrome()  # Ensure chromedriver is in PATH or provide its full path

# Open the base URL
base_url = 'https://fbref.com/en/players/1f44ac21/matchlogs/2023-2024/Erling-Haaland-Match-Logs'
driver.get(base_url)

try:

    # Wait for the table to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'matchlogs_all'))
    )

    # Locate the table
    table = driver.find_element(By.ID, 'matchlogs_all')

    # Extract the table's HTML
    table_html = table.get_attribute('outerHTML')

    # Use pandas to parse the table
    df = pd.read_html(table_html)[0]

    # Save the data to a CSV file
    output_file = '../data/raw/haaland_match_logs_2023_2024.csv'
    df.to_csv(output_file, index=False)

    print(f"Goal and Shot Creation data saved successfully to {output_file}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
