import pyautogui
from tkinter import *
import tkinter as tk
import time
import os
import re
import pyperclip

class App(tk.Tk):
    # msc = 1000
    # global status_text
    # status_text = ''


    def __init__(self):
        super().__init__()
        self.title('点餐工具')
        self.lbl = tk.Label(self,
                            text='第一步：确认menu下菜单是否正确（每个文件最多认15个菜名）；',
                            anchor=W,)
        self.lbl.grid(row=0, column=0, stick=W, columnspan=4)
        self.lbl2 = tk.Label(self,
                            text='第二步：点击QQ群应用下的群投票；',
                            anchor=W,)
        self.lbl2.grid(row=1, column=0, stick=W)
        self.lbl3 = tk.Label(self,
                            text='第三步：点击开始；',
                            anchor=W,)
        self.lbl3.grid(row=2, column=0, stick=W)
        self.lbl6 = tk.Label(self,
                             text='',
                             anchor=W)
        self.lbl6.grid(row=3, column=0, stick=W, columnspan=2)
        self.button = tk.Button(self,
                                text='开始',
                                width=15,
                                command=self.getMenuList)
        self.button.grid(row=4, column=0, columnspan=1)
        self.button = tk.Button(self,
                                text='退出',
                                width=15,
                                command=self.quit)
        self.button.grid(row=4, column=1, columnspan=1)
        self.lbl5 = tk.Label(self,
                             text='',
                             anchor=W)
        self.lbl5.grid(row=5, column=0, stick=W, columnspan=2)
        self.status_text = StringVar()

        self.lbl4 = tk.Label(self,
                             textvariable=self.status_text,
                             anchor=W)
        self.lbl4.grid(row=6, column=0, stick=W, columnspan=2)

    def update(self):
        global status_text
        self.status_text.set(str(status_text))
        self._upd = self.after(1000, self.update)

    def order_auto(self, menuTheme, menuList):
        # global status_text
        # self.update()
        # 已知menuTheme,menuList,发布群投票点餐
        los = pyautogui.locateOnScreen('picture/newvote.png', confidence=0.9)
        if los is not None:
            cent_xy = pyautogui.center(los)
            pyautogui.click(cent_xy)
            status_text = '匹配到newvote'
            # self.lbl4.config(text=self.status_text)
            los = pyautogui.locateOnScreen('picture/addItem.png', confidence=0.95)
            while los is not None:
                cent_xy = pyautogui.center(los)
                pyautogui.click(cent_xy)
                pyautogui.moveRel(40, 0)
                self.status_text = '匹配到add item'
                self.lbl4.config(text=self.status_text)
                los = pyautogui.locateOnScreen('picture/addItem.png', confidence=0.95)
            else:
                with open('log/log.txt', 'a', encoding='utf-8') as file_object:
                    file_object.write(time.asctime(time.localtime(time.time())) + ',没有匹配到addItem.png;\n')
            pyautogui.scroll(1000)
            i = 0
            los = pyautogui.locateOnScreen('picture/theme.png', confidence=0.95)
            if los is not None:
                cent_xy = pyautogui.center(los)
                pyautogui.click(cent_xy)
                pyperclip.copy(f'点餐（{menuTheme}）')
                pyautogui.hotkey('ctrl', 'v')
                # pyautogui.typewrite(menuTheme)  # 不支持输入中文
                self.status_text = '匹配到theme'
                self.lbl4.config(text=self.status_text)
                while i < 3:
                    pyautogui.press('tab')
                    pyperclip.copy(menuList[i])
                    pyautogui.hotkey('ctrl', 'v')
                    # pyautogui.typewrite(menuList[i])
                    i += 1
                # try:
                #     pyautogui.press('tab')
                #     pyautogui.press('tab')
                #     time.sleep(5)
                #     pyperclip.copy(menuList[i])
                #     pyautogui.hotkey('ctrl', 'v')
                #     # pyautogui.typewrite(menuList[i])
                #     i += 1
                # except IndexError:
                #     pass
                # else:
                while i < 15:
                    try:
                        pyperclip.copy(menuList[i])
                    except IndexError:
                        break
                    else:
                        pyautogui.press('tab')
                        pyautogui.press('tab')
                        pyautogui.press('tab')
                        pyautogui.hotkey('ctrl', 'v')
                        # pyautogui.typewrite(menuList[i])
                        i += 1
                pyautogui.scroll(-1000)
                los = pyautogui.locateOnScreen('picture/checkBox.png', confidence=0.95)
                if los is not None:
                    cent_xy = pyautogui.center(los)
                    pyautogui.click(cent_xy)
                    pyautogui.press('tab')
                    pyautogui.typewrite(str(len(menuList)))  # 每人可多选最大数量
                    time.sleep(0.5)
                    self.status_text = '匹配到checkBox'
                    self.lbl4.config(text=self.status_text)
                    los = pyautogui.locateOnScreen('picture/confirm.png', confidence=0.95)
                    if los is not None:
                        cent_xy = pyautogui.center(los)
                        pyautogui.click(cent_xy)
                        self.status_text = '匹配到confirm'
                        self.lbl4.config(text=self.status_text)
                    else:
                        with open('log/log.txt', 'a', encoding='utf-8') as file_object:
                            file_object.write(time.asctime(time.localtime(time.time())) + ',没有匹配到confirm.png;\n')
                else:
                    with open('log/log.txt', 'a', encoding='utf-8') as file_object:
                        file_object.write(time.asctime(time.localtime(time.time()))+',没有匹配到checkBox;\n')
            else:
                with open('log/log.txt', 'a', encoding='utf-8') as file_object:
                    file_object.write(time.asctime(time.localtime(time.time())) + ',没有匹配到theme.png;\n')
        else:
            with open('log/log.txt', 'a', encoding='utf-8') as file_object:
                file_object.write(time.asctime(time.localtime(time.time()))+',没有匹配到newvote.png;\n')
        # self.lbl4.config(text=self.status_text)

    def getMenuList(self):
        # 依次打开menu/.txt文件，解析出menuTheme, menuList
        for files in os.listdir('menu/'):
            if os.path.splitext(files)[1] == '.txt':
                regx = r'[\n\t]*(.+)[\n\t]*'
                with open('menu/' + files, 'r', encoding='utf-8') as file_object:
                    contents = file_object.read()
                    contents_list = re.findall(regx, contents)
                    # print(os.path.splitext(files)[0])
                    # print(contents_list)
                    self.order_auto(menuTheme=os.path.splitext(files)[0], menuList=contents_list)
                    time.sleep(3)


if __name__ == '__main__':

    app = App()
    app.geometry('380x170+200+300')
    app.mainloop()