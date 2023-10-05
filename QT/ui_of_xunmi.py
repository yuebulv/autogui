from qt_ui import enter_ui
from auto_gui_base import find_and_click_pic
from network import network_connection
from setting import trans_pic_name_to_path
from setting import qt_ui_region, xunmi_recommend_number


def ui_xunmi_like():
    enter_or_not = enter_ui("寻觅")
    if enter_or_not is None:
        print(f"没有找到寻觅")
        return None
    wode_pic_list = trans_pic_name_to_path("like.png")
    for i in range(xunmi_recommend_number):
        res = find_and_click_pic(wode_pic_list, click_model=1, confidence=0.8, region=qt_ui_region)
        if res is None:
            print(f"没有找到{wode_pic_list},done!")
            return True


if __name__ == '__main__':
    ui_xunmi_like()