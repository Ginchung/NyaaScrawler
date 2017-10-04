import requests
import re
from lxml import etree
import json
"""
適用的domain:
img.yt
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
        try:
            if re.match(r"http.*(?=html)",self.url):
                headers = {'Content-type': 'application/x-www-form-urlencoded'}
                data = {"imgContinue":self.chooseParam()}
                r = requests.post(self.url,data=data,headers = headers)
                img = re.search(r"(?P<url>https?://[^\/]*\/upload\/big\/[^\']*)", r.text)
                if img:
                     BigImgUrl = img["url"]
            elif re.match(r"http.*(?=(jpe?g|png))",self.url):
                BigImgUrl = self.url.replace("small","big")

            return BigImgUrl
        except Exception as e:
            print("imgyt錯誤: url=",self.url," message=",str(e))

    # 依據domain 選擇對應的參數
    def chooseParam(self):
        value = ''
        if re.search(r"img.yt",self.url) is not None:
            value = "Continue to your image"
        elif re.search(r"xxxwebdlxxx",self.url) is not None:
            value = "Continue to image ..."
        elif re.search(r"imgtornado", self.url) is not None:
            value ="Continue to Image"

        return value

if __name__ == '__main__':
    imh = imgyt("http://imgtornado.com/img-59cacef6a678b.html")
    print(imh.get())
    # print(imh.chooseParam())