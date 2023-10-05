import pyautogui
from network import network_connection


def find_and_click_pic(pic_name: list, coordinate_added_value=None, click_model=1, **kwargs):
    # 功能查找到照片，并点击
    '''
    pic_name: 要查找按钮对应路径，按钮有不同形态，放到一个list里
    coordinate_added_value: 点击照片时，点击位置x,y附加的值
    click_model: 0时不点击，1鼠标左键单击，2鼠标右键单击
    '''
    # 返回查找图标坐标
    if type(pic_name) == str:
        pic_name = [pic_name]
    if type(pic_name) != list:
        print("错误：typeerror, 要求输入列表，find_and_click_pic")
        quit()
    if coordinate_added_value is None:
        coordinate_added_value = [0, 0]
    for pic in pic_name:
        try:
            loc = pyautogui.locateOnScreen(pic, **kwargs)
        except ValueError as er:  ################################# 删除
            print(er, kwargs)
            quit()
        if loc is not None:
            x, y = pyautogui.center(loc)
            x1 = x + coordinate_added_value[0]
            y1 = y + coordinate_added_value[1]
            # pyautogui.moveTo(x1, y1, duration=0.2)
            print(f"找到{pic_name}")
            if click_model == 1:
                network_connection()
                print(f"左击:{pic_name}")
                pyautogui.moveTo(x1, y1, duration=0.5)
                pyautogui.click(x1, y1)
            elif click_model == 2:
                network_connection()
                print(f"右击:{pic_name}")
                pyautogui.moveTo(x1, y1, duration=0.5)
                pyautogui.rightClick(x1, y1)
            return {"坐标": [x, y]}
    # print(kwargs)
    # try:
    #     pyautogui.screenshot(".\screen\shot.png", region=kwargs["region"])
    # except KeyError:
    #     pass
    print(f"没找到{pic_name}")
    try:
        region = kwargs["region"]
    except:
        print("无region")
    else:
        im = pyautogui.screenshot(region=region)
        fileneame = str(pic_name)
        # fileneame = fileneame.replace(r'\', '').replace(".", "").replace('[', "").replace("]", "")
        # im.save(f'.\screen\{1}.png')
    return None


def if_pics_in_region(pics, find_region):
    '''
    # 判断区域内是否存在pics
    :param pics: 照片path；可以是List，可以是str
    :param region: 要在屏幕是查找的区域
    :return: {"all_exist": True or False, "every_coordinate": [[x, y], None]}
    '''
    if type(pics) == str:
        pics = [pics]
    all_exist = True
    pics_coordinate = []
    for pic in pics:
        exist_or_not = find_and_click_pic(pic, confidence=0.7, click_model=0, region=find_region)
        pics_coordinate.append(exist_or_not)
        if exist_or_not is None:
            pics_coordinate.append(exist_or_not)
            all_exist = False
        else:
            pics_coordinate.append(exist_or_not["坐标"])
    res = {"all_exist": all_exist, "every_coordinate": pics_coordinate}
    return res


def qt_beep(n=3):
    import winsound
    duration = 1000  # millisecond
    freq = 440  # Hz
    for i in range(n):
        winsound.Beep(freq, duration)


def test(*args, **kwargs):
    print(args)
    print(kwargs)


if __name__ == '__main__':
    a = [1, 2]
    # a = '1'
    find_and_click_pic(a)
    if type(a) == list:
        print("list")
    elif type(a) == str:
        print(2)