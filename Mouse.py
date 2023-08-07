import pyautogui as pag
import random
import time

def delayClick(position):
    pag.click(x=position[0], y=position[1], duration=random.uniform(1, 1.5), tween=pag.easeInOutSine)
    time.sleep(random.uniform(1.1, 1.3))

def click(position):
    pag.click(x=position[0], y=position[1], duration=random.uniform(0.8, 1.2), tween=pag.easeInOutSine)

