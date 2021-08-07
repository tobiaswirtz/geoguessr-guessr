import os
import pathlib
import cv2
import numpy as np
from PIL import ImageGrab, Image
import cv2

current_path = str(pathlib.Path(__file__).parent.resolve())
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

    def save_image(game_id, round_number):
        ## Setup Screenshotting
        im = ImageGrab.grab(bbox=(25,400,2750,1750), xdisplay=None)
        filename = game_id + "-" + round_number + ".png"
        path = "./tmp/" + filename
        im.save(path)

    def save_coordinates():
        tmp_img = ImageGrab.grab(bbox=(25, 400, 2750, 1200), xdisplay=None)
        numpy_tmp = np.array(tmp_img)
        opencv_img = cv2.cvtColor(numpy_tmp, cv2.COLOR_RGB2GRAY)
        coords = ImageManipulator.get_coordinates_of_marker(opencv_img.astype(np.uint8))
        return coords

    def add_annotations(game_id, data):
        for i in range(0, 5):
            new_filename = str(((data["rounds"])[i])['lat']) + "," + str(((data["rounds"])[i])['lng']) + ".png"
            old_filename = current_path + "/tmp/" + game_id + "-" + str(i) + ".png"
            os.rename(old_filename, current_path + "/data/" + new_filename)
