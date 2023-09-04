import pyautogui
import time
import setting as setting


def test():
    print(pyautogui.position())
    pyautogui.scroll(300, x=706, y=380)
    # time.sleep(3)
    # print(pyautogui.position())
    # pyautogui.press('enter')  # press the Enter key
    # im2 = pyautogui.screenshot('my_screenshot.png')
    # im = pyautogui.screenshot(region=(0, 0, 300, 400))
    # x, y = pyautogui.locateCenterOnScreen('calc7key.png')
    # for pos in pyautogui.locateAllOnScreen('someButton.png'):
    #     print(pos)
    # pyautogui.locateOnScreen('someButton.png', region=(0, 0, 300, 400))


if __name__ == '__main__':
    # test()
    print(setting.match_pic_path)