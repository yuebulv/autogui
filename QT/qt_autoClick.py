import pyautogui
from tkinter import *
import tkinter as tk
import time


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('自动点播放按钮')
        self.lbl = tk.Label(self,
                            text='刷新时间(s)：',
                            padx=0,
                            pady=0)
        # self.lbl.pack()
        self.lbl.grid(row=0, column=2, stick=EW)
        self.txt = tk.Text(self, width=5, height=1)
        # self.txt.pack()
        self.txt.grid(row=0, column=3, stick=EW)
        self.txt.insert(INSERT, '20')
        self.status_text = '状态'
        self.lbl2 = tk.Label(self,
                             text=self.status_text)
        # self.lbl2.pack()
        self.lbl2.grid(row=1, column=2, columnspan=2)
        self.button = tk.Button(self,
                                text='退出',
                                width=10,
                                command=self.quit)
        self.button.grid(row=2, column=2, columnspan=2)
        # self.update_auto()
        self.click_female_in_comment_auto()

    # def update_auto(self):
    #     los = pyautogui.locateOnScreen('female.png', confidence=0.6)
    #     if los is not None:
    #         cent_xy = pyautogui.center(los)
    #         # pyautogui.click(cent_xy)
    #         cent_x, female_y = cent_xy
    #         cent_x_last, cent_y_last = cent_x, female_y
    #         # Point(x=400, y=860)
    #         pyautogui.click(cent_x, female_y)
    #         self.status_text = '匹配到female按钮，点击'
    #         # pyautogui.PAUSE = 0.5
    #         time.sleep(1)
    #         los = pyautogui.locateOnScreen('back.png', confidence=0.6)
    #         if los is not None:
    #             cent_xy = pyautogui.center(los)
    #             cent_x, cent_y = cent_xy
    #             pyautogui.click(cent_x, cent_y)
    #         else:  # 匿名用户
    #             los = pyautogui.locateOnScreen('chacha.png', confidence=0.6)
    #             if los is not None:
    #                 cent_xy = pyautogui.center(los)
    #                 cent_x, cent_y = cent_xy
    #                 pyautogui.click(cent_x, cent_y)
    #             else:  # 隐身用户
    #                 pyautogui.click(cent_x-130, female_y)
    #         pyautogui.moveTo(cent_x_last, cent_y_last)
    #         # 计算向下滑动距离
    #         cent_y = 0
    #         los = pyautogui.locateOnScreen('tj.png', confidence=0.6)
    #         if los is not None:
    #             cent_x, cent_y = pyautogui.center(los)
    #         dist_scroll = int(cent_y - female_y)
    #         print(dist_scroll)
    #         pyautogui.scroll(dist_scroll)
    #         # pyautogui.scroll(-462)
    #     else:
    #         pyautogui.scroll(-700)
    #         self.status_text = '没有匹配female，正在播放'+time.strftime("%H:%M:%S", time.localtime())
    #         im = pyautogui.screenshot()
    #         im.save(r'.\screen\截屏.png')
    #     # pyautogui.moveTo(random.randint(0, 100), random.randint(0, 100))
    #     self.lbl2.config(text=self.status_text)
    #     self.after(int(self.txt.get('1.0', END))*1000, self.update_auto)

    def click_female_in_comment_auto(self):
        los = pyautogui.locateOnScreen('comment.png', confidence=0.9)
        if los is not None:
            cent_x, comment_y = pyautogui.center(los)
            self.status_text = '匹配到comment按钮，点击'
            # cent_x_last, cent_y_last = cent_x, female_y
            # Point(x=400, y=860)
            print("点击comment按钮")
            pyautogui.moveTo(cent_x, comment_y, duration=0.2)
            # time.sleep(1)
            click_comment_icon_and_back(cent_x, comment_y)
            # pyautogui.PAUSE = 0.5
            print("该comment完成，进行下一个comment")
            # time.sleep(1)
            # pyautogui.moveTo(cent_x_last, cent_y_last)

            # 计算向下滑动距离
            ui = ui_identify()
            if ui["UI"] == "同城":
                cent_x, cent_y = ui["坐标"][0], ui["坐标"][1]
                print("移动鼠标到tc下方")
                pyautogui.moveTo(cent_x, cent_y+100, duration=0.2)
                # time.sleep(1)
            else:
                print("不是tc页面")
                reset_to_tc()
                # quit()

            # cent_y = 0
            # los = pyautogui.locateOnScreen('tj.png', confidence=0.5, grayscale=True)
            # if los is not None:
            #     cent_x, cent_y = pyautogui.center(los)
            #     print("移动鼠标到推荐下方")
            #     pyautogui.moveTo(cent_x, cent_y+100, duration=1)
            #     time.sleep(1)
            # else:
            #     print("不是tc页面，识别错误")
            #     quit()

                # pyautogui.moveRel(0, 200)
            dist_scroll = int(-abs(cent_y - comment_y))
            dist_scroll = int(1.2 * dist_scroll)
            print("tc中滑动", dist_scroll)
            # print(dist_scroll)
            time.sleep(1)
            # pyautogui.scroll(-10)
            # pyautogui.scroll(-50)
            pyautogui.scroll(dist_scroll)
            # pyautogui.scroll(-462)
        else:
            print("没有匹配commen,滑动")
            ui = ui_identify()
            if ui["UI"] == "同城":
                cent_x, cent_y = ui["坐标"][0], ui["坐标"][1]
                print("移动鼠标到tc下方")
                pyautogui.moveTo(cent_x, cent_y+100, duration=0.2)
                # time.sleep(1)
            else:
                print("不是tc页面，退出")
                reset_to_tc()
            # ui_now = which_ui_identify()
            # if ui_now != "同城":
            #     reset_to_tc()
            # los = pyautogui.locateOnScreen('tj.png', confidence=0.5)
            # if los is not None:
            #     print("向下移动鼠标")
            #     cent_x, cent_y = pyautogui.center(los)
            #     pyautogui.moveTo(cent_x, cent_y+100)
            # time.sleep(1)
            pyautogui.scroll(-600)
            self.status_text = '没有匹配commen，正在播放' + time.strftime("%H:%M:%S", time.localtime())
            im = pyautogui.screenshot()
            im.save(r'.\screen\截屏.png')
        # pyautogui.moveTo(random.randint(0, 100), random.randint(0, 100))
        self.lbl2.config(text=self.status_text)
        self.after(int(self.txt.get('1.0', END)) * 1000, self.click_female_in_comment_auto())


