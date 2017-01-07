import requests
import time
from lxml import etree
import os
import random

root_url = "http://www.mzitu.com/22467"

header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Cache-Control': 'max-age=0',
    # 'Host': 'pic.d741.com',
    'Upgrade-Insecure-Requests': '1',
    'Connection': 'keep-alive'}


# result = requests.get(root_url, None, headers=header)
# if result.status_code == 200:
#     # print result.text
#     html = etree.HTML(result.text)
#     print html.xpath('//*[@class="pagenavi"]/a[last()]/@href')[0]


def download(img_url):
    print("---------- download stat ----------")
    save_path = '/mnt/SanDisk/imgs/'
    arr = img_url.split('/')

    result = requests.get(img_url, None, headers=header)
    if result.status_code == 200:
        f = open(save_path + arr[len(arr) - 1], 'wb')
        f.write(result.content)
        f.flush()
        f.close()
    print("---------- download complete ----------")

count = 0
for i in range(20000):
    result = requests.get(root_url, None, headers=header)
    if result.status_code == 200:
        html = etree.HTML(result.text)
        root_url = html.xpath('//*[@class="pagenavi"]/a[last()]/@href')[0]
        imgUrl = html.xpath('//*[@class="main-image"]/p/a/img/@src')[0]
        download(imgUrl)
        count += 1
        print 'count === ', count
        time.sleep(random.randint(1, 10) / 10.0)
