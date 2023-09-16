import time
import pyautogui


def screenshot():
    name = int(round(time.time() * 1000))
    name = "D:/PYTHON Projects/Screenshot_App/screenshot images/{}.png".format(name)
    time.sleep(5)
    img = pyautogui.screenshot(name)
    img.show()


screenshot()