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
    if type(pic_name) != list:
        print("错误：typeerror, 要求输入列表，find_and_click_pic")
        quit()
    if coordinate_added_value is None:
        coordinate_added_value = [0, 0]
    for pic in pic_name:
        loc = pyautogui.locateOnScreen(pic, **kwargs)
        if loc is not None:
            x, y = pyautogui.center(loc)
            x1 = x + coordinate_added_value[0]
            y1 = y + coordinate_added_value[1]
            # pyautogui.moveTo(x1, y1, duration=0.2)
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
    try:
        print(f"region:", kwargs["region"])
    except:
        pass
    print(f"没找到{pic_name}")
    return None


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
    a = {"a":1, "b":2, "c":3}
    b = []
    print(type(b))
    if type(b) == list:
        print(1)