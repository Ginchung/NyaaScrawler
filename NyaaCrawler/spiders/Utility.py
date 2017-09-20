from urllib.parse import urlencode
import feedparser

class Utility:
    # 依據搜尋關鍵字 組合出搜尋url
    @staticmethod
    def BuildUrl(url, **querys):
        return url + urlencode(querys)

    # 匹配html 找出文章

    def GetNyaaDevItem(self):
        pass

    def GetNyaaCatItem(self):
        pass