import time
import datetime
from tkinter import *
import tkinter as tk
import pyautogui
from start import start_qt
from start import restart_qt
import setting
from qt_ui import click_comment_icon_and_back
from qt_ui import ui_identify
from qt_ui import reset_to_ui, ui_mutually_like_traverse
from quit_qt import qt_quit
from music import qt_beep
from daytask import get_day_qtb


class App(tk.Tk):
    def __init__(self, seconds: int, minutes=0, hours=0):
        super().__init__()
        self.time_0 = datetime.datetime.now()
        self.seconds, self.minutes, self.hours = seconds, minutes, hours
        self.count = 0
        # self.test()
        self.reset_number = 0
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
        self.txt.insert(INSERT, '20')
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
        # self.update_auto()
        self.click_female_in_comment_auto()

    def click_female_in_comment_auto(self):
        t2 = datetime.timedelta(seconds=self.seconds, minutes=self.minutes, hours=self.hours)
        time_end = self.time_0 + t2
        try:
            pic_path = setting.trans_pic_name_to_path(['comment.png'])
            los = pyautogui.locateOnScreen(pic_path[0], confidence=0.9, region=setting.qt_ui_region)
            if los is not None:
                cent_x, comment_y = pyautogui.center(los)
                self.status_text = '匹配到comment按钮，点击'
                # cent_x_last, cent_y_last = cent_x, female_y
                # Point(x=400, y=860)
                print("点击comment按钮")
                pyautogui.moveTo(cent_x, comment_y, duration=0.2)
                # time.sleep(1)
                click_comment_icon_and_back(cent_x, comment_y)
                # pyautogui.PAUSE = 0.5
                print("该comment完成，进行下一个comment")
                # time.sleep(1)
                # pyautogui.moveTo(cent_x_last, cent_y_last)

                # 计算向下滑动距离
                ui = ui_identify()
                if ui["UI"] == "同城":
                    cent_x, cent_y = ui["坐标"][0], ui["坐标"][1]
                    print("移动鼠标到tc下方")
                    pyautogui.moveTo(cent_x, cent_y+100, duration=0.2)
                    # time.sleep(1)
                else:
                    print("不是tc页面")
                    self.reset_number += 1
                    ui_dic = reset_to_ui("同城")
                    if ui_dic["UI"] == "同城":
                        cent_x, cent_y = ui_dic["坐标"][0], ui_dic["坐标"][1]
                        print("移动鼠标到tc下方")
                        pyautogui.moveTo(cent_x, cent_y + 100, duration=0.2)
                    else:
                        quit()
                    # reset_to_tc()
                    # quit()

                dist_scroll = int(-abs(cent_y - comment_y))
                dist_scroll = int(1.2 * dist_scroll)
                print("tc中滑动", dist_scroll)
                # print(dist_scroll)
                time.sleep(1)
                # pyautogui.scroll(-10)
                # pyautogui.scroll(-50)
                pyautogui.scroll(dist_scroll)
                # pyautogui.scroll(-462)
            else:
                print("没有匹配commen,滑动")
                ui = ui_identify()
                if ui["UI"] == "同城":
                    cent_x, cent_y = ui["坐标"][0], ui["坐标"][1]
                    print("移动鼠标到tc下方")
                    pyautogui.moveTo(cent_x, cent_y+100, duration=0.2)
                    # time.sleep(1)
                else:
                    print("不是tc页面，退出")
                    self.reset_number += 1
                    reset_to_tc()
                pyautogui.scroll(-600)
                self.status_text = '没有匹配commen，正在播放' + time.strftime("%H:%M:%S", time.localtime())
                # im = pyautogui.screenshot(region=setting.qt_ui_region)
                # im.save(r'.\screen\截屏.png')
            print("reset_number", self.reset_number)
            if self.reset_number > 0:
                restart_qt()
                self.reset_number = 0
        except:
            print("未知错误")
            im = pyautogui.screenshot(region=setting.qt_ui_region)
            im.save(r'.\screen\未知错误.png')
            restart_qt()
        if datetime.datetime.now() > time_end:
            print(f"开始时间{self.time_0},结束时间{datetime.datetime.now()},用时{datetime.datetime.now()-self.time_0}")
            # ui_mutually_like_traverse()
            # get_day_qtb()
            qt_quit()
        self.lbl2.config(text=self.status_text)
        self.after(int(self.txt.get('1.0', END)) * 1000, self.click_female_in_comment_auto())


def main(*run_time):
    # 进入tc界面
    pic_path = setting.trans_pic_name_to_path(['tc.png'])
    tc_loc = pyautogui.locateOnScreen(pic_path[0], confidence=0.7, region=setting.qt_ui_region)
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
    app = App(*run_time)
    app.geometry('280x100+200+300')
    app.mainloop()


if __name__ == "__main__":
    start_qt()
    main(0, 20, 0)
