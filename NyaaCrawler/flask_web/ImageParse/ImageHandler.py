
class Image:

    def __init__(self,domain,url):
        self.__initImageClient(domain,url)

    # 依據domain 呼叫不同的class
    def __initImageClient(self, domain,url):

        # 支援的圖床 key是domain ，value是要使用的class 用來處理此domain的圖片
        host = {
            "imgchili.net":"imgchili",
            "t13.imgchili.net": "imgchili",
            "www.pixsense.net":"pixsense",
            "imagetwist.com": "imagetwist",
            "3xplanet.com": "xplanet",
            "hostimg.co": "hostimg",

            # =========================
            # 直接回傳
            "i.imgur.com": "directReturn",
            "imgtuku.com": "directReturn",
            "www.qpic.ws": "directReturn",
            "4.bp.blogspot.com": "directReturn",
            "3.bp.blogspot.com": "directReturn",
            "2.bp.blogspot.com": "directReturn",
            "1.bp.blogspot.com": "directReturn",
            "imghost.io": "directReturn",
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
            "xxx.pornscreen.xyz": "eu5588",
            # ========================
            # 有鎖continue to image 但直接在頁面就能抓得到圖
            "imgtaxi.com": "imgtaxi",
            "imgdrive.net": "imgtaxi",
            "imgadult.com": "imgtaxi",
            "imgwallet.com": "imgtaxi",
            # =========================
            # 有鎖continue to image  點擊button挾帶參數post
            "img.yt": "imgyt",
            "xxxwebdlxxx.org": "imgyt",
            "imgtornado.com": "imgyt",
            # ===================================
            # 需要取得轉址後連結 點擊continue to image 並夾帶多個hidden參數
            "imgrock.co": "imgrock",
            "r01.imgrock.co": "imgrock",
            "io1.imgoutlet.co": "imgrock",  # 這圖床的continue按鈕好像是用js載入的 待研究
            "imgoutlet.co": "imgrock",  # 原理同上  continue button是用js載入的
             # =================================



             "www.imgbabes.com":"NotSupport", # 會用到javascript 先跳過
            "www.imgflare.com": "NotSupport",# 同上 會用到js
            "www.fapforfun.com": "NotSupport", # 看起來會直接連到gallery
            "anidex.info": "NotSupport",  # 這網址會連到另一個種子站 先跳過
            "www.dmm.co.jp": "NotSupport", # 會連到gallery
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