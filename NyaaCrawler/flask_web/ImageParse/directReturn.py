class directReturn(object):
    def __init__(self, url):
        self.url = url
    # 直接回傳圖片網址
    def get(self):
        return self.url

if __name__ == '__main__':
    imh = directReturn("http://imgchili.net/show/112285/112285521_sample.png")
    print(imh.get())