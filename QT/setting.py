import os
import pyautogui
# match_pic_path = r'.\pic_home'
match_pic_path = r'.\pic_company'
qt_ui_width = 512
qt_ui_height = 970
win_renwulan_height = 200
qt_ui_region = [0, 0, 1920, 1080]
win_renwulan_region = [0, 900, 1920, 150]
cunkou_bottom_icon_interval_dic = {"寻觅":[-200, 0], "喜欢":[-100, 0], "村口":[0, 0], "消息":[100, 0], "我的":[200, 0]}  # cunkou 界面底部功能图标间隔
cunkou_top_icon_interval_dic = {"喜欢我的":[-70, -830], "最近来访":[70, -830]}
cunkou_icon_position = [965, 965]
like_me_pic_interval_dic = {"p1": [-130, -650], "p2": [130, -650]}
like_me_pic_scroll_number = -int(285*1.02)
like_me_pic_scroll_count = 25
day_task_icon_interval_dic = {"每日签到": [360, -0], "浏览时长": [360, -0], "参与投票": [360, -0]}
day_task_scroll_number = -100
# ui_features_pic_dic = {"寻觅":[-200, 0],
#                        "喜欢":[-100, 0],
#                        "村口":[0, 0],
#                        "消息":[100, 0],
#                        "我的":[200, 0]}


def get_qt_ui_region():
    # 获得qt界面region
    pic_path = os.path.join(match_pic_path, "qt_ui_top.png")
    # print(pic_path)
    loc = pyautogui.locateOnScreen(pic_path, confidence=0.9)  # 路径中不能存在中文，否则识别不了
    if loc is not None:
        left, top, width, height = loc
        width = qt_ui_width
        height = qt_ui_height
        global qt_ui_region
        qt_ui_region = [left, top, width, height]
        print("获得qt区域位置")
        return qt_ui_region
    return None


def get_win_renwulan_region():
    screen_size = pyautogui.size()
    width, height = screen_size
    global win_renwulan_region
    win_renwulan_region = [0, height-win_renwulan_height, width, win_renwulan_height]
    return win_renwulan_region


def ui_like_setting():
    icon_like_pic = ['like_2.png', 'like_1.png']
    icon_like_in_pic = ['like_in.png']
    icon_like_pic = trans_pic_name_to_path(icon_like_pic)
    icon_like_in_pic = trans_pic_name_to_path(icon_like_in_pic)

    res = {"icon_like_pic": icon_like_pic, "icon_like_in_pic": icon_like_in_pic}
    return res


def ui_cunkou_setting():
    # global icon_cunkou_pic, icon_cunkou_in_pic
    icon_cunkou_pic = ['cunkou.png', 'cunkou_2.png']
    icon_cunkou_in_pic = ['cunkou_in.png']
    icon_cunkou_pic = trans_pic_name_to_path(icon_cunkou_pic)
    icon_cunkou_in_pic = trans_pic_name_to_path(icon_cunkou_in_pic)
    res = {"icon_cunkou_pic": icon_cunkou_pic, "icon_cunkou_in_pic": icon_cunkou_in_pic}
    return res


def trans_pic_name_to_path(picnames: list):
    res = []
    for i in range(len(picnames)):
        res.append(os.path.join(match_pic_path, picnames[i]))
    return res


if __name__ == '__main__':
    # region_qt = get_qt_ui_region()
    # # im1 = pyautogui.screenshot("shot.png", region=(705, 30, 512, 970))
    # print(region_qt)
    # pic_path = os.path.join(match_pic_path, "cunkou_in.png")
    # loc = pyautogui.locateOnScreen(pic_path, confidence=0.7, region=region_qt)  # 路径中不能存在中文，否则识别不了
    # if loc is not None:
    #     x, y = pyautogui.center(loc)
    #     pyautogui.moveTo(x, y, duration=1)
    # else:
    #     print("没找到")

    # region_qt = get_win_renwulan_region()
    # im1 = pyautogui.screenshot("shot.png", region=region_qt)
    # icon_like_pic = ['like_2.png', 'like_1.png']
    # res = trans_pic_name_to_path(icon_like_pic)
    # print(res)

    res = pyautogui.position()
    print(res)

    # like_me_pic_interval_dic = {"p1": [-230, -560], "p2": [230, 560]}
    # res = like_me_pic_interval_dic.values()
    # r = [i for i in res]
    # print(r)