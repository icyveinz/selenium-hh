from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os

def get_driver():
    current_directory = os.path.dirname(os.path.realpath(__file__))
    chromedriver_path = os.path.join(current_directory, '../chromedriver32.exe')
    options = Options()
    options.debugger_address = "localhost:9222"
    service = Service(chromedriver_path)
    return webdriver.Chrome(service=service, options=options)