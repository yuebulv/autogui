from setting import trans_pic_name_to_path, qt_ui_region, cunkou_page_features_pic_setting
from auto_gui_base import find_and_click_pic


def enter_ui(ui_name) -> bool:
    # 从cunkou进入下个ui
    try:
        pic_path = cunkou_page_features_pic_setting[ui_name]
    except KeyError:
        print(f"输入的key{ui_name}，cunkou_page_features_pic_setting中没有")
        return False
    pic_path = trans_pic_name_to_path(pic_path)
    enter = find_and_click_pic(pic_path, confidence=0.7, region=qt_ui_region)
    if enter is not None:
        print(f"进入{ui_name}")
        return True
    else:
        print(f"未能进入{ui_name}")
        return False
