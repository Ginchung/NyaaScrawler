import requests
import re
from lxml import etree

class imagetwist(object):
    def __init__(self, url):
        self.url = url

    def get(self):
        BigImgUrl = ''
        """
        只request pixsense.net/site/v/xxxxxx的網址
        因為如果是縮圖 通常都會搭配圖床連結，就不用重覆抓取了 
        而且縮圖的規則沒辨法replace small to big就能看到大圖
        """
        try:
            if re.match(r"^https?://imagetwist.com/.*$",self.url):
                r = requests.get(self.url)
                img = re.search(r"(?P<url>http://\w+.(imgtrex|imagetwist).com/i/[\w/]+.jpe?g)",r.text)
                if img:
                    BigImgUrl = img["url"]

            return BigImgUrl
        except Exception as e:
            print("imagetwist錯誤: url=",self.url," message=",str(e))

if __name__ == '__main__':
    imh = imagetwist("http://imagetwist.com/suumv6b9iw9p/kawd839pl.jpg")
    print(imh.get())