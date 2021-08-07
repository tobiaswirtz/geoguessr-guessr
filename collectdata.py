import time 
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from imagemanipulation import ImageManipulator

api_url = "https://www.geoguessr.com/api/v3/games/"

service = Service('./chromedriver')
service.start()
chrome_options = Options()
chrome_options.add_argument("--user-data-dir=chrome-data")
driver = webdriver.Remote(service.service_url, options=chrome_options)
driver.get("https://www.geoguessr.com/maps/world/play")

for i in range(0, 2000):
    driver.find_element_by_css_selector("button[data-qa='start-game-button']").click()
    time.sleep(1)
    current_url = driver.current_url.split("/")
    game_id = current_url[len(current_url) - 1]
    for j in range(0, 5):
        time.sleep(4.5)
        ImageManipulator.save_image(game_id, str(j))
        driver.find_element_by_class_name("guess-map__canvas").click()
        time.sleep(1)
        driver.find_element_by_css_selector("button[data-qa='perform-guess']").click()
        time.sleep(1.2)
        driver.find_element_by_css_selector("button[data-qa='close-round-result']").click()
        time.sleep(0.5)
    driver.find_element_by_css_selector("a[data-qa='play-same-map']").click()
    time.sleep(0.4)
    driver.find_element_by_css_selector("button[data-qa='play-map-world']").click()
    time.sleep(0.2)
    r = requests.get(url = api_url + game_id)
    data = r.json()
    ImageManipulator.add_annotations(game_id, data)
    current_score = (i+1)*5
    print(str(current_score) + "/10000")
