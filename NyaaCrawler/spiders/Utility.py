from urllib.parse import urlencode

class Utility:
    # 依據搜尋關鍵字 組合出搜尋url 用法 BuildUrl('http://xxx/',{'key':'value'})
    @staticmethod
    def NyaaCatBuildUrl(url,page, **querys):
        return url + str(page) + '?' + urlencode(querys)

    # 匹配html 找出文章

    def GetNyaaDevItem(self):
        pass

    def GetNyaaCatItem(self):
        pass