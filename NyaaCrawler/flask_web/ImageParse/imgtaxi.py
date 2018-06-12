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
        imgtaxi類都可以replace small to big看到大圖
        """
        try:
            if re.match(r"http.*(?=html)",self.url):
                r = requests.get(self.url)
                # https://imgadult.com/upload/small/2017/09/26/59ca0e7512c0d.jpg
                img = re.search(r"(?P<url>https?://[\w\.]+/(images|upload).*.jpe?g)",r.text)
                if img:
                    BigImgUrl = img["url"].replace("small","big")
            elif re.match(r"http.*(?=(jpe?g|png))",self.url):
                BigImgUrl = self.url.replace("small","big")

            return BigImgUrl
        except Exception as e:
            print("imgtaxi錯誤: url=",self.url," message=",str(e))

if __name__ == '__main__':
    # imh = imgtaxi("https://imgtaxi.com/img-59cb3bb991980.html")
    # imh = imgtaxi("https://imgadult.com/img-59ca38ac53cb8.html")
    imh = imgtaxi("https://imgwallet.com/img-59ca0e7785759.html")
    print(imh.get())
