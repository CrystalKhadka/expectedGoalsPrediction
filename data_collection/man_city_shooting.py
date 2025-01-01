from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os

# Set up Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run browser in headless mode
driver = webdriver.Chrome(options=options)

# URL of the FBref page
url = 'https://fbref.com/en/squads/b8fd03ef/2023-2024/matchlogs/all_comps/shooting/Manchester-City-Match-Logs-All-Competitions'

try:
    # Open the URL
    driver.get(url)

    # Wait for the shooting table to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'matchlogs_for'))
    )

    # Locate the table
    table = driver.find_element(By.ID, 'matchlogs_for')

    # Extract the table's HTML
    table_html = table.get_attribute('outerHTML')

    # Use pandas to parse the table
    df = pd.read_html(table_html)[0]

    # Save the data to a raw CSV file
    output_dir = "../data/raw"
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "man_city_shooting_2023_2024.csv")
    df.to_csv(output_file, index=False)

    print(f"Raw shooting data saved successfully to {output_file}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
