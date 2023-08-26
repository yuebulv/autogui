import pyautogui
from tkinter import *
import tkinter as tk


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
        self.txt.insert(INSERT, '60')
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
        los = pyautogui.locateOnScreen('playbutton.png')
        if los is not None:
            cent_xy = pyautogui.center(los)
            pyautogui.click(cent_xy)
            self.status_text = '匹配到播放按钮，点击播放'
        else:
            im = pyautogui.screenshot()
            im.save('截屏.png')
            self.status_text = '没有匹配到播放按钮，正在播放'
        self.lbl2.config(text=self.status_text)
        self.after(int(self.txt.get('1.0', END))*1000, self.update_auto)


if __name__ == '__main__':
    app = App()
    app.geometry('280x100+200+300')
    app.mainloop()