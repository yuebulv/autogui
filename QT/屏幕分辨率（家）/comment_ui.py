import pyautogui
from tkinter import *
import tkinter as tk
import time


def click_comment_icon_and_back(icon_x, icon_y):
    # pyautogui.PAUSE = 0.5
    network_connection()
    pyautogui.moveTo(icon_x, icon_y)
    pyautogui.click(icon_x, icon_y)
    time.sleep(0.5)
    n_count = 0
    while True:
        los = pyautogui.locateOnScreen('laolao.png', confidence=0.7)
        if los is not None:
            print("检测到comment，进入comment页面")
            cent_x, cent_y = pyautogui.center(los)
            # cent_x = int(cent_y-200)
            # time.sleep(1)
            pyautogui.moveTo(cent_x, cent_y+50)
            # pyautogui.click(cent_x, cent_y+50)
            # time.sleep(1)
            break
        print("未进入到comment页面")
        n_count += 1
        if n_count > 20:
            return
    los = pyautogui.locateOnScreen('zan.png', confidence=0.6)
    zan_y = 0
    if los is not None:
        cent_x, zan_y = pyautogui.center(los)
    last_cent_y = -1
    while last_cent_y != zan_y or zan_y == 0:
        last_cent_y = zan_y
        cent_y = 0
        female_y = 700
        female = pyautogui.locateOnScreen('female.png', confidence=0.7)
        if female is not None:
            cent_x, cent_y = pyautogui.center(female)
            print("检测到female")
            pyautogui.moveTo(cent_x, cent_y)
            time.sleep(0.5)
            click_female_icon_and_back(cent_x, cent_y)
            # 判断是否退回到comment界面
            n_count = 0
            while True:
                print("等待返回到comment界面")
                los = pyautogui.locateOnScreen('laolao.png', confidence=0.6)
                if los is not None:
                    print("返回到comment界面")
                    break
                time.sleep(1)
                n_count += 1
                if n_count > 10:
                    reset_to_tc()
                    return "timeout"
            female_y = cent_y
        # los = pyautogui.locateOnScreen("shafa.png", confidence=0.6)
        los = pyautogui.locateOnScreen("shuru.png", confidence=0.6)
        if los is not None:
            print("无人评论")
            break
        # 计算向下滑动距离
        # female_y = cent_y
        los = pyautogui.locateOnScreen('laolao.png', confidence=0.7)
        if los is not None:
            cent_x, cent_y = pyautogui.center(los)
            pyautogui.moveTo(cent_x, cent_y+50)
        else:
            print("非commetn页面，重启")
            reset_to_tc()
            # pyautogui.click(cent_x, cent_y+50)
            # time.sleep(1)
        print("滑动")

        # print(zan_y)
        cent_y = 0
        los = pyautogui.locateOnScreen('laolao.png', confidence=0.6)
        if los is not None:
            network_connection()
            cent_x, cent_y = pyautogui.center(los)
        else:
            print("错误，没有在comment界面")
            reset_to_ui("同城")
        dist_scroll = int(-abs(cent_y - female_y)*1.3)
        # pyautogui.scroll(-50)
        pyautogui.scroll(dist_scroll)
        los = pyautogui.locateOnScreen('zan.png', confidence=0.5)
        if los is not None:
            cent_x, zan_y = pyautogui.center(los)
    # print(last_cent_y)
    # print(zan_y)
    print("滑到底了")
    time.sleep(1)
    los = pyautogui.locateOnScreen('back.png', confidence=0.6)
    if los is not None:
        cent_x, cent_y = pyautogui.center(los)
        pyautogui.click(cent_x, cent_y)