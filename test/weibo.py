import requests

cookie = {"Cookie": "SCF=AuRvbH0V9yd5jUeUGbeC20T8T07EwZPbNmHIiK2jFjP_Ia7PeRTJPW2d-BtALmWOeyHjkh1HknYFlQ2eJP7uwJM.; SUHB=0h148hvIa_meYy; SSOLoginState=1482416455; ALF=1485008455; _T_WM=f579f545f516c66ea966f81d1d5de19c; SUB=_2A251ahesDeRxGedI6VIS9SjEwj6IHXVWlLnkrDV6PUJbkdAKLXD2kW0F3_AqXyt-mK_wkRiidTDyG-cOyg..; gsid_CTandWM=4ukybeab1S3l0cFN6ZMFl6NwMeo"}
url = "http://weibo.cn/?vt=4"
html = requests.get(url, cookies=cookie).content
print html