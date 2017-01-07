import requests
import time
from lxml import etree
import os
import random
import urlparse

root_url = "http://www.299gan.com/html/pic/as/Heyzo01041700426P/"

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
#     print result.text
#     html = etree.HTML(result.text)
#     img_path_arr = html.xpath('//*[@class="news"]/img/@src')
#     for path in img_path_arr:
#         print path
#     new_url = html.xpath('//*[@class="next_pre"]/span[2]/a/@href')[0]
#     print urlparse.urljoin(root_url, new_url)


def download(img_url):
    save_path = '/mnt/SanDisk/imgs2/'
    # save_path = os.getcwd() + '/imgs/'
    arr = img_url.split('/')

    result = requests.get(img_url, None, headers=header)
    if result.status_code == 200:
        f = open(save_path + arr[len(arr) - 1], 'wb')
        f.write(result.content)
        f.flush()
        f.close()

count = 0
countUrl = 0
for i in range(100):
    result = requests.get(root_url, None, headers=header)
    if result.status_code == 200:
        html = etree.HTML(result.text)
        new_url = html.xpath('//*[@class="next_pre"]/span[2]/a/@href')[0]
        root_url = urlparse.urljoin(root_url, new_url)
        imgUrls = html.xpath('//*[@class="news"]/img/@src')
        countUrl += 1
        print 'Url page === ', countUrl
        for imgUrl in imgUrls:
            download(imgUrl)
            count += 1
            print 'count === ', count
            time.sleep(random.randint(1, 10) / 10.0)
