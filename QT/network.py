import os
from music import qt_beep
from quit_qt import qt_quit
import time


def network_connection(conn_time: int = 30, interval: int = 1):
    for i in range(conn_time):
        res = os.system("ping baidu.com -n 1")
        if res == 0:
            # print("有网")
            return True
        time.sleep(interval)
    # 没有网络
    print("没有网络，退出")
    qt_beep()
    qt_quit()
