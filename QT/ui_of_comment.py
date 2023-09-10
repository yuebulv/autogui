import pyautogui
from setting import trans_pic_name_to_path, comment_top_zuozelan_region, cunkou_icon_position, comment_bottom_icon_interval_dic
# from auto_gui_base import find_and_click_pic
from auto_gui_base import if_pics_in_region


def zan_female_comment():
    pics = ["female.png", "guanzhu.png"]
    pics = trans_pic_name_to_path(pics)
    region = comment_top_zuozelan_region
    res = if_pics_in_region(pics, region)
    print(res)
    # im = pyautogui.screenshot(region=region)
    # im.save(r'.\screen\comment_zuozelan.png')
    if res["all_exist"]:
        x = cunkou_icon_position[0] + comment_bottom_icon_interval_dic["赞"][0]
        y = cunkou_icon_position[1] + comment_bottom_icon_interval_dic["赞"][1]
        pyautogui.moveTo(x, y, duration=0.2)
        pyautogui.click(x, y)


if __name__ == '__main__':
    zan_female_comment()

