import time
# import datetime
import pyautogui
from auto_gui_base import find_and_click_pic
from qt_ui import enter_ui
from network import network_connection
from setting import trans_pic_name_to_path
from setting import day_task_icon_interval_dic
from setting import day_task_scroll_number
from setting import qt_ui_region
from setting import cunkou_icon_position


def get_day_qtb():
    # pyautogui.PAUSE = 0.5
    # wode_pic_list = ["wode.png", "wode_1.png", "wode_in.png", "wode_in2.png"]
    enter_or_not = enter_ui("我的")
    if enter_or_not is None:
        print(f"没有找到我的")
        return None
    time.sleep(1)
    # wode_pic_list = ["lqjl.png"]
    # res = find_and_click_pic(wode_pic_list)
    # if res is None:
    #     print(f"没有找到{wode_pic_list}")

    wode_pic_list = trans_pic_name_to_path(["ckgd.png"])
    # print(trans_pic_name_to_path(["ckgd.png"]))
    # print(f"wode_pic_list{wode_pic_list}")
    res = find_and_click_pic(wode_pic_list)
    if res is None:
        print(f"没有找到{wode_pic_list}")
        return None
    print("点击查看更多")
    time.sleep(1)

    # 循环ling bi
    last_loc = [0, 0]
    center_xy = [1, 1]
    n = 10
    while last_loc != center_xy and n > 0:
        # wode_pic_list = trans_pic_name_to_path(["lqjl_canyu.png"])
        # res = find_and_click_pic(wode_pic_list, click_model=1, confidence=0.8, region=qt_ui_region)
        # if res is not None:
        #     print("领取每日奖励")
        click_lingqujiangli()
        wode_pic_list = trans_pic_name_to_path(["cytp.png"])
        res = find_and_click_pic(wode_pic_list, coordinate_added_value=day_task_icon_interval_dic["参与投票"], click_model=1, confidence=0.8, region=qt_ui_region)
        if res is not None:
            time.sleep(1)
            wode_pic_list = trans_pic_name_to_path(["xuanxiang_a.png"])
            res = find_and_click_pic(wode_pic_list, click_model=1, confidence=0.7, region=qt_ui_region)
            if res is not None:
                wode_pic_list = trans_pic_name_to_path(["back.png"])
                res = find_and_click_pic(wode_pic_list, click_model=1, confidence=0.7, region=qt_ui_region)
        else:
            print(f"没有找到{wode_pic_list}")
            # quit()
            # return None

        x = cunkou_icon_position[0]
        y = cunkou_icon_position[1] - 100
        pyautogui.moveTo(x, y, duration=0.2)
        pyautogui.scroll(day_task_scroll_number)
        time.sleep(1)

        # 判断是否到底
        print(trans_pic_name_to_path(["quwancheng.png"])[0])
        loc = pyautogui.locateOnScreen(trans_pic_name_to_path(["quwancheng.png"])[0], confidence=0.7, region=qt_ui_region)
        if loc is not None:
            last_loc = center_xy
            center_xy = pyautogui.center(loc)
            if center_xy == last_loc:
                print("day task 滑到底了")
        else:
            print("没找到quwancheng")
        # print(n)
        # print(last_loc)
        # print(center_xy)
        n -= 1

    x = cunkou_icon_position[0]
    y = cunkou_icon_position[1] - 700
    pyautogui.moveTo(x, y, duration=0.2)
    pyautogui.click(x, y )


def click_lingqujiangli():
    while True:
        wode_pic_list = trans_pic_name_to_path(["lqjl_canyu.png"])
        res = find_and_click_pic(wode_pic_list, click_model=1, confidence=0.8, region=qt_ui_region)
        if res is not None:
            print("领取每日奖励")
        else:
            print("领取奖励完成")
            break


if __name__ == '__main__':
    get_day_qtb()