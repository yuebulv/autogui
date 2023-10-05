import time
import datetime
import pyautogui
import setting
import os
from log_on import re_log_on as re_log_on
from setting import match_pic_path
from auto_gui_base import find_and_click_pic
from network import network_connection
from quit_qt import qt_quit
from music import qt_beep


def click_female_icon_and_back(icon_x, icon_y):
    re_log_on()
    pyautogui.PAUSE = 0.5
    pic_path = setting.trans_pic_name_to_path(["shuru.png"])
    los = pyautogui.locateOnScreen(pic_path[0], confidence=0.6, region=setting.qt_ui_region)  # 输入框状态
    if los is not None:
        pyautogui.click(icon_x, icon_y)
    print('点击female')
    network_connection()
    pyautogui.click(icon_x, icon_y)  # 进入主页
    homepageType = "blank_homepage"
    while homepageType == "blank_homepage":
        homepageType = personal_homepage_type()["ui_type"]
        network_connection(60, 2)

    if homepageType == "personal_homepage":
        print("进入到female页面")
        pic_path = setting.trans_pic_name_to_path(['back.png'])
        exit_or_not = find_and_click_pic(pic_path, confidence=0.7, region=setting.qt_ui_region)
        return
    if homepageType == "anonymous":
        print("匿名用户")
        pic_path = setting.trans_pic_name_to_path(['chacha.png'])
        exit_or_not = find_and_click_pic(pic_path, confidence=0.7, region=setting.qt_ui_region)
        return
    if homepageType == "stealth_in_comment":
        print("对方开启隐身")
        pic_path = setting.trans_pic_name_to_path(['back.png'])
        exit_or_not = find_and_click_pic(pic_path, confidence=0.7, region=setting.qt_ui_region)
        return
    if homepageType == "stealth_in_homepage":
        print("隐身用户")
        time.sleep(3)
        pic_path = setting.trans_pic_name_to_path(['back.png'])
        exit_or_not = find_and_click_pic(pic_path, confidence=0.7, region=setting.qt_ui_region)
        # im = pyautogui.screenshot(region=setting.qt_ui_region)
        # im.save(r'.\screen\隐身用户.png')
        return
    print(homepageType)
    # im = pyautogui.screenshot(region=setting.qt_ui_region)
    # im.save(f'.\screen\{homepageType}.png')
    # quit()


def personal_homepage_type():
    network_connection()
    for homepage_type in setting.person_homepage_features_pic_setting:
        pic_name = setting.person_homepage_features_pic_setting[homepage_type]
        pic_path = setting.trans_pic_name_to_path(pic_name)
        exit_or_not = find_and_click_pic(pic_path, click_model=0, confidence=0.6, region=setting.qt_ui_region)
        if exit_or_not is not None:
            if homepage_type == "stealth_in_homepage":
                qt_beep()
                # quit()
            print(f"页面{homepage_type}")
            return {"ui_type": homepage_type}
    print("ui_of_female personal_homepage_type发生错误")
    quit()
    return {"ui_type": "未知页面"}
