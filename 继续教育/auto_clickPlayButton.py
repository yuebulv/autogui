import pyautogui
from tkinter import *
import tkinter as tk
import time
import random


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('自动点播放按钮')
        self.lbl = tk.Label(self,
                            text='刷新时间(s)：',
                            padx=0,
                            pady=0)
        # self.lbl.pack()
        self.lbl.grid(row=0, column=2, stick=EW)
        self.txt = tk.Text(self, width=5, height=1)
        # self.txt.pack()
        self.txt.grid(row=0, column=3, stick=EW)
        self.txt.insert(INSERT, '10')
        self.status_text = '状态'
        self.lbl2 = tk.Label(self,
                             text=self.status_text)
        # self.lbl2.pack()
        self.lbl2.grid(row=1, column=2, columnspan=2)
        self.button = tk.Button(self,
                                text='退出',
                                width=10,
                                command=self.quit)
        self.button.grid(row=2, column=2, columnspan=2)
        self.quit_numner = 0
        self.update_auto()

    def update_auto(self):
        pyautogui.FAILSAFE = False
        settings = setting()
        los = pyautogui.locateOnScreen('playbutton.png', confidence=0.9, region=settings["ui_region"])
        if los is not None:
            x0, y0 = pyautogui.position()
            x, y = pyautogui.center(los)
            pyautogui.click(x, y)
            pyautogui.moveTo(x0, y0)
            # pyautogui.hotkey("alt", "tab")
            self.quit_numner = 0
            self.status_text = '匹配到播放按钮，点击播放'
        else:
            zanting_los = pyautogui.locateOnScreen('zanting.png', confidence=0.9, region=settings["ui_region"])
            if zanting_los is not None:
                self.status_text = '正在播放'+time.strftime("%H:%M:%S", time.localtime())
            else:
                self.quit_numner += 1
                print(self.quit_numner, "done")
                # pyautogui.hotkey("alt", "F4")
            # im = pyautogui.screenshot(region=settings["ui_region"])
            # im.save(r'.\screen\截屏.png')
        # pyautogui.moveTo(random.randint(0, 100), random.randint(0, 100))

        # if self.quit_numner >= settings["quit_numner"]:
        #     quit()
        self.lbl2.config(text=self.status_text)
        self.after(int(self.txt.get('1.0', END))*1000, self.update_auto)


def setting():
    ui_region = [1400, 50, 520, 500]
    quit_numner = 5
    res = {"ui_region": ui_region, "quit_numner": quit_numner}
    return res


if __name__ == '__main__':
    app = App()
    app.geometry('280x100+200+300')
    app.mainloop()

    # res = pyautogui.position()
    # print(res)