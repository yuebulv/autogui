import pyautogui
import time
import os
import setting
from setting import match_pic_path as match_pic_path
from music import qt_beep as qt_beep
from qt_ui import ui_identify as ui_identify
from log_on import re_log_on as re_log_on
from network import network_connection
import quit_qt
from auto_gui_base import find_and_click_pic
import copy


def restart_qt(close_qtzl=True):
    # 重启qt
    qt_beep()
    re_log_on()
    if close_qtzl == True:
        # close_win_list = ["qtzl_renwulan.png"]
        quit_qt.close_win(["qtzl_renwulan.png"])

        # pic_path = os.path.join(match_pic_path, "qt_renwulan.png")
        # for i in range(2):
        #     res = find_and_click_pic([pic_path], confidence=0.7, region=setting.win_renwulan_region)
        #     if res is None:
        #         print("没找到qt_renwulan.png，无法从qt_fuwuhao启动")
        #         quit_qt.qt_quit()
        #         # start_qt()
        #     else:
        #         time.sleep(0.5)
        #         pic_path = os.path.join(match_pic_path, "qt_zdx.png")
        #         loc = pyautogui.locateOnScreen(pic_path, confidence=0.7, region=setting.qt_ui_region)
        #         if loc is None:
        #             print("没找到zdx,重启失败")
        #         else:
        #             cent_xy = pyautogui.center(loc)
        #             network_connection()
        #             pyautogui.click(cent_xy)
        #             break

    for i in range(3):
        pic_path = os.path.join(match_pic_path, "qt_zdx.png")
        region_zdx = copy.deepcopy(setting.qt_ui_region)
        region_zdx[0] = max(region_zdx[0]-30, 0)
        print(region_zdx)
        loc_zdx = find_and_click_pic([pic_path], confidence=0.7, region=region_zdx)
        if loc_zdx is not None:
            print("找到zdx.png")
            break
        pic_path = os.path.join(match_pic_path, "qt_renwulan.png")
        loc = find_and_click_pic([pic_path], confidence=0.7, region=setting.win_renwulan_region)
        if loc is None:
            print("没找到qt_renwulan.png，无法从qt_fuwuhao启动，退出程序")
            im = pyautogui.screenshot(region=setting.qt_ui_region)
            im.save(r'.\screen\没找到qt_renwulan.png')
            quit_qt.qt_quit()
    if loc_zdx is None:
        im = pyautogui.screenshot(region=setting.qt_ui_region)
        im.save(r'.\screen\没找到zdx.png')
        quit_qt.qt_quit()

        # pic_path = os.path.join(match_pic_path, "quit.png")
        # loc = pyautogui.locateOnScreen(pic_path, confidence=0.7, region=setting.qt_ui_region)
        # if loc is None:
        #     print("没找到退出按钮，重启失败")
        #     quit()
        # else:
        #     print("退出qt")
        #     pyautogui.click(pyautogui.center(loc))
        # pic_path = os.path.join(match_pic_path, "qt_renwulan.png")
        # loc = pyautogui.locateOnScreen(pic_path, confidence=0.7, region=setting.win_renwulan_region)
        # if loc is None:
        #     print("重启失败1")
        #     quit()
        # cent_rwl = pyautogui.center(loc)
        # cent_x, cent_y = cent_rwl
        # pyautogui.moveTo(cent_x, cent_y, duration=2)
        # pyautogui.click(cent_rwl)


    # if close_qtzl == True:
    #     pyautogui.click(cent_rwl)
    time.sleep(2)
    network_connection()
    setting.get_qt_ui_region()
    print(f"初始region：{setting.qt_ui_region}")
    cunkou_pic_list = ['cunkou_in.png', 'cunkou_in2.png', 'cunkou.png', 'cunkou_2.png']
    for conkou_pic in cunkou_pic_list:
        pic_path = os.path.join(match_pic_path, conkou_pic)
        print(f"click cunkou region：{setting.qt_ui_region}")
        loc = pyautogui.locateOnScreen(pic_path, confidence=0.7, region=setting.qt_ui_region)
        time.sleep(2)
        if loc is not None:
            print("进入cunkou")
            x, y = pyautogui.center(loc)
            setting.cunkou_icon_position = [x, y]
            pyautogui.moveTo(x, y, duration=0.2)
            pyautogui.click(pyautogui.center(loc))
            break
        else:
            print("没找到cunkou")
    if loc is None:
        im = pyautogui.screenshot(region=setting.qt_ui_region)
        im.save(r'.\screen\没找到cunkou.png')
        quit_qt.qt_quit()
    n = 5
    while n > 0:
        res = ui_identify()
        if res["UI"] == "推荐":
            print("重启qt成功")
            time.sleep(1)
            # click_win_min({"qt_renwulan.png": "qt_zxh.png", "qtgzh_renwulan.png": "qt_gzh_zxh.png", "wx_renwulan.png": "qt_zxh.png"})
            return res
        time.sleep(1)
        n -= 1


