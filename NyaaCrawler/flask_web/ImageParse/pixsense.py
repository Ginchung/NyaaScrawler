import requests
import re
from lxml import etree

class pixsense(object):
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
            if re.match(r"^https?://\w+.pixsense.net/site/[\w/#&]+$",self.url):
                r = requests.get(self.url)
                img = re.search(r"attr\(\"src\",\"(?P<url>http://www.pixsense.net/themes/[^\"]*)",r.text)
                if img:
                    BigImgUrl = img["url"]

            return BigImgUrl
        except Exception as e:
            print("pixsense錯誤: url=",self.url," message=",str(e))

if __name__ == '__main__':
    # imh = pixsense("http://www.pixsense.net/site/v/3035160#2095&3035160")
    imh = pixsense("https://www.pixsense.net/site/v/2950051")
    print(imh.get())