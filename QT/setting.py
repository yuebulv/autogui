import os
import pyautogui
# match_pic_path = r'.\pic_home'
# qt_ui_width = 512
# qt_ui_height = 980
# win_renwulan_region = [0, 930, 1920, 150]
# day_task_icon_interval_dic = {"每日签到": [360, -0], "浏览时长": [360, -0], "参与投票": [360, -0]}
# cunkou_top_icon_interval_dic = {"喜欢我的":[-70, -830], "最近来访":[70, -830], "同城": [75, -830], "推荐": [0, -830]}
# cunkou_xiaoxi_top_icon_interval_dic = {"找搭子":[- 135, -665], "相互喜欢": [135, -665]}  # 与cunkou的相对位置
# mutually_like_pic_interval_dic = {"p1": [-125, -680], "p2": [125, -680]}  # 与cunkou的相对位置
# mutually_like_me_pic_scroll_number = -375
# cunkou_icon_position = [965, 965]

win_renwulan_height = 200
qt_ui_region = [0, 0, 1920, 1080]
cunkou_bottom_icon_interval_dic = {"寻觅": [-200, 0], "喜欢": [-100, 0], "村口": [0, 0], "消息": [100, 0], "我的": [200, 0]}  # cunkou 界面底部功能图标间隔
like_me_pic_interval_dic = {"p1": [-130, -650], "p2": [130, -650]}  # 与cunkou的相对位置
like_me_pic_scroll_number = -int(285*1.02)
like_me_pic_scroll_count = 25
# person_homepage setting
day_task_scroll_number = -100
xunmi_recommend_number = 10

match_pic_path = r'.\pic_company'
qt_ui_width = 410
qt_ui_height = 780
win_renwulan_region = [0, 930, 1920, 150]
day_task_icon_interval_dic = {"每日签到": [280, -0], "浏览时长": [360, -0], "参与投票": [280, -0]}
cunkou_top_icon_interval_dic = {"喜欢我的": [-50, -665], "最近来访": [50, -665], "同城": [65, -665], "推荐": [0, -665], "加号": [145, -120]}  # 与cunkou的相对位置
cunkou_xiaoxi_top_icon_interval_dic = {"找搭子": [-125, -540], "相互喜欢": [-175, -665]}  # 与cunkou的相对位置
mutually_like_pic_interval_dic = {"p1": [-90, -550], "p2": [90, -550]}  # 与cunkou的相对位置
mutually_like_me_pic_scroll_number = -365
cunkou_icon_position = [960, 880]
comment_top_zuozelan_region = [755, 245, 405, 70]
comment_bottom_icon_interval_dic = {"分享": [30, 0], "评论": [90, 0], "赞": [150, 0]}  # cunkou 界面底部功能图标间隔
deliver_laolao_icon_interval_dic = {"匿名发布": [0, -20], "发布": [155, -20]}


# feature pic name
person_homepage_features_pic_setting = {"personal_homepage": ["xiaozhitiao.png", "guanyuwo.png"],
                                        "anonymous": "chacha.png",
                                        "stealth_in_comment": "ys_comment.png",
                                        "blank_homepage": "blank_homepage.png",
                                        "stealth_in_homepage": "back.png"}
cunkou_page_features_pic_setting = {"tc": ["tc.png", "tc_in.png"]}
restart_interval = [0, 7, 0]  # 秒，分，时


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
    if type(picnames) == str:
        picnames = [picnames]
    res = []
    for i in range(len(picnames)):
        res.append(os.path.join(match_pic_path, picnames[i]))
    return res


if __name__ == '__main__':
    res = pyautogui.position()
    print(res)

    # im = pyautogui.screenshot(region=[755, 132, 410, 780])
    # im.save((r'.\screen\2.png'))

