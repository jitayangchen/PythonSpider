import requests
import time
from lxml import etree
import os
import random
import urlparse

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


def download(img_url, save_path, img_name):

    result = requests.get(img_url, None, headers=header, timeout=30)
    if result.status_code == 200:
        f = open(save_path + img_name, 'wb')
        f.write(result.content)
        f.flush()
        f.close()


def main():
    root_url = "http://www.299gan.com/html/pic/as/Heyzo01041700426P/"

    # save_path = '/mnt/SanDisk/imgs2/'
    save_path = os.getcwd() + '/imgs/'
    is_exists = os.path.exists(save_path)
    print is_exists
    if not is_exists:
        os.mkdir(save_path)

    img_names = set()
    img_list = os.listdir(save_path)
    for name in img_list:
        img_names.add(name)

    count = 0
    count_url = 0
    for i in range(50):
        result = requests.get(root_url, None, headers=header, timeout=30)
        if result.status_code == 200:
            html = etree.HTML(result.text)
            new_url = html.xpath('//*[@class="next_pre"]/span[2]/a/@href')[0]
            root_url = urlparse.urljoin(root_url, new_url)
            img_urls = html.xpath('//*[@class="news"]/img/@src')
            count_url += 1
            print 'Url page === ', count_url
            for img_url in img_urls:
                arr = img_url.split('/')
                img_name = arr[len(arr) - 1]
                count += 1
                if img_name not in img_names:
                    print 'start download img'
                    download(img_url, save_path, img_name)
                    img_names.add(img_name)
                    time.sleep(random.randint(1, 10) / 5.0)
                    print 'count === ', count
                else:
                    print 'old count === ', count


main()
