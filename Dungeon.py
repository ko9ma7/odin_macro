import random
import pyautogui as pag
import Mouse
import ClickPos
import time

def dungeonClick():
    dungeon_mouse_pos = [random.randrange(1620, 1665), random.randrange(420, 475)]
    elite_dungeon_mouse_pos = [random.randrange(220, 375), random.randrange(105, 130)]

    Mouse.delayClick(ClickPos.menu_mouse_pos)
    Mouse.delayClick(dungeon_mouse_pos)
    Mouse.delayClick(elite_dungeon_mouse_pos)

def coolTime():
    time.sleep(3630 + random.randrange(10, 50))

def dungeonAuto(select_dungeon, select_floor):
    dungeonClick()
    pag.click()
    Mouse.delayClick(select_dungeon)
    pag.click()
    Mouse.delayClick(select_floor)
    pag.click()
    Mouse.delayClick(ClickPos.dungeon_enter_mouse_pos)
    pag.click()
    time.sleep(random.randrange(20, 30))
    Mouse.delayClick(ClickPos.teleport_mouse_pos)
    time.sleep(random.randrange(8, 12))
    Mouse.delayClick(ClickPos.auto_mode_mouse_pos)
    coolTime()