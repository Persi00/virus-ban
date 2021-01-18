from random import randint as r
import pyautogui as gui

while True:
    pos = gui.position()
    pos_y = r(1, 50)
    pos_x = r(1, 50)
    gui.moveTo(pos[0] + pos_x, pos[1] + pos_y)
    gui.click()
    gui.write("Ban!")
    gui.press("enter")
    pos = gui.position()
    pos_y = r(1, 50)
    pos_x = r(1, 50)
    gui.moveTo(pos[0] - pos_x, pos[1] - pos_y)
    gui.click()
    gui.write("Ban!")
    gui.press("enter")