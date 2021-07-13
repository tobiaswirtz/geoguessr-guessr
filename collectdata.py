from PIL import ImageGrab
from pynput import keyboard 
import numpy as np
import cv2
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service('./chromedriver')
service.start()

driver = webdriver.Remote(service.service_url)

driver.get("https://www.geoguessr.com/maps/world/play")


actual_location_marker_img = cv2.imread('assets/marker.png', 0)
h_marker, w_marker = actual_location_marker_img.shape

def get_coordinates_of_marker(input_img):
    img2 = input_img.copy()
    print(actual_location_marker_img.dtype, img2.dtype, actual_location_marker_img.shape, img2.shape)
    result = cv2.matchTemplate(img2, actual_location_marker_img.astype(np.uint8), cv2.TM_CCOEFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    location = max_loc
    bottom_right = (location[0] + w_marker, location[1] + h_marker)
    cv2.rectangle(img2, location, bottom_right, 255, 5)
    cv2.imwrite('Match.png', img2)
    return (0, 1)


def save_image():
    ## Setup Screenshotting
    im = ImageGrab.grab(bbox=(25,400,2750,1750), xdisplay=None)
    im.show()

def save_coordinates():
    tmp_img = ImageGrab.grab(bbox=(25, 400, 2750, 1200), xdisplay=None)
    numpy_tmp = np.array(tmp_img)
    opencv_img = cv2.cvtColor(numpy_tmp, cv2.COLOR_RGB2GRAY)
    coords = get_coordinates_of_marker(opencv_img.astype(np.uint8))

with keyboard.GlobalHotKeys({
        '<cmd_l>+s': save_image,
        '<cmd_l>+c': save_coordinates
        }) as h:
    h.join()

print("Test")
driver.quit()
