import requests
import re
from lxml import etree

class xplanet(object):
    def __init__(self, url):
        self.url = url

    def get(self):
        BigImgUrl = ''
        try:

            if re.match(r"^https?://3xplanet.com/view/.*html$",self.url):
                r = requests.get(self.url)
                sel = etree.HTML(r.text)
                BigImgUrl = sel.xpath('//*[ @ id = "view-content"]/img/@src')[0]

            return BigImgUrl
        except Exception as e:
            print("xplanet錯誤: url=",self.url," message=",str(e))

if __name__ == '__main__':
    imh = xplanet("http://3xplanet.com/view/278389.html")
    print(imh.get())