def click_comment_icon_and_back(icon_x, icon_y):
    # pyautogui.PAUSE = 0.5
    pyautogui.moveTo(icon_x, icon_y)
    pyautogui.click(icon_x, icon_y)
    time.sleep(0.5)
    n_count = 0
    while True:
        los = pyautogui.locateOnScreen('laolao.png', confidence=0.7)
        if los is not None:
            print("检测到comment，进入comment页面")
            cent_x, cent_y = pyautogui.center(los)
            # cent_x = int(cent_y-200)
            # time.sleep(1)
            pyautogui.moveTo(cent_x, cent_y+50)
            # pyautogui.click(cent_x, cent_y+50)
            # time.sleep(1)
            break
        print("未进入到comment页面")
        n_count += 1
        if n_count > 20:
            return
    los = pyautogui.locateOnScreen('zan.png', confidence=0.6)
    zan_y = 0
    if los is not None:
        cent_x, zan_y = pyautogui.center(los)
    last_cent_y = -1
    while last_cent_y != zan_y or zan_y == 0:
        last_cent_y = zan_y
        cent_y = 0
        female = pyautogui.locateOnScreen('female.png', confidence=0.7)
        if female is not None:
            cent_x, cent_y = pyautogui.center(female)
            print("检测到female")
            pyautogui.moveTo(cent_x, cent_y)
            time.sleep(0.5)
            click_female_icon_and_back(cent_x, cent_y)
            # 判断是否退回到comment界面
            n_count = 0
            while True:
                print("等待返回到comment界面")
                los = pyautogui.locateOnScreen('laolao.png', confidence=0.6)
                if los is not None:
                    print("返回到comment界面")
                    break
                time.sleep(1)
                n_count += 1
                if n_count > 10:
                    reset_to_tc()
                    return "timeout"
        los = pyautogui.locateOnScreen("shafa.png", confidence=0.6)
        if los is not None:
            print("无人评论")
            break
        # 计算向下滑动距离
        female_y = cent_y
        los = pyautogui.locateOnScreen('laolao.png', confidence=0.7)
        if los is not None:
            cent_x, cent_y = pyautogui.center(los)
            pyautogui.moveTo(cent_x, cent_y+50)
            # pyautogui.click(cent_x, cent_y+50)
            # time.sleep(1)
        print("滑动")
        # print(zan_y)
        cent_y = 0
        los = pyautogui.locateOnScreen('laolao.png', confidence=0.6)
        if los is not None:
            cent_x, cent_y = pyautogui.center(los)
        dist_scroll = int(-abs(cent_y - female_y)*1.3)
        # pyautogui.scroll(-50)
        pyautogui.scroll(dist_scroll)
        los = pyautogui.locateOnScreen('zan.png', confidence=0.5)
        if los is not None:
            cent_x, zan_y = pyautogui.center(los)
    # print(last_cent_y)
    # print(zan_y)
    print("滑到底了")
    time.sleep(1)
    los = pyautogui.locateOnScreen('back.png', confidence=0.6)
    if los is not None:
        cent_x, cent_y = pyautogui.center(los)
        pyautogui.click(cent_x, cent_y)


