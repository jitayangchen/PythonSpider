import os
import urllib2

from bs4 import BeautifulSoup
import re
import urlparse

class HtmlParser(object):
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # links = soup.find_all('a', href=re.compile(r"/view/\d+\.htm"))
        # for link in links:
        #     new_url = link['href']
        #     new_full_url = urlparse.urljoin(page_url, new_url)
        #     new_urls.add(new_full_url)

        links = soup.find_all('a', href=re.compile(r"html/article/index"))
        for link in links:
            new_url = link.get('href')
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)

        pagination = soup.find(name='div', attrs={"class": "pagination"})
        if pagination is None:
            print('pagination is None')
            return new_urls

        links = pagination.find_all('a')
        for link in links:
            new_urls.add(urlparse.urljoin(page_url, link.get('href')))

        return new_urls

    def download_img(self, img_url):
        print("---------- download stat ----------")
        save_path = os.getcwd() + '/imgs/'
        arr = img_url.split('/')
        conn = urllib2.urlopen(img_url)
        print('------downloading')
        if conn.getcode() != 200:
            print("---------- response !==200")
            return None

        f = open(save_path + arr[len(arr) - 1])
        while True:
            s = conn.read(1024 * 100)
            print(len(s))
            if len(s) == 0:
                break
            f.write(s)
            f.flush()
        f.close()
        print("---------- download complete ----------")

    def _get_new_data(self, soup):
        links = soup.find_all('img')
        for link in links:
            img_url = link['src']
            print(img_url)
            # self.download_img(img_url)

    def paser(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='gb2312')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(soup)
        return new_urls, new_data
