from flask import Flask
from flask_pymongo import PyMongo
from dateutil import parser
import NyaaCrawler.settings as settings


app = Flask(__name__)
app.config.update(
    MONGO_HOST='localhost',
    MONGO_PORT=27017,
    MONGO_DBNAME='Nyaa'
)
mongo = PyMongo(app)

class ArticleList:
    # 取得所有文章
    def GetArticleAll(self):
        with app.app_context():
            # 不回傳_id欄位
            articles = mongo.db.Article.find({}, {'_id': 0}).sort("pubDate", -1)
            return dict(result='success', articlelist=articles)
    '''
    依據關鍵字搜尋文章
    fromDate:發佈日期_起
    toDate:發佈日期_迄
    keyWord:文章標題關鍵字
    minSize:檔案大小_起 type:字串
    maxSize:檔案大小_迄 type:字串
    sortKey:要排序的欄位 type:字串
    sortOrder:搜尋的排序 若無值 預設1  接受的參數:asc排序:'1' desc排序:'-1'  type:字串
    '''
    def GetArticleByKey(self,**kwargs):
        print(settings.DATETIME_FORMAT)
        with app.app_context():
            query = {}

            # 搜尋日期起迄
            fromDate = kwargs.get('fromDate', None)
            toDate = kwargs.get('toDate', None)
            # 當這兩個關鍵字有值 就新增一個key到dict
            if fromDate is not None or toDate is not None:
                key = "pubDate"
                query.setdefault(key, {})
            # 如果fromDate/toDate有值 最終格式:{'pubDate': {'$gte': '2017-09-21 00:00:00', '$lt': '2017-12-12 00:00:00'}}
            if fromDate is not None:
                query['pubDate'].update({'$gte': parser.parse(fromDate).strftime("%Y-%m-%d %H:%M:%S")})
            if toDate is not None:
                query['pubDate'].update({'$lt': parser.parse(toDate).strftime("%Y-%m-%d %H:%M:%S")})

            # 用關鍵字搜尋title 用regex達成like效果
            keyWord = kwargs.get('keyWord', None)
            if keyWord is not None:
                query['title'] = {'$regex':keyWord}

            # 搜尋檔案大小 起迄
            minSize = kwargs.get('minSize', None)
            maxSize = kwargs.get('maxSize', None)
            # 當這兩個關鍵字有值 就新增一個key到dict
            if minSize is not None or maxSize is not None:
                key = "size"
                query.setdefault(key, {})
            # 如果minSize/maxSize有值 就新增dict到size裡 最終格式:{'size': {'$gte': '123', '$lt': '999'}}
            if minSize is not None:
                query['size'].update({'$gte': float(minSize)})
            if maxSize is not None:
                query['size'].update({'$lt': float(maxSize)})

            # 排序
            sortQuery = []
            sortKey = kwargs.get('sortKey', None)
            sortOrder = kwargs.get('sortOrder', None)
            if sortKey is not None:
                if sortOrder in ['1','-1']:
                    sortQuery.append((sortKey, int(sortOrder)))
                else:
                    sortQuery.append((sortKey, 1))  # 如果沒設定sortOrder 預設ASC
            else:
                sortQuery.append(('pubDate', -1))  # 如果沒設定sortKey 預設用發佈日期 desc
            # 撈出資料
            article = mongo.db.Article.find(query, {'_id': 0}).sort(sortQuery)
            if article is not None:
                return dict(result='success', article=article)
            return dict(result='error', message='No record found')


if __name__=='__main__':
    ArticleList().GetArticleByKey(fromDate='20170921')

