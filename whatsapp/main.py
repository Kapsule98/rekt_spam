import pyautogui as pt
from time import sleep
import pyperclip
import random

msg_to_send_ok = ":ok"
msg_to_send_pray = ":pray"
msg_to_send_lenny = "( ͡° ل͜ ͡°)"
sleep(2)
position1 = pt.locateOnScreen("paperclip.PNG",confidence=.6)
x = position1[0]
y = position1[1]

def getmsg():
    global x,y
    try:
        position = pt.locateOnScreen("paperclip.PNG",confidence=.6)
        x = position[0]
        y = position[1]
        ##pt.moveTo(x,y,duration=.5)
        x+=100
        y-=50
        pt.moveTo(x,y,duration=.5)
        posXY = pt.position()
        try:
            if pt.pixelMatchesColor(int(posXY[0]),int(posXY[1]),(255,255,255),tolerance=10):
                pt.moveRel(-10,0)
                pt.tripleClick()
                pt.moveRel(60,80)
                pt.click()
                pt.typewrite(msg_to_send_pray,interval=.5)
                pt.typewrite("\n")
                sleep(0.5)
                pt.press('enter')
            else :
                print("waiting for new msg")
        
        except(Exception):
            print("color match failed")
    except(Exception):
        print("paperclip not found")

    sleep(3)


while True:
    getmsg()