def click_female_icon_and_back(icon_x, icon_y):
    # print('click-female')
    pyautogui.PAUSE = 0.5
    # print(2, "    ", icon_x, icon_y)
    # pyautogui.moveTo(0, 0)
    los = pyautogui.locateOnScreen("shuru.png", confidence=0.6)  # 输入框状态
    if los is not None:
        pyautogui.click(icon_x, icon_y)
    print('点击female')
    pyautogui.click(icon_x, icon_y)  # 进入主页
    time.sleep(1)
    # while True:
    #     los = pyautogui.locateOnScreen('kuozhan.png', confidence=0.7)
    #     if los is not None:
    #         print("进入到个人主页")
    #         break
    #     time.sleep(1)
    while True:
        los = pyautogui.locateOnScreen('xiaozhitiao.png', confidence=0.6)
        if los is not None:
            print("进入到female页面")
            back_icon = None
            while back_icon is None:
                print("等待back图标")
                time.sleep(1)
                back_icon = pyautogui.locateOnScreen('back.png', confidence=0.7)
            cent_x, cent_y = pyautogui.center(back_icon)
            print("退出female页面")
            time.sleep(1)
            pyautogui.click(cent_x, cent_y)  # 退出
            break
        else:  # 匿名用户
            los = pyautogui.locateOnScreen('chacha.png', confidence=0.6)
            if los is not None:
                print("匿名用户")
                cent_x, cent_y = pyautogui.center(los)
                print("退出female页面")
                time.sleep(1)
                pyautogui.click(cent_x, cent_y)
                break
            else:  # 对方开启隐身
                time.sleep(1)
                los_ys = pyautogui.locateOnScreen('ys_comment.png', confidence=0.9)
                los = pyautogui.locateOnScreen('back.png', confidence=0.6)
                if los is not None and los_ys is not None:
                    print("对方开启隐身")
                    cent_x, cent_y = pyautogui.center(los)
                    print("退出female页面")
                    time.sleep(1)
                    pyautogui.click(cent_x, cent_y)
                    break
                else:  # 隐身用户
                    time.sleep(3)
                    print("隐身用户")
                    break
                    # los = pyautogui.locateOnScreen('qtzl.png', confidence=0.6)
                    # if los is not None:
                    #     print("隐身用户")
                    #     cent_x, cent_y = pyautogui.center(los)
                    #     print("退出female页面")
                    #     time.sleep(1)
                    #     pyautogui.click(cent_x, cent_y+100)
                    #     break


def test():
    pass


def which_ui_identify():
    pyautogui.moveTo(1, 1)
    los = pyautogui.locateOnScreen('tc_in.png', confidence=0.5)
    if los is not None:
        return "同城"
    los = pyautogui.locateOnScreen('laolao.png', confidence=0.6)
    if los is not None:
        return "唠唠"
    los = pyautogui.locateOnScreen('xiaozhitiao.png', confidence=0.6)
    if los is not None:
        return "简历"
    return "未知"


