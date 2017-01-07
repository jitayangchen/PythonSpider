import urllib2
import lxml

import re
from bs4 import BeautifulSoup
root_url = "http://www.8111ppp.com/html/part/index10_2.html"
# /html/article/index98962.html


def download(url):
        if url is None:
            return None
        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            return None

        return response.read()

soup = BeautifulSoup(download(root_url), 'html.parser', from_encoding='gb2312')

links = soup.find_all('img')
for link in links:
    print(link['src'])

links = soup.find_all('a', href=re.compile(r"html/(article)|(part)/index"))
for link in links:
    print(link.get('href'))


def get_pagination_url():
    pagination = soup.find(name='div', attrs={"class": "pagination"})
    if pagination is None:
        print('pagination is None')
        return
    links = pagination.find_all('a')
    for link in links:
        print(link.get('href'))


get_pagination_url()