import requests
import re
from lxml import etree

class imgtaxi(object):
    def __init__(self, url):
        self.url = url

    def get(self):
        BigImgUrl = ''
        """
        只request pixsense.net/site/v/xxxxxx的網址
        因為如果是縮圖 通常都會搭配圖床連結，就不用重覆抓取了 
        而且縮圖的規則沒辨法replace small to big就能看到大圖
        """
        if re.match(r"http.*(?=html)",self.url):
            r = requests.get(self.url)
            # https://imgtaxi.com/images/small/2017/09/27/59cb3bb991946.jpg
            img = re.search(r"(?P<url>https?://imgtaxi.com/images.*.jpe?g)",r.text)
            if img:
                BigImgUrl = img["url"].replace("small","big")
        elif re.match(r"http.*(?=(jpe?g|png))",self.url):
            BigImgUrl = self.url.replace("small","big")

        return BigImgUrl

if __name__ == '__main__':
    imh = imgtaxi("https://imgtaxi.com/images/small/2017/09/27/59cb67c3bccd7.jpg")
    print(imh.get())