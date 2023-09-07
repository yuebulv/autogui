import time
import datetime
import pyautogui
import setting


def qt_quit(quit_sorft=True):
    pyautogui.PAUSE = 0.5
    quit_win_list = ["qtzl_renwulan.png", "qt_renwulan.png", "qtgzh_renwulan.png", "wx_renwulan.png"]
    quit_win_list = setting.trans_pic_name_to_path(quit_win_list)
    for qui_win in quit_win_list:
        loc = pyautogui.locateOnScreen(qui_win, confidence=0.9, region=setting.win_renwulan_region)
        if loc is not None:
            x, y = pyautogui.center(loc)
            pyautogui.moveTo(x, y, duration=0.2)
            pyautogui.rightClick(pyautogui.center(loc))
            print(f"关闭{qui_win}")
            loc = pyautogui.locateOnScreen("quit_win.png", confidence=0.7, region=setting.win_renwulan_region)
            x, y = pyautogui.center(loc)
            pyautogui.moveTo(x, y, duration=0.2)
            pyautogui.click(pyautogui.center(loc))
    print(f"退出时间：{datetime.datetime.now()}")
    if quit_sorft:
        quit()


def close_win(close_win_list: list):
    # 输入，例如close_win_list = ["qtzl_renwulan.png", "qt_renwulan.png", "qtgzh_renwulan.png", "wx_renwulan.png"]
    pyautogui.PAUSE = 0.5
    quit_win_list = setting.trans_pic_name_to_path(close_win_list)
    for qui_win in quit_win_list:
        loc = pyautogui.locateOnScreen(qui_win, confidence=0.9, region=setting.win_renwulan_region)
        if loc is not None:
            x, y = pyautogui.center(loc)
            pyautogui.moveTo(x, y, duration=0.2)
            pyautogui.rightClick(pyautogui.center(loc))
            print(f"关闭{qui_win}")
            loc = pyautogui.locateOnScreen("quit_win.png", confidence=0.7, region=setting.win_renwulan_region)
            x, y = pyautogui.center(loc)
            pyautogui.moveTo(x, y, duration=0.2)
            pyautogui.click(pyautogui.center(loc))
