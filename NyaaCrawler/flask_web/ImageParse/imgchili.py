import requests
import re
from lxml import etree

class imgchili(object):
    def __init__(self, url):
        self.url = url

    def get(self):
        BigImgUrl = ''

        if re.match(r".*show.*",self.url):
            r = requests.get(self.url)
            sel = etree.HTML(r.text)
            BigImgUrl = sel.xpath('//*[@id="show_image"]/@src')[0]

        else:
            # 把t(\d){2}的字串換成 i(\d){2}  ex. t13 -> i13  t100->i100
            BigImgUrl = re.sub(r"(t)(\d+)", r"i\2", self.url)


        return BigImgUrl

if __name__ == '__main__':
    imh = imgchili("http://imgchili.net/show/112285/112285521_sample.png")
    # imh = imgchili("http://t13.imgchili.net/112285/112285521_sample.jpg")
    print(imh.get())