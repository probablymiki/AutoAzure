from PIL import ImageGrab
from PIL import ImageOps
from numpy import *
import os
import time
import win32api
import win32con
import random


x_pad = 46
y_pad = 52
x2 = 1873
y2 = 1078
ignorelist = [0, 1, 0, 0]

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))

def get_cords():
    x, y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print x, y

def mainb():
    getbox(1421, 418, 1466, 448)
     # while True:
     #     raw_input("first clikc")
     #     get_cords()

def main():
    while True:
        start14run()
        print 'started 1-4'
        mapScreen()
        print 'entered map screen'
        loclist = [0,0,0,0]
        ints=0
        prev=0
        time.sleep(1)
        while ints < 4:
            mousePos((50,50))
            if ints < len(loclist)-1:
                loclist = checkMap(loclist, prev)
            locToGoTo = getnextLoc(loclist)
            print loclist
            print 'found location'
            gotoLoc(locToGoTo)
            if ints<len(loclist)-1:
                print 'locked', locToGoTo-1
                loclist[locToGoTo-1] = 3
                print loclist
            mapWait(locToGoTo)
            startBattle()
            print 'starting battle'
            time.sleep(10)
            waitBattleOver()
            print 'battle finished'
            movescorescreen()
            print 'back to map'
            if ints < len(loclist):
                time.sleep(4)
            storePopup()
            print 'store poped up'
            ints+=1
            prev = locToGoTo-1

def checkMap(loclist,cur):
    changed = False
    if ignorelist[cur] != 0:
        print 'ignoring ',cur
        temp = loclist[ignorelist[cur]-1]
        loclist[ignorelist[cur]-1]=2
        changed = True
        print 'got booped'
        print loclist
    for indexx in range(len(loclist)):
        if loclist[indexx] == 0:
            if getloc(indexx+1)!=blankloc(indexx+1):
                loclist[indexx] =1
    if changed:
        loclist[ignorelist[cur]-1]=temp
    return loclist

def getnextLoc(loclist):
    indexv = 0;
    for x in loclist:
        if x == 1:
            break
        else:
            indexv += 1
    return indexv+1

def mapWait(loc):
    while True:
        time.sleep(2)
        if getbox(1320, 840, 1720, 970) == 84640:
            print 'entered team select screen'
            break
        elif getbox(1136, 500, 1445, 585) == 46783:
            print 'ambush screen'
            mousePos((random.randrange(1136, 1445), random.randrange(500, 585)))
            time.sleep(.1)
            leftClick()
            time.sleep(1)
            if getbox(1320, 840, 1720, 970) == 84640:
                startBattle()
                time.sleep(10)
                waitBattleOver()
                movescorescreen()
                storePopup()
        else:
            print 'air raid / trying again'
            gotoLoc(loc)
def waitBattleOver():
    while True:
        time.sleep(3)
        if getbox(1726, 34, 1787, 95) == 10597:
            time.sleep(.5)
            break
def mapScreen():
    while True:
        time.sleep(1)
        if getbox(1421, 418, 1466, 448) == 3606:
            break
def storePopup():
    if getbox(783, 670, 1041, 744) == 47444:
        mousePos((random.randrange(783, 1041), random.randrange(670, 744)))
        time.sleep(.1)
        leftClick()
        time.sleep(.5)

def start14run():
    mousePos((random.randrange(1065, 1500), random.randrange(185, 305)))
    time.sleep(.1)
    leftClick()
    time.sleep(float(random.randrange(100, 150))/100)

    mousePos((random.randrange(1195, 1465), random.randrange(650, 725)))
    time.sleep(.1)
    leftClick()
    time.sleep(float(random.randrange(100, 150)) / 100)

    mousePos((random.randrange(1195, 1465), random.randrange(765, 850)))
    time.sleep(.1)
    leftClick()
    time.sleep(float(random.randrange(100, 150)) / 100)

def startBattle():
    mousePos((random.randrange(1320, 1720), random.randrange(840, 970)))
    time.sleep(.1)
    leftClick()
    time.sleep(float(random.randrange(100, 200)) / 100)

