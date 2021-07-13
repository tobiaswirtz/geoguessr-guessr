from PIL import ImageGrab
from pynput import keyboard 


def save_image():
    ## Setup Screenshotting
    im = ImageGrab.grab(bbox=(25,400,2750,1750), xdisplay=None)
    im.show()

def save_coordinates():
    print("Saving coordinates")

with keyboard.GlobalHotKeys({
        '<cmd_l>+s': save_image,
        '<cmd_l>+c': save_coordinates
        }) as h:
    h.join()

## Setup Get Coordinates




