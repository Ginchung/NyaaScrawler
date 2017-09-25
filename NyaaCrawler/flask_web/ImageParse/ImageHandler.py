
class Image:

    def __init__(self,domain,url):
        self.__initImageClient(domain,url)

    # 依據domain 呼叫不同的class
    def __initImageClient(self, domain,url):

        # 支援的圖床 key是domain ，value是要使用的class 用來處理此domain的圖片
        host = {
            "imgchili.net":"imgchili",
            "www.pixsense.net":"NotSupport",
            "55888.eu":"NotSupport",
            "imgazel.info":"NotSupport",
            "img.yt":"NotSupport",
             "anidex.info":"NotSupport",
             "www.imgbabes.com":"NotSupport",
             "imageteam.org":"NotSupport",
            "imgtaxi.com":"NotSupport",
             "imagetwist.com":"NotSupport",
             "imgseed.com":"NotSupport",
            "dimtus.com":"NotSupport",
            "e-hentai.org":"NotSupport",
            "i.imgur.com":"NotSupport",
            "damimage.com":"NotSupport",
            "imgstudio.org":"NotSupport",
            "imgtuku.com":"NotSupport",
            "imagedecode.com":"NotSupport",
            "xxxwebdlxxx.org":"NotSupport",
            "www.imgflare.com":"NotSupport",
            "3xplanet.com":"NotSupport",
            "imgdrive.net":"NotSupport",
            "imgtornado.com":"NotSupport",
            "imgadult.com":"NotSupport",
            "imgwallet.com":"NotSupport",
            "www.qpic.ws":"NotSupport",
            "18itv.com":"NotSupport",
            "io1.imgoutlet.co":"NotSupport",
        }
        # 依據domain 找出對應的class file並import 對應的class
        # 如果dict沒有此key 就使用NotSupport class
        default_value = 'NotSupport'
        domainName = host.get(domain, default_value)
        imgClass = __import__(domainName)
        self.ImgClient = getattr(imgClass, domainName)(url=url)

    def get(self):
        return self.ImgClient.get()

if __name__=='__main__':
    result = Image('www.imgflare.com','http://imgchili.net/5747.jpg')

    print(result.get())