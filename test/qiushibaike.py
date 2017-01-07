# -*- coding: UTF-8 -*-
import urllib2

# from lxml import etree

header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
          'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
          # 'Accept-Encoding': 'gzip, deflate, sdch',
          'Cache-Control': 'max-age=0',
          'Upgrade-Insecure-Requests': '1',
          'Connection': 'keep-alive'}

req = urllib2.Request("http://www.baidu.com", headers=header)
response = urllib2.urlopen(req)
content = response.read()
print content