from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv, find_dotenv
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

load_dotenv(find_dotenv())
username = os.getenv('INFINITE_USERNAME')
password = os.getenv('INFINITE_PASSWORD')

chrome_options = Options()
# chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)

wait = WebDriverWait(driver, 10)

driver.get('https://greatneckny.infinitecampus.org/campus/portal/students/greatneck.jsp')
