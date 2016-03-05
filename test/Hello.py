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

root_url = "http://pic.14bobo.com/desimgs/201510/20151030410261026.jpg"
# arr = root_url.split('/')
#
# print(arr[len(arr) - 1])

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
          'Accept': 'text/html;q=0.9,*/*;q=0.8',
          'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
          'Accept-Encoding': 'gzip',
          'Connection': 'close',
          'Referer': 'pic.14bobo.com'}

print("---------- download stat ----------")
save_path = os.getcwd() + '/imgs/'
arr = root_url.split('/')

req_timeout = 60
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
