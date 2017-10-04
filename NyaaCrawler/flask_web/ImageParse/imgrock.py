import requests
import re
from lxml import etree

class imgrock(object):
    def __init__(self, url):
        self.url = url

    def get(self):
        BigImgUrl = ''
        try:
            # 取得fileCode 用來加在cookie 用在step2的Get request
            m = re.match(r"http://[\w\.]+\/(?P<fileCode>\w+)\/.*html", self.url)
            fileCode = ''
            if m:
                fileCode = m["fileCode"]

            # 如果是連結網址就進行request 縮圖網址就忽略
            if re.match(r"http.*(?!html)", self.url):
                s = requests.session()
                r = s.get(self.url)
                # 抓取php連結 此為真正的連結
                realLink = re.search(r"http://(\w|\.)+\/.*\.php",r.text)[0]

                r2 = s.get(realLink,data={'fileCode':fileCode})
                # 因為隱藏欄位是用js產生的 所以直接match javascript裡的<input type="hidden"的值>
                # hiddenValue = re.search(r"<input\\x20type=\\x22hidden\\x22\\x20name=\\x22\'\+\'(?P<hiddenValue>[^']+)",r2.text)

                # 更新 不是match <input type="hidden"的值 而是match類似下面的這串值
                # (_0x7995('0x72','TB3R'),"a3fef360d8a2279ab2d067f4554280e4")
                hiddenValue = re.search(r"\(_0x7995\(\'0x72\',\'TB3R\'\)\,\"(?P<hiddenValue>[^\"]+)",r2.text)

                # 再向php連結post一次
                headers = {'Content-type': 'application/x-www-form-urlencoded'}
                data = {"op":"view","id":fileCode,"pre":"1",hiddenValue["hiddenValue"]:"1"}

                r3 = s.post(realLink,headers=headers,data=data)
                BigImgUrl = re.search(r"img\ssrc=\"(?P<img>http://[^\/]+\/img\/[^\"]+\.jpe?g)\"",r3.text)["img"]

            else:
                BigImgUrl = self.url
        except Exception as e:
            print("imgrock錯誤: url=",self.url," message=",str(e))




        return BigImgUrl

if __name__ == '__main__':
    # imh = imgrock("http://imgrock.co/15lok1ijuoj0/MVSD-009.jpg.html")
    # imh = imgrock("http://r01.imgrock.co/i/00269/sq3ja45cjoqv_t.jpg")
    imh = imgrock("http://imgoutlet.co/qf8looqufspr/IBW-495z.jpg.html")

    print(imh.get())