import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

service = Service('./chromedriver')
service.start()

chrome_options = Options()
chrome_options.add_argument("--user-data-dir=chrome-data")
driver = webdriver.Remote(service.service_url,options=chrome_options)
chrome_options.add_argument("user-data-dir=chrome-data")
driver.get('http://geoguessr.com')
time.sleep(30)  # Time to enter credentials
driver.quit()

