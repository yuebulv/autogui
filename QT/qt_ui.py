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
import ui_of_female
# from start import reset_to_ui


def ui_identify():
    pyautogui.moveTo(1, 1)
    re_log_on()
    tc_feature_pic_list = ['tc_in.png', 'tc_in2.png', 'tc_in3.png']
    for tc_feature_pic in tc_feature_pic_list:
        pic_path = os.path.join(match_pic_path, tc_feature_pic)
        los = pyautogui.locateOnScreen(pic_path, confidence=0.9, region=setting.qt_ui_region)
        if los is not None:
            cent_xy = pyautogui.center(los)
            tc_x, tc_y = cent_xy
            res = {"UI": "同城", "坐标": [tc_x, tc_y]}
            return res
    tc_feature_pic_list = ['tj_in.png', 'tj_in2.png', 'tj_in3.png']
    for tc_feature_pic in tc_feature_pic_list:
        pic_path = os.path.join(match_pic_path, tc_feature_pic)
        los = pyautogui.locateOnScreen(pic_path, confidence=0.9, region=setting.qt_ui_region)
        if los is not None:
            cent_xy = pyautogui.center(los)
            tc_x, tc_y = cent_xy
            res = {"UI": "推荐", "坐标": [tc_x, tc_y]}
            return res
    pic_path = os.path.join(match_pic_path, 'laolao.png')
    los = pyautogui.locateOnScreen(pic_path, confidence=0.9, region=setting.qt_ui_region)
    if los is not None:
        cent_xy = pyautogui.center(los)
        tc_x, tc_y = cent_xy
        res = {"UI": "唠唠", "坐标": [tc_x, tc_y]}
        return res
    pic_path = os.path.join(match_pic_path, 'xiaozhitiao.png')
    los = pyautogui.locateOnScreen(pic_path, confidence=0.9, region=setting.qt_ui_region)
    if los is not None:
        cent_xy = pyautogui.center(los)
        tc_x, tc_y = cent_xy
        res = {"UI": "简历", "坐标": [tc_x, tc_y]}
        return res
    return {"UI": "未知", "坐标": [0, 0]}


def click_comment_icon_and_back(icon_x, icon_y):
    # pyautogui.PAUSE = 0.5
    network_connection()
    pyautogui.moveTo(icon_x, icon_y)
    pyautogui.click(icon_x, icon_y)
    time.sleep(0.5)
    n_count = 0
    while True:
        pic_path = setting.trans_pic_name_to_path(["laolao.png"])
        los = pyautogui.locateOnScreen(pic_path[0], confidence=0.7, region=setting.qt_ui_region)
        if los is not None:
            print("检测到comment，进入comment页面")
            cent_x, cent_y = pyautogui.center(los)
            pyautogui.moveTo(cent_x, cent_y+50)
            break
        print("未进入到comment页面")
        n_count += 1
        if n_count > 20:
            return
    pic_path = setting.trans_pic_name_to_path(["zan.png"])
    los = pyautogui.locateOnScreen(pic_path[0], confidence=0.6, region=setting.qt_ui_region)
    zan_y = 0
    if los is not None:
        cent_x, zan_y = pyautogui.center(los)
    last_cent_y = -1
    while last_cent_y != zan_y or zan_y == 0:
        last_cent_y = zan_y
        cent_y = 0
        female_y = 700
        pic_path = setting.trans_pic_name_to_path(["female.png"])
        female = pyautogui.locateOnScreen(pic_path[0], confidence=0.7, region=setting.qt_ui_region)
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
                pic_path = setting.trans_pic_name_to_path(["laolao.png"])
                los = pyautogui.locateOnScreen(pic_path[0], confidence=0.6, region=setting.qt_ui_region)
                if los is not None:
                    print("返回到comment界面")
                    break
                time.sleep(1)
                n_count += 1
                if n_count > 10:
                    reset_to_ui()
                    return "timeout"
            female_y = cent_y
        # los = pyautogui.locateOnScreen("shafa.png", confidence=0.6)
        pic_path = setting.trans_pic_name_to_path(["shuru.png"])
        los = pyautogui.locateOnScreen(pic_path[0], confidence=0.6, region=setting.qt_ui_region)
        if los is not None:
            print("无人评论")
            break
        # 计算向下滑动距离
        # female_y = cent_y
        pic_path = setting.trans_pic_name_to_path(["laolao.png"])
        los = pyautogui.locateOnScreen(pic_path[0], confidence=0.7, region=setting.qt_ui_region)
        if los is not None:
            cent_x, cent_y = pyautogui.center(los)
            pyautogui.moveTo(cent_x, cent_y+50)
        else:
            print("非commetn页面，重启")
            reset_to_ui()
            # pyautogui.click(cent_x, cent_y+50)
            # time.sleep(1)
        print("滑动")

        # print(zan_y)
        cent_y = 0
        pic_path = setting.trans_pic_name_to_path(["laolao.png"])
        los = pyautogui.locateOnScreen(pic_path[0], confidence=0.6, region=setting.qt_ui_region)
        if los is not None:
            network_connection()
            cent_x, cent_y = pyautogui.center(los)
        else:
            print("错误，没有在comment界面")
            reset_to_ui("同城")
        dist_scroll = int(-abs(cent_y - female_y)*1.3)
        # pyautogui.scroll(-50)
        pyautogui.scroll(dist_scroll)
        pic_path = setting.trans_pic_name_to_path(["zan.png"])
        los = pyautogui.locateOnScreen(pic_path[0], confidence=0.5, region=setting.qt_ui_region)
        if los is not None:
            cent_x, zan_y = pyautogui.center(los)
    # print(last_cent_y)
    # print(zan_y)
    print("滑到底了")
    time.sleep(1)
    pic_path = setting.trans_pic_name_to_path(["back.png"])
    los = pyautogui.locateOnScreen(pic_path[0], confidence=0.6, region=setting.qt_ui_region)
    if los is not None:
        cent_x, cent_y = pyautogui.center(los)
        network_connection()
        pyautogui.click(cent_x, cent_y)