def start_qt():
    win_renwulan_region = setting.get_win_renwulan_region()
    pyautogui.PAUSE = 0.5
    pyautogui.moveTo(1, 1)
    pic_path = os.path.join(match_pic_path, "wx_renwulan.png")
    loc_wx_renwulan = pyautogui.locateOnScreen(pic_path, confidence=0.7, region=win_renwulan_region)
    if loc_wx_renwulan is not None:
        pyautogui.click(pyautogui.center(loc_wx_renwulan))
    else:
        pic_path = os.path.join(match_pic_path, "kuozhan_rwl.png")
        loc = pyautogui.locateOnScreen(pic_path, confidence=0.7, region=win_renwulan_region)
        if loc is not None:
            pyautogui.click(pyautogui.center(loc))
            pic_path = os.path.join(match_pic_path, "wx_in_kuozhan.png")
            loc = pyautogui.locateOnScreen(pic_path, confidence=0.7, region=win_renwulan_region)
            if loc is not None:
                pyautogui.click(pyautogui.center(loc))
            else:
                print("任务栏没有启动微信")
                quit()
        else:
            print("没找到任务栏扩展按钮")
            quit()
    wx_txl_ico = ["wx_txl.png", "wx_txl_in.png"]
    for wx_txl in wx_txl_ico:
        pic_path = os.path.join(match_pic_path, wx_txl)
        loc = pyautogui.locateOnScreen(pic_path, confidence=0.7)
        if loc is not None:
            pyautogui.click(pyautogui.center(loc))
            print("找到微信通讯录")
            break
    if loc is None:
        print("没找到微信通讯录")
        quit()
    wx_gzh_ico = ["wx_gzh.png", "wx_gzh_in.png"]
    for wx_gzh in wx_gzh_ico:
        pic_path = os.path.join(match_pic_path, wx_gzh)
        loc = pyautogui.locateOnScreen(pic_path, confidence=0.7)
        if loc is not None:
            gzc_x, gzc_y = pyautogui.center(loc)
            pyautogui.click(pyautogui.center(loc))
            print("找到微信公众号")
            break
    if loc is None:
        print("没找到微信公众号")
        quit()
    n = 0
    pyautogui.moveTo(gzc_x+250, gzc_y)
    while True and n < 30:
        pic_path = os.path.join(match_pic_path, "wx_qt.png")
        loc = pyautogui.locateOnScreen(pic_path, confidence=0.9)
        if loc is not None:
            print("点击qt公众号")
            pyautogui.click(pyautogui.center(loc))
            time.sleep(1)
            pic_path = os.path.join(match_pic_path, "qt_gzh_fxx.png")
            loc = pyautogui.locateOnScreen(pic_path, confidence=0.7)
            if loc is not None:
                print("进入qt公众号")
                time.sleep(1)
                pyautogui.click(pyautogui.center(loc))
                restart_qt(close_qtzl=False)
                return
            else:
                print("没找到发消息按钮")
                quit()
        else:
            print("没找到qt按钮")
            pyautogui.scroll(-300)
            time.sleep(1)
        n += 1


# def reset_to_ui(ui="同城"):
#     # 重置到同城
#     qt_beep()
#     re_log_on()
#     ui_list = ["关注", "推荐", "同城"]
#     ui_pic_dic = {"同城": "tc.png", "推荐": "tj.png", "关注": "guanzhu_ui.png"}
#     if ui in ui_list:
#         pass
#     else:
#         res = {"UI": "输入ui不在列表中", "坐标": [0, 0]}
#     print(f"重置到{ui}界面")
#     n = 0
#     while True:
#         pyautogui.moveTo(1, 1)
#         time.sleep(1)
#         pic_path = os.path.join(match_pic_path, "back.png")
#         los = pyautogui.locateOnScreen(pic_path, confidence=0.7, region=setting.qt_ui_region)
#         if los is not None:
#             cent_x, cent_y = pyautogui.center(los)
#             pyautogui.click(cent_x, cent_y)
#         pic_path = os.path.join(match_pic_path, ui_pic_dic[ui])
#         los_tc = pyautogui.locateOnScreen(pic_path, confidence=0.7, region=setting.qt_ui_region)
#         if los_tc is not None:
#             cent_x, cent_y = pyautogui.center(los_tc)
#             pyautogui.click(cent_x, cent_y)
#             res = {"UI": ui, "坐标": [cent_x, cent_y]}
#             return res
#         res = ui_identify()
#         if res['UI'] == ui:
#             return res
#         n += 1
#         if n > 20:
#             print(f"无法重置到{ui}界面")
#             return res


def test():
    res = setting.get_qt_ui_region()


if __name__ == '__main__':
    start_qt()
    # region_renwulan = setting.get_win_renwulan_region()
    # print(f"region_renwulan{region_renwulan}")
    # region_qt = setting.get_qt_ui_region()
    # print(f"region_qt{region_qt}")
    # print(setting.qt_ui_region)
    # print(setting.win_renwulan_region)
    # im1 = pyautogui.screenshot("shot.png", region=region_qt)