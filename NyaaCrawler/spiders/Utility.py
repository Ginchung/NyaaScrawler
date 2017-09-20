from urllib.parse import urlencode
import re
from dateutil import parser

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
        return urls

    # 將字串轉為YYYY-MM-DD HH:MM:SS的DateTime格式
    def strToDateTime(self,text):
        dt = parser.parse(text)
        return dt.strftime("%Y-%m-%d %H:%M:%S")
