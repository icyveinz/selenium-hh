import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
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