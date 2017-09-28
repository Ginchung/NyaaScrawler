import requests
import re
from lxml import etree
"""
適用的domain:
eu55888.eu
imgazel.info
"""
class imgyt(object):
    def __init__(self, url):
        self.url = url

    def get(self):
        BigImgUrl = ''
        """
        如果結尾是html 就request 如果是圖片 就把samll換成big
        傳進來之前先判斷 如果有縮圖 就不要request img.yt/xxxx.html了
        通常都是重覆的 直接把縮圖換大圖就好
        
        需要request兩次才能取得到圖片 第一次get 第二次用post
        """
        if re.match(r"http.*(?=html)",self.url):
            s = requests.Session()
            # s.get(self.url)
            # headers = {'Content-type': 'application/x-www-form-urlencoded'}
            payload = {"imgContinue":"Continue+to+your+image..."}
            r = s.post(self.url)
            # img = re.search(r"(?P<url>http://[^\/]*\/upload\/big\/[^\']*)", r.text)
            # if img:
            #     BigImgUrl = img["url"]
        elif re.match(r"http.*(?=(jpe?g|png))",self.url):
            BigImgUrl = self.url.replace("small","big")

        return BigImgUrl

if __name__ == '__main__':
    imh = imgyt("https://img.yt/img-59c65a87227a3.html")
    print(imh.get())