def click_female_icon_and_back(icon_x, icon_y, features_pic=["xiaozhitiao.png"]):
    ui_of_female.click_female_icon_and_back(icon_x,icon_y)


def reset_to_ui(ui="同城"):
    # 重置到同城
    qt_beep()
    re_log_on()
    ui_list = ["关注", "推荐", "同城"]
    ui_pic_dic = {"同城": "tc.png", "推荐": "tj.png", "关注": "guanzhu_ui.png"}
    if ui in ui_list:
        pass
    else:
        res = {"UI": "输入ui不在列表中", "坐标": [0, 0]}
    print(f"重置到{ui}界面")
    n = 0
    while True:
        pyautogui.moveTo(1, 1)
        time.sleep(1)
        pic_path = setting.trans_pic_name_to_path(["back.png"])
        find_and_click_pic(pic_path, confidence=0.7, region=setting.qt_ui_region)
        # los = pyautogui.locateOnScreen(pic_path, confidence=0.7, region=setting.qt_ui_region)
        # if los is not None:
        #     cent_x, cent_y = pyautogui.center(los)
        #     network_connection()
        #     pyautogui.click(cent_x, cent_y)
        pic_path = setting.trans_pic_name_to_path([ui_pic_dic[ui]])
        los_tc = pyautogui.locateOnScreen(pic_path[0], confidence=0.7, region=setting.qt_ui_region)
        if los_tc is not None:
            cent_x, cent_y = pyautogui.center(los_tc)
            network_connection()
            pyautogui.click(cent_x, cent_y)
            res = {"UI": ui, "坐标": [cent_x, cent_y]}
            return res
        res = ui_identify()
        if res['UI'] == ui:
            return res
        n += 1
        if n > 20:
            print(f"无法重置到{ui}界面")
            return res


def enter_ui(ui_name):
    # 进入cunkou
    icunkou_bottom_icon_interval_dic = setting.cunkou_bottom_icon_interval_dic
    try:
        icon_interval: list = icunkou_bottom_icon_interval_dic[ui_name]
    except KeyError:
        print("不是cunkou ui")
        qt_quit()
    cunkou_settings = setting.ui_cunkou_setting()
    cunkou_pic: list = cunkou_settings["icon_cunkou_pic"] + cunkou_settings["icon_cunkou_in_pic"]
    # cunkou_pic.append(cunkou_settings["icon_cunkou_in_pic"])
    network_connection()
    print(cunkou_pic)
    status = find_and_click_pic(cunkou_pic, icon_interval, click_model=1, confidence=0.7, region=setting.qt_ui_region)
    if status is not None:
        print(f"已点击，等待进入{ui_name}页面")
        return "enter"
    return None


