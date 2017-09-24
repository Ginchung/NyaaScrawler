import logging

class Image:
    logging.basicConfig(
        level=logging.WARNING,
        format=
        '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
        datefmt='%a,%Y %b %d  %H:%M:%S',
        handlers=[logging.FileHandler('../Logs/NoSupportImageUrl.log', 'a', 'utf-8'), ])
    logging.getLogger("ImageHandler").setLevel(logging.WARNING
                                               )  # 将requests的日志级别设成WARNING


    # 依據domain 呼叫不同的function
    def getImage(self, domain,url):
        def func_not_found():  # 未支援的圖床會回傳找不到url
            logging.warning("url: "+url)
            return "This image url:(" + domain + ") is not yet supported!"
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
        # 如果domain有在host的value裡 取出host的key
        domainName = ''
        if domain in host.values():
            domainName = list(host.keys())[list(host.values()).index(domain)]

        func_name = 'func_' + domainName
        func = getattr(self, func_name, func_not_found)
        return func()

    def func_imgchili(self):
        return 'imgchili'

    def func_pixsense(self):
        return 'pixsense'

if __name__=='__main__':
    result = Image().getImage('adhadh.','http://dahah.com.tw/5747.jpg')
    print(result)