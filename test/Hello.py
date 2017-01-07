# -*- coding: UTF-8 -*-
# print "你好 世界"


# for letter in 'Python':
#     print('lala : ', letter)


# fruits = ['banana', 'apple', 'mango']
# for fruit in fruits:
#     print('haha : ', fruit)
import cookielib
import os
import urllib2

# url = 'http://www.baidu.com'
# print('---------- lalala hahaha ----------')
# cj = cookielib.CookieJar()
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
# urllib2.install_opener(opener)
# response = urllib2.urlopen(url)
# print(response.getcode())
# print(cj)
# print(response.read())
# import re
#
# print(re.compile(r"/view/\d+\.htm"))

root_url = "http://i.meizitu.net/2017/01/04a01.jpg"
# arr = root_url.split('/')
#
# print(arr[len(arr) - 1])

# GET /d4/3030/303001-2.jpg HTTP/1.1
# Host: pic.d741.com
# Connection: keep-alive
# Cache-Control: max-age=0
# Upgrade-Insecure-Requests: 1
# User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
# Accept-Encoding: gzip, deflate, sdch
# Accept-Language: zh-CN,zh;q=0.8,en;q=0.6
# Cookie: __cfduid=d7ad26dc6d0ab6ce0290bc10917ab65081482416826
# If-Modified-Since: Tue, 19 Apr 2016 21:57:50 GMT

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

req_timeout = 5
req = urllib2.Request(root_url, None, headers=header)
conn = urllib2.urlopen(req, None, req_timeout)

if conn.getcode() != 200:
    print("---------- response !==200")

f = open(save_path + arr[len(arr) - 1], 'wb')
while True:
    s = conn.read()
    print(len(s))
    if len(s) == 0:
        break
    f.write(s)
    f.flush()
f.close()
print("---------- download complete ----------")
