# -*- coding: UTF-8 -*-
import os
import requests


root_url = "http://caopic.146cao.com/pic/newspic/2017-1/rvfmfouxdkz-1350.jpg"

header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
          'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
          'Accept-Encoding': 'gzip, deflate, sdch',
          'Cache-Control': 'max-age=0',
          # 'Host': 'pic.d741.com',
          'Upgrade-Insecure-Requests': '1',
          'Connection': 'keep-alive'}

print("---------- download stat ----------")
save_path = os.getcwd() + '/imgs/'
arr = root_url.split('/')

result = requests.get(root_url, None, headers=header)
if result.status_code == 200:
    f = open(save_path + arr[len(arr) - 1], 'wb')
    f.write(result.content)
    f.flush()
    f.close()
print("---------- download complete ----------")
