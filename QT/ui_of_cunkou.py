from setting import trans_pic_name_to_path, qt_ui_region, cunkou_page_features_pic_setting, cunkou_top_icon_interval_dic, cunkou_icon_position, deliver_laolao_icon_interval_dic
from auto_gui_base import find_and_click_pic
import pyautogui
import time
from network import network_connection
import pyperclip


def enter_ui(ui_name) -> bool:
    # 从cunkou进入下个ui
    # 判断是否在cuokou
    # 查找相对位置
    # if ui_name in cunkou_bottom_icon_interval_dic:

    # 查找features_pic
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


def deliver_laolao(textLaolao, anonymous=False):
    '''
    :param textLaolao: 唠唠内容
    :param anonymous: 是否匿名发唠唠
    :return:
    '''
    pyautogui.click(cunkou_icon_position[0], cunkou_icon_position[1], duration=0.2)
    x = cunkou_icon_position[0] + cunkou_top_icon_interval_dic["加号"][0]
    y = cunkou_icon_position[1] + cunkou_top_icon_interval_dic["加号"][1]
    pyautogui.click(x, y, duration=0.2)

    pic_path = trans_pic_name_to_path("nimingfabu.png")[0]
    n = 0
    while True and n < 10:
        network_connection()
        los = pyautogui.locateOnScreen(pic_path, confidence=0.9, region=qt_ui_region)
        if los is not None:
            print(textLaolao)
            pyperclip.copy(textLaolao)
            # pyautogui.click(x, y)
            pyautogui.hotkey('ctrl', 'v')
            if anonymous:
                x = cunkou_icon_position[0] + deliver_laolao_icon_interval_dic["匿名发布"][0]
                y = cunkou_icon_position[1] + deliver_laolao_icon_interval_dic["匿名发布"][1]
                pyautogui.click(x, y, duration=0.2)
            break
        n += 1
    x = cunkou_icon_position[0] + deliver_laolao_icon_interval_dic["发布"][0]
    y = cunkou_icon_position[1] + deliver_laolao_icon_interval_dic["发布"][1]
    pyautogui.click(x, y, duration=0.2)
    print("发布成功")


def get_laola_text(txtpath='laolao.txt'):
    today = time.strftime('%m-%d', time.localtime(time.time()))
    txtpath = 'laolao.txt'
    with open(txtpath, 'r', encoding="utf-8") as file:
        laolao_txt_lines = file.readlines()
    for txt_line in laolao_txt_lines:
        txt_line_list = txt_line.split(" ", 1)
        # print(txt_line_list)
        if txt_line_list[0] == today:
            # print(txt_line_list[1])
            return txt_line_list[-1]
    return "发错了"


def fabu_laolao():
    text = get_laola_text()
    deliver_laolao(text, anonymous=False)