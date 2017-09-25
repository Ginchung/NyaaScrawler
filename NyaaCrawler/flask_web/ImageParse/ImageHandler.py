
class Image:

    def __init__(self,domain,url):
        self.__initImageClient(domain,url)

    # 依據domain 呼叫不同的class
    def __initImageClient(self, domain,url):

        # 支援的圖床
        host = {
            "imgchili": "imgchili.net",
            "pixsense": "www.pixsense.net",
            "55888":"55888.eu",
            "imgazel": "imgazel.info",
            "imgyt": "img.yt",
            "anidex": "anidex.info",
            "imgbabes": "www.imgbabes.com",
            "imageteam": "imageteam.org",
            "imgtaxi": "imgtaxi.com",
            "imagetwist": "imagetwist.com",
            "imgseed": "imgseed.com",
            "dimtus": "dimtus.com",
            "hentai": "e-hentai.org",
            "imgur": "i.imgur.com",
            "damimage": "damimage.com",
            "imgstudio": "imgstudio.org",
            "imgtuku": "imgtuku.com",
            "imagedecode": "imagedecode.com",
            "xxxwebdlxxx": "xxxwebdlxxx.org",
            "imgflare": "www.imgflare.com",
            "3xplanet":"3xplanet.com",
            "imgdrive": "imgdrive.net",
            "imgtornado": "imgtornado.com",
            "imgadult": "imgadult.com",
            "imgwallet": "imgwallet.com",
            "qpic": "www.qpic.ws",
            "18itv": "18itv.com",
            "imgoutlet": "io1.imgoutlet.co",

        }
        # 依據domain 找出對應的class
        domainName = list(host.keys())[list(host.values()).index(domain)]
        # 如果import不到此class 就使用NotSupport class
        try:
            imgClass = __import__(domainName)
        except:
            imgClass = __import__('NotSupport')
            domainName = 'NotSupport'

        self.ImgClient = getattr(imgClass, domainName)(url=url)

    def get(self):
        return self.ImgClient.get()

if __name__=='__main__':
    result = Image('damimage.com','http://imgchili.net/5747.jpg')

    print(result.get())