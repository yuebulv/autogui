# 根据url.txt中网址和时间，定时打开网页
import os
import re
import webbrowser
import time
from urllib.request import urlopen

# 提取网址
new_url = []
url_path = 'url.txt'
if not os.path.exists(url_path):
    pass
else:
    url_file = open('url.txt', 'r')
    readlines = url_file.readlines()
    # print(readlines)
    regx = r'[^ \n\r\t]+'
    for line in readlines:
        url = re.findall(regx, line)
        # 这里可以筛选能打开的网址
        try:
            resp = urlopen(url[0])
        except ValueError:
            try:
                resp = urlopen('https://'+url[0])
            except:
                continue
        except:
            continue
        code = resp.getcode()
        if code == 200:
            new_url.append(url)
    print(f'网址：{new_url}')
# 访问网址
for url in new_url:
    webbrowser.open(url[0])
    time.sleep(int(url[1]))
