
class Image:

    def __init__(self,domain,url):
        self.__initImageClient(domain,url)

    # 依據domain 呼叫不同的class
    def __initImageClient(self, domain,url):

        # 支援的圖床 key是domain ，value是要使用的class 用來處理此domain的圖片
        host = {
            "imgchili.net":"imgchili",
            "www.pixsense.net":"pixsense",
            "img.yt": "imgyt",
            "imagetwist.com": "imagetwist",
            "3xplanet.com": "xplanet",
            # =========================
            # 直接回傳
            "i.imgur.com": "directReturn",
            "imgtuku.com": "directReturn",
            # ================
            # 圖片規則是/upload/big的圖床
            "55888.eu":"eu5588",
            "imgazel.info":"eu5588",
            "imageteam.org": "eu5588",
            "imgseed.com": "eu5588",
            "i.imgseed.com": "eu5588",
            "dimtus.com": "eu5588",
            "damimage.com": "eu5588",
            "imgstudio.org": "eu5588",
            "imagedecode.com": "eu5588",
            # =================

             "anidex.info":"NotSupport", # 這網址會連到另一個種子站 先跳過
             "www.imgbabes.com":"NotSupport", # 會用到javascript 先跳過
            "www.imgflare.com": "NotSupport",# 同上 會用到js

            # 可參考imgyt 可能原理都一樣
            "imgtaxi.com":"NotSupport", # 這個需要按continue to image
            "xxxwebdlxxx.org":"NotSupport",# 有鎖continue to image
            "imgdrive.net": "NotSupport",# 有鎖continue to image
            "imgtornado.com": "NotSupport",# 有鎖continue to image
            "imgadult.com": "NotSupport",# 有鎖continue to image
            "imgwallet.com": "NotSupport",# 有鎖continue to image
            "io1.imgoutlet.co":"NotSupport",# 有鎖continue to image


            "xxx.pornscreen.xyz": "NotSupport",
            "www.qpic.ws":"NotSupport",
            "t13.imgchili.net":"NotSupport",
            "tu6.3wk.cc":"NotSupport",
            "imgoutlet.co":"NotSupport",
            "www.dlsite.com":"NotSupport",
            "imgclick.net":"NotSupport",
            "bbs.mikocon.com":"NotSupport",
            "jav69.xyz":"NotSupport",
            "2.bp.blogspot.com":"NotSupport",
            "1.bp.blogspot.com":"NotSupport",
            "main.imgclick.net":"NotSupport",
            "imgrock.co":"NotSupport",
            "r01.imgrock.co":"NotSupport",
            "www.fapforfun.com":"NotSupport",
            "hostimg.co":"NotSupport",
            "bishoujo.moe":"NotSupport",
            "avhot.cc":"NotSupport",
            "imghost.io":"NotSupport",
            "www.dmm.co.jp":"NotSupport",

            # "":"NotSupport",
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