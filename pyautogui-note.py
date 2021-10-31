import pyautogui
from tkinter import *
import time


def task(timejiange):
    while True:
        print(timejiange)
        timejiange = float(timejiange)
        los = pyautogui.locateOnScreen('playbutton.png')
        if los is not None:
            cent_xy = pyautogui.center(los)
            pyautogui.click(cent_xy)
        time.sleep(timejiange)

# x, y = pyautogui.position()
# po = 'x:= ' + str(x).rjust(4) + 'y: ' + str(y).rjust(4)
# im = pyautogui.screenshot()
# print(im.getpixel((-1860, 554)))
# print(po)


if __name__ == '__main__':
    tk = Tk()
    txt = Text(tk, width=10, height=2)
    txt.pack()
    txt.insert(INSERT, '6')
    timejiange = txt.get('1.0', END)
    task(timejiange)
    tk.mainloop()