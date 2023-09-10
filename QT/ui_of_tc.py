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
from auto_gui_base import find_and_click_pic
from network import network_connection


def click_female_in_comment_auto():
    print("***********************begin***********************")
    pic_path = setting.trans_pic_name_to_path(['comment.png'])
    los = pyautogui.locateOnScreen(pic_path[0], confidence=0.9, region=setting.qt_ui_region)
    if los is not None:
        cent_x, comment_y = pyautogui.center(los)
        print("点击comment按钮")
        pyautogui.moveTo(cent_x, comment_y, duration=0.2)
        click_comment_icon_and_back(cent_x, comment_y)
        print("该comment完成，进行下一个comment")

        # 计算向下滑动距离
        ui = ui_identify()
        if ui["UI"] == "同城":
            cent_x, cent_y = ui["坐标"][0], ui["坐标"][1]
            print("移动鼠标到tc下方")
            pyautogui.moveTo(cent_x, cent_y + 100, duration=0.2)
            # time.sleep(1)
        else:
            print("不是tc页面")
            # self.reset_number += 1
            ui_dic = reset_to_ui("同城")
            if ui_dic["UI"] == "同城":
                cent_x, cent_y = ui_dic["坐标"][0], ui_dic["坐标"][1]
                print("移动鼠标到tc下方")
                pyautogui.moveTo(cent_x, cent_y + 100, duration=0.2)
            else:
                restart_qt()
            # reset_to_tc()
            # quit()

        dist_scroll = int(-abs(cent_y - comment_y))
        dist_scroll = int(1.2 * dist_scroll)
        print("tc中滑动", dist_scroll)
        network_connection()
        pyautogui.scroll(dist_scroll)
    else:
        print("没有匹配commen,滑动")
        ui = ui_identify()
        if ui["UI"] == "同城":
            cent_x, cent_y = ui["坐标"][0], ui["坐标"][1]
            print("移动鼠标到tc下方")
            pyautogui.moveTo(cent_x, cent_y + 100, duration=0.2)
            # time.sleep(1)
        else:
            print("不是tc页面，退出")
            # self.reset_number += 1
            reset_to_ui()
        pyautogui.scroll(-600)