def ui_identify():
    pyautogui.moveTo(1, 1)
    tc_feature_pic_list = ['tc_in.png', 'tc_in2.png', 'tc_in3.png']
    for tc_feature_pic in tc_feature_pic_list:
        los = pyautogui.locateOnScreen(tc_feature_pic, confidence=0.9)
        if los is not None:
            cent_xy = pyautogui.center(los)
            tc_x, tc_y = cent_xy
            res = {"UI": "同城", "坐标": [tc_x, tc_y]}
            return res
    los = pyautogui.locateOnScreen('laolao.png', confidence=0.9)
    if los is not None:
        cent_xy = pyautogui.center(los)
        tc_x, tc_y = cent_xy
        res = {"UI": "唠唠", "坐标": [tc_x, tc_y]}
        return res
    los = pyautogui.locateOnScreen('xiaozhitiao.png', confidence=0.9)
    if los is not None:
        cent_xy = pyautogui.center(los)
        tc_x, tc_y = cent_xy
        res = {"UI": "简历", "坐标": [tc_x, tc_y]}
        return res
    return {"UI": "未知", "坐标": [0, 0]}


def reset_to_tc():
    # 重置到同城
    print("重置到同城界面")
    # ui_dic = {"同城": 0, "唠唠": 1, "简历": 2}
    # ui_now = which_ui_identify()
    # j = 0
    # try:
    #     j = ui_dic[ui_now]
    # except KeyError:
    #     print("未知界面")
    #     print("dengdai")
    #     time.sleep(5)
    #     los = pyautogui.locateOnScreen('tc.png', confidence=0.7)
    #     if los is not None:
    #         cent_x, cent_y = pyautogui.center(los)
    #         print("点击同城按钮")
    #         time.sleep(5)
    #         pyautogui.moveTo(cent_x, cent_y)
    #         pyautogui.click(cent_x, cent_y)
    #         return
    # for i in range(int(j)):
    #     los = pyautogui.locateOnScreen('back.png', confidence=0.6)
    #     if los is not None:
    #         cent_x, cent_y = pyautogui.center(los)
    #         time.sleep(1)
    #         pyautogui.click(cent_x, cent_y)

    # 方法二重置到同城界面
    while True:
        pyautogui.moveTo(1, 1)
        los = pyautogui.locateOnScreen('back.png', confidence=0.7)
        if los is not None:
            cent_x, cent_y = pyautogui.center(los)
            pyautogui.click(cent_x, cent_y)
        los_tc = pyautogui.locateOnScreen('tc.png', confidence=0.7)
        if los_tc is not None:
            cent_x, cent_y = pyautogui.center(los_tc)
            pyautogui.click(cent_x, cent_y)
            return
        los_in = pyautogui.locateOnScreen('tc_in.png', confidence=0.7)
        if los_in is not None:
            return
        time.sleep(1)


def main():
    # 进入同城界面
    tc_loc = pyautogui.locateOnScreen('tc.png', confidence=0.7)
    loc = tc_loc
    if loc is not None:
        cent_xy = pyautogui.center(loc)
        tc_x, tc_y = cent_xy
        pyautogui.click(cent_xy)
    else:
        print("没匹配到tc.png")
        # quit()
    time.sleep(1)

    # 进入female界面
    app = App()
    app.geometry('280x100+200+300')
    app.mainloop()


if __name__ == '__main__':
    main()


    # reset_to_tc()

    # los = pyautogui.locateAllOnScreen('comment.png', confidence=0.6)
    # for comment_icon in los:
    #     cent_x, cent_y = pyautogui.center(comment_icon)
    #     click_comment_icon_and_back(cent_x, cent_y)

    # if los is not None:
    #     cent_x, cent_y = pyautogui.center(los)
    #     pyautogui.click(cent_x, cent_y)
    # else:
    #     cent_y = 0
    #     quit()
    # click_comment_icon_and_back()

    # females = pyautogui.locateAllOnScreen('female.png', confidence=0.8)
    # # print(len(females))
    # for female in pyautogui.locateAllOnScreen('female.png', confidence=0.6):
    #     print(female)