def gotoLoc(loc):
    if loc == 1:
        print 'going to loc 1'
        mousePos((random.randrange(660, 740), random.randrange(420, 470)))
        time.sleep(.1)
        leftClick()
        time.sleep(float(random.randrange(100, 200)) / 100)
    elif loc == 2:
        print 'going to loc 2'
        mousePos((random.randrange(660, 700), random.randrange(550, 575)))
        time.sleep(.1)
        leftClick()
        time.sleep(float(random.randrange(100, 200)) / 100)
    elif loc == 3:
        print 'going to loc 3'
        mousePos((random.randrange(840, 890), random.randrange(700, 735)))
        time.sleep(.1)
        leftClick()
        time.sleep(float(random.randrange(100, 200)) / 100)
    elif loc == 4:
        print 'going to loc 4'
        mousePos((random.randrange(1230, 1300), random.randrange(695, 735)))
        time.sleep(.1)
        leftClick()
        time.sleep(float(random.randrange(100, 200)) / 100)
    elif loc ==5:
        print 'going to loc boss'
        mousePos((random.randrange(1400, 1500), random.randrange(680, 750)))
        time.sleep(.1)
        leftClick()
        time.sleep(float(random.randrange(100, 200)) / 100)

def screenGrab():
    box = (x_pad, y_pad, x2, y2)
    im = ImageGrab.grab(box)
    return im

def grab():
    box = (x_pad, y_pad, x2, y2)
    im = ImageGrab.grab(box)
    a = array(im.getcolors())
    a = a.sum()
    print a
    return a

def getbox(x,y,x2,y2):
    box = (x + x_pad, y + y_pad, x2 + x_pad, y2 + y_pad)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    im.save(os.getcwd() + '\\full_snap__' + 'getbox' +
            '.png', 'PNG')
    a = array(im.getcolors())
    a = a.sum()
    return a

def movescorescreen():
    time.sleep(1)
    mousePos((random.randrange(260, 1530), random.randrange(750, 990)))
    time.sleep(.1)
    leftClick()
    time.sleep(float(random.randrange(50, 100)) / 100)
    mousePos((random.randrange(260, 1530), random.randrange(750, 990)))
    time.sleep(.1)
    leftClick()
    time.sleep(float(random.randrange(300, 350)) / 100)
    if getbox(1230, 962, 1297, 971) == 719:
        print 'got ship'
        mousePos((random.randrange(260, 1530), random.randrange(750, 990)))
        time.sleep(.1)
        leftClick()
        time.sleep(float(random.randrange(300, 350)) / 100)
    mousePos((random.randrange(260, 1530), random.randrange(500, 990)))
    time.sleep(.1)
    leftClick()
    while True:
        time.sleep(.5)
        if getbox(1450, 835, 1720, 910) == 42109:
            mousePos((random.randrange(1450, 1720), random.randrange(835, 910)))
            time.sleep(1)
            leftClick()
            time.sleep(.5)
            leftClick()
            break

def getloc(loc):
    if loc == 1:
        box = (725+x_pad, 420+y_pad, 750+x_pad, 450+y_pad)
        im = ImageOps.grayscale(ImageGrab.grab(box))
        im.save(os.getcwd() + '\\full_snap__' + 'loc1' +
                '.png', 'PNG')
        a = array(im.getcolors())
        a = a.sum()
        print 'checked loc 1', a
        return a
    elif loc == 2:
        box = (725+x_pad, 551+y_pad, 750+x_pad, 591+y_pad)
        im = ImageOps.grayscale(ImageGrab.grab(box))
        im.save(os.getcwd() + '\\full_snap__' + 'loc2' +
                '.png', 'PNG')
        a = array(im.getcolors())
        a = a.sum()
        print 'checked loc 2 ', a
        return a
    elif loc ==3:
        box = (905+x_pad, 700+y_pad, 930+x_pad, 730+y_pad)
        im = ImageOps.grayscale(ImageGrab.grab(box))
        im.save(os.getcwd() + '\\full_snap__' + 'loc3' +
                '.png', 'PNG')
        a = array(im.getcolors())
        a = a.sum()
        print 'checked loc 3 ',a
        return a
    elif loc ==4:
        box = (1285+x_pad, 700+y_pad, 1310+x_pad, 730+y_pad)
        im = ImageOps.grayscale(ImageGrab.grab(box))
        im.save(os.getcwd() + '\\full_snap__' + 'loc4' +
                '.png', 'PNG')
        a = array(im.getcolors())
        a = a.sum()
        print 'checked loc 4 ', a
        return a
def blankloc(loc):
    if loc ==1:
        return 3106
    elif loc ==2:
        return 8337
    elif loc ==3:
        return 2047
    elif loc == 4:
        return 1848

if __name__ =='__main__':
    main()