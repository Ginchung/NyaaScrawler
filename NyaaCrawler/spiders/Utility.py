from urllib.parse import urlencode
import re
from dateutil import parser
from scrapy.conf import settings

class Utility:
    # 依據搜尋關鍵字 組合出搜尋url
    @staticmethod
    def BuildUrl(url, **querys):
        return url + '?' + urlencode(querys)

    # 輸入html 找出所有的網址連結 回傳dict {url:'xxx','domain':'xxx'}
    def GetUrlFromHtml(self,html):
        # match所有url
        pattern = '(?P<url>(?:\w+):\/\/(?P<domain>[\w@][\w.:@-]+)\/?[\w\.?=%&=\-@/$,]*)'
        regex = re.compile(pattern)
        # match description裡所有的url 將url跟domain存在dict裡 格式 {'url':'xxx','url':'http://xxx/'}
        urls = [m.groupdict() for m in regex.finditer(html)]
        # 用set移除重覆的url
        seen = set()
        new_l = []
        for d in urls:
            t = tuple(d.items())
            if t not in seen:
                seen.add(t)
                new_l.append(d)

        return new_l

    # 將字串轉為YYYY-MM-DD HH:MM:SS的DateTime格式
    def strToDateTime(self,text):
        dt = parser.parse(text)
        return dt.strftime(settings['DATETIME_FORMAT'])

    # 輸入檔案大小 轉成MB 接受以下格式 12316546、123 Mib、123Gib
    def convertSize(self,text):
        item = re.match("(?P<size>[\d\.]+)\s?(?P<st>\w+)?", text)
        if (item):
            size = item.group('size')
            st = item.group('st')
            # 找不到st就是byte 除以1024的平方轉成MB
            if st is None:
                return round(float(size) / (1024 * 1024), 1)
            elif st.upper() == 'GIB':
                return round(float(size) * 1000, 1)
            elif st.upper() == 'MIB':
                return float(size)
            else:
                return 0
        else:
            return 0

if __name__=='__main__':
    print(settings['DATETIME_FORMAT'])