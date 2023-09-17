import pyautogui
import os
import time
import setting
from setting import match_pic_path as match_pic_path
from auto_gui_base import find_and_click_pic


def re_log_on():
    # 重新登录wx
    pic_path = os.path.join(match_pic_path, "cxdl.png")
    loc = pyautogui.locateOnScreen(pic_path, confidence=0.7, region=setting.qt_ui_region)
    if loc is not None:
        time.sleep(30)
        cent_xy = pyautogui.center(loc)
        pyautogui.click(cent_xy)
    pic_path = os.path.join(match_pic_path, "wx_pic_renwulan.png")
    find_and_click_pic(pic_path, confidence=0.7, region=setting.win_renwulan_region)