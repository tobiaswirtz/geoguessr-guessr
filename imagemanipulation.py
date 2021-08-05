import time
import cv2
import numpy as np
from PIL import ImageGrab, Image
import cv2

actual_location_marker_img = cv2.imread('assets/marker.png', 0)
h_marker, w_marker = actual_location_marker_img.shape

class ImageManipulator:
    def get_coordinates_of_marker(input_img):
        img2 = input_img.copy()
        result = cv2.matchTemplate(img2, actual_location_marker_img.astype(np.uint8), cv2.TM_CCOEFF)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        location = max_loc
        bottom_right = (location[0] + w_marker, location[1] + h_marker)
        return bottom_right 

    def save_image(tmp):
        ## Setup Screenshotting
        im = ImageGrab.grab(bbox=(25,400,2750,1750), xdisplay=None)
        filename = time.strftime("%Y%m%d-%H%M%S") + ".png"
        if tmp == True:
            path = "./tmpflow/" + filename
            im.save(path)
        else:
            path = "./tmp/" + filename
            im.save(path)

    def save_coordinates():
        tmp_img = ImageGrab.grab(bbox=(25, 400, 2750, 1200), xdisplay=None)
        numpy_tmp = np.array(tmp_img)
        opencv_img = cv2.cvtColor(numpy_tmp, cv2.COLOR_RGB2GRAY)
        coords = ImageManipulator.get_coordinates_of_marker(opencv_img.astype(np.uint8))
        return coords
