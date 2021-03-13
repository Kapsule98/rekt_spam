import pyautogui as pt
from time import sleep

while 1:
    posXY = pt.position()
    print(posXY)
    print(pt.pixel(posXY[0],posXY[1]))
    sleep(1)
    if posXY[0] == 0:
        break