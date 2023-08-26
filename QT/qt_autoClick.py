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
        self.txt.insert(INSERT, '3')
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
        self.update_auto()

    def update_auto(self):
        los = pyautogui.locateOnScreen('female.png', confidence=0.9)
        if los is not None:
            cent_xy = pyautogui.center(los)
            # pyautogui.click(cent_xy)
            cent_x, cent_y = cent_xy
            cent_x_last, cent_y_last = cent_x, cent_y
            # Point(x=400, y=860)
            pyautogui.click(cent_x, cent_y)
            self.status_text = '匹配到按钮，点击'
            # pyautogui.PAUSE = 0.5
            time.sleep(1)
            los = pyautogui.locateOnScreen('back.png', confidence=0.6)
            if los is not None:
                cent_xy = pyautogui.center(los)
                cent_x, cent_y = cent_xy
                pyautogui.click(cent_x, cent_y)
            else:  # 匿名用户
                los = pyautogui.locateOnScreen('chacha.png', confidence=0.9)
                if los is not None:
                    cent_xy = pyautogui.center(los)
                    cent_x, cent_y = cent_xy
                    pyautogui.click(cent_x, cent_y)
                else:  # 隐身用户
                    pyautogui.click(cent_x, cent_y)
            pyautogui.moveTo(cent_x_last, cent_y_last)
            pyautogui.scroll(-700)
        else:
            pyautogui.scroll(-700)
            self.status_text = '没有匹配到按钮，正在播放'+time.strftime("%H:%M:%S", time.localtime())
            im = pyautogui.screenshot()
            im.save(r'.\screen\截屏.png')
        # pyautogui.moveTo(random.randint(0, 100), random.randint(0, 100))
        self.lbl2.config(text=self.status_text)
        self.after(int(self.txt.get('1.0', END))*1000, self.update_auto)


def main():
    # 进入同城界面
    tc_loc = pyautogui.locateOnScreen('tc.png', confidence=0.9)
    loc = tc_loc
    if loc is not None:
        cent_xy = pyautogui.center(loc)
        tc_x, tc_y = cent_xy
        pyautogui.click(cent_xy)
    else:
        print("没匹配到tc.png")
        # quit()
    time.sleep(1)

    # 进入female界面
    app = App()
    app.geometry('280x100+200+300')
    app.mainloop()


if __name__ == '__main__':
    main()


