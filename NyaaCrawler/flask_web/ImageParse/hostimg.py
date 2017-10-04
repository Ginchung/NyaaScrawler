import requests
import re
from lxml import etree

class hostimg(object):
    def __init__(self, url):
        self.url = url

    def get(self):
        BigImgUrl = ''
        try:
            if re.match(r".*hostimg.co/i/.*",self.url):
                r = requests.get(self.url)
                sel = etree.HTML(r.text)
                BigImgUrl = sel.xpath('//*[@id="image-viewer-container"]/img/@src')[0]

            else:
                BigImgUrl = self.url
        except Exception as e:
            print("hostimg錯誤: url=", self.url, " message=", str(e))


        return BigImgUrl

if __name__ == '__main__':
    # imh = hostimg("https://hostimg.co/i/6q5zS")
    imh = hostimg("https://hostimg.co/images/2017/09/28/h.ero-Viper-GTS---03-480p-HEVC-jpneng-audiouncC01F5075.mkv_snapshot_00_20_11.751_8bit.th.png")
    print(imh.get())