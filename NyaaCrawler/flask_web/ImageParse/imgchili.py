class imgchili(object):
    def __init__(self, url):
        self.url = url

    def get(self):
        return '進到imgchili url='+self.url

if __name__ == '__main__':
    imh = imgchili("gag")
    print(imh.get())