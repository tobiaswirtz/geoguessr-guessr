import time 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from imagemanipulation import ImageManipulator

service = Service('./chromedriver')
service.start()
chrome_options = Options()
chrome_options.add_argument("--user-data-dir=chrome-data")
driver = webdriver.Remote(service.service_url, options=chrome_options)
driver.get("https://www.geoguessr.com/maps/world/play")

for i in range(0, 2000):
    driver.find_element_by_css_selector("button[data-qa='start-game-button']").click()
    for i in range(0, 5):
        time.sleep(4.5)
        ImageManipulator.save_image(tmp=False)
        driver.find_element_by_class_name("guess-map__canvas").click()
        time.sleep(1)
        driver.find_element_by_css_selector("button[data-qa='perform-guess']").click()
        time.sleep(1)
        (x_marker, y_marker) = ImageManipulator.save_coordinates()
        print(x_marker, y_marker)
        actions = ActionChains(driver)
        actions.move_to_element_with_offset(driver.find_element_by_tag_name('body'), 0,0)
        actions.move_by_offset(x_marker, y_marker).click().perform()
        driver.find_element_by_css_selector("button[data-qa='close-round-result']").click()
        time.sleep(0.5)
    driver.find_element_by_css_selector("a[data-qa='play-same-map']").click()
    time.sleep(0.2)
    driver.find_element_by_css_selector("button[data-qa='play-map-world']").click()
    time.sleep(0.2)