def ui_like_traverse():
    enter_status = enter_ui("喜欢")
    if enter_status is None:
        print("未进入like页面")
        return None
    cunkou_top_icon_interval_dic = setting.cunkou_top_icon_interval_dic
    try:
        icon_interval: list = cunkou_top_icon_interval_dic["喜欢我的"]
    except KeyError:
        print("KeyError")
        return None
    cunkou_icon_position = setting.cunkou_icon_position
    x = cunkou_icon_position[0]+icon_interval[0]
    y = cunkou_icon_position[1]+icon_interval[1]
    network_connection()
    print("进入like页面")
    pyautogui.click(x, y)

    # traverse
    female_position = [i for i in setting.like_me_pic_interval_dic.values()]
    # y = setting.cunkou_icon_position[1]-100
    # pyautogui.moveTo(setting.cunkou_icon_position[0], y, duration=0.2)
    # time.sleep(1)
    # pyautogui.scroll(-90)
    n = setting.like_me_pic_scroll_count
    while True and n > 0:
        network_connection()
        for position in female_position:
            # pyautogui.moveTo(setting.cunkou_icon_position[0], setting.cunkou_icon_position[1], duration=1)
            # print(position)
            x = position[0] + setting.cunkou_icon_position[0]
            y = position[1] + setting.cunkou_icon_position[1]
            # print(x, y)
            pyautogui.moveTo(x, y, duration=0.2)
            # time.sleep(0.5)
            click_female_icon_and_back(x, y, features_pic=["lt_likeme.png"])
        pyautogui.moveTo(x, y, duration=0.2)
        pyautogui.scroll(setting.like_me_pic_scroll_number)
        n -= 1


def ui_mutually_like_traverse():
    enter_status = enter_ui("消息")
    if enter_status is None:
        print("未进入消息页面")
        return None
    cunkou_top_icon_interval_dic = setting.cunkou_xiaoxi_top_icon_interval_dic
    try:
        icon_interval: list = cunkou_top_icon_interval_dic["相互喜欢"]
    except KeyError:
        print("KeyError")
        return None
    cunkou_icon_position = setting.cunkou_icon_position
    x = cunkou_icon_position[0] + icon_interval[0]
    y = cunkou_icon_position[1] + icon_interval[1]
    print("mutually-like页面")
    network_connection()
    pyautogui.click(x, y)
    time.sleep(1)

    # traverse
    female_position = [i for i in setting.like_me_pic_interval_dic.values()]
    last_female_position = [0, 0]
    now_female_position = [1, 1]
    # n = setting.mutually_like_me_pic_scroll_count
    while last_female_position != now_female_position:
        pic_path = setting.trans_pic_name_to_path(["female.png"])
        los = pyautogui.locateOnScreen(pic_path[0], confidence=0.6, region=setting.qt_ui_region)  # 输入框状态
        if los is not None:
            now_female_position = pyautogui.center(los)
        network_connection()
        for position in female_position:
            # pyautogui.moveTo(setting.cunkou_icon_position[0], setting.cunkou_icon_position[1], duration=1)
            # print(position)
            x = position[0] + setting.cunkou_icon_position[0]
            y = position[1] + setting.cunkou_icon_position[1]
            # print(x, y)
            pyautogui.moveTo(x, y, duration=0.2)
            # time.sleep(0.5)
            click_female_icon_and_back(x, y, features_pic=["lt_likeme.png"])
        pyautogui.moveTo(x, y, duration=0.2)
        pyautogui.scroll(setting.mutually_like_me_pic_scroll_number)
        last_female_position = now_female_position
        los = pyautogui.locateOnScreen(pic_path[0], confidence=0.6, region=setting.qt_ui_region)  # 输入框状态
        if los is not None:
            now_female_position = pyautogui.center(los)
    pic_path = setting.trans_pic_name_to_path(["back.png"])
    network_connection()
    find_and_click_pic(pic_path, click_model=1, confidence=0.7, region=setting.qt_ui_region)
    print("mutually_like_traverse done")


if __name__ == '__main__':
    ui_mutually_like_traverse()

    # for i in range(40):
    #     pyautogui.moveTo(843, 286, duration=0.2)
    #     pyautogui.scroll(-375)
    #     time.sleep(0.5)
    #     print(i)
