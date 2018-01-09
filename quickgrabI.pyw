from PIL import ImageGrab
import os
import time

x_pad = 46
y_pad = 52
x2 = 1873
y2 = 1078

def screenGrab():
    box = (x_pad, y_pad, x2, y2)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
            '.png', 'PNG')


def main():
    screenGrab()


if __name__ =='__main__':
    main()