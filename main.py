from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# Get the current directory of the script
current_directory = os.path.dirname(os.path.realpath(__file__))

# Set the relative path to chromedriver.exe
chromedriver_path = os.path.join(current_directory, 'chromedriver32.exe')  # Adjust the path if necessary

# Create Chrome options
options = Options()
options.debugger_address = "localhost:9222"  # Use the address of the remote Chrome instance

# Create a Service object and pass the path to chromedriver
service = Service(chromedriver_path)

# Pass the Service and Options objects to the Chrome WebDriver
driver = webdriver.Chrome(service=service, options=options)

# Open the website
driver.get("https://www.hh.ru")
print(driver.title)

# Wait for all buttons to be present
wait = WebDriverWait(driver, 10)  # Wait for up to 10 seconds
buttons = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//button[@class="container--j4NR0XcPvN4DXL8p" and @data-qa="link"]')))

# Print all buttons found
print(f"Total buttons found: {len(buttons)}")
for i, button in enumerate(buttons):
    print(f"Button {i + 1}: {button.get_attribute('outerHTML')}")

# Example of interacting with the second button (if it exists)
if len(buttons) > 1:
    second_button = buttons[4]
    second_button.click()  # Click the second button
    print("Second button clicked successfully!")

# You can add more actions or close the browser later
# driver.quit()
