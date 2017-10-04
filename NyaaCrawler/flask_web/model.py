from flask import Flask
from flask_pymongo import PyMongo
from dateutil import parser
import NyaaCrawler.settings as settings
import datetime


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
            articles = mongo.db.Article.find({}).sort("pubDate", -1)
            return dict(result='success', article=articles)
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
        with app.app_context():
            query = {}

            # 搜尋日期起迄
            fromDate = kwargs.get('fromDate', None)
            toDate = kwargs.get('toDate', None)
            # 當這兩個關鍵字有值 就新增一個key到dict
            if fromDate  or toDate:
                key = "pubDate"
                if not key in query:
                    query.setdefault(key, {})
            # 如果fromDate/toDate有值 最終格式:{'pubDate': {'$gte': '2017-09-21 00:00:00', '$lt': '2017-12-12 00:00:00'}}
            if fromDate:
                query['pubDate'].update({'$gte': parser.parse(fromDate).strftime(settings.DATETIME_FORMAT)})
            if toDate:
                query['pubDate'].update({'$lt': parser.parse(toDate).strftime(settings.DATETIME_FORMAT)})

            # 用關鍵字搜尋title 用regex達成like效果
            keyWord = kwargs.get('keyword', None)
            if keyWord:
                query['title'] = {'$regex':keyWord,'$options':'i'}

            # 如果有勾選只搜尋無碼的checkbox
            IsUncensored = kwargs.get('IsUncensored', None)
            if IsUncensored=='true':
                # 從setting取出無碼片的關鍵字 組成regex字串  ex.  'fc2|Heyzo|carib'
                regexUnconsole = settings.UncensoredKeyWords
                # 如果query裡已存在title這個key 用$and將兩個查詢組起來 再把title這個key刪掉
                if 'title' in query:
                    query['$and'] = [{'title': {'$regex': regexUnconsole, '$options': 'i'}}]
                    query['$and'].append({'title': query['title']})
                    query.pop('title', None)
                else:
                    query['title'] = {'$regex': regexUnconsole, '$options': 'i'}

            # 搜尋檔案大小 起迄
            minSize = kwargs.get('minSize', None)
            maxSize = kwargs.get('maxSize', None)
            # 當這兩個關鍵字有值 就新增一個key到dict
            if minSize or maxSize:
                key = "size"
                query.setdefault(key, {})
            # 如果minSize/maxSize有值 就新增dict到size裡 最終格式:{'size': {'$gte': '123', '$lt': '999'}}
            if minSize:
                query['size'].update({'$gte': float(minSize)})
            if maxSize:
                query['size'].update({'$lt': float(maxSize)})

            # 搜尋最近日期的資料 將pubDate的$gte更新為mindate
            maxage = kwargs.get('maxage', None)
            if maxage:
                key = "pubDate"
                if not key in query:
                    query.setdefault(key, {})
                # 只取date部份 把time設為0
                mindate = datetime.datetime.now().date() + datetime.timedelta(days=-int(maxage))
                query['pubDate'].update({'$gte': mindate.strftime(settings.DATETIME_FORMAT)})

            # 排序
            sortQuery = []
            sortKey = kwargs.get('sort', None)
            sortOrder = kwargs.get('order', None)
            if sortKey:
                if sortOrder in ['desc','asc']:
                    sortQuery.append((sortKey, 1 if sortOrder == 'asc' else -1))
                else:
                    sortQuery.append((sortKey, 1))  # 如果沒設定sortOrder 預設ASC
            else:
                sortQuery.append(('pubDate', -1))  # 如果沒設定sortKey 預設用發佈日期 desc
            # 分頁
            limit = kwargs.get('limit', None)
            offset = kwargs.get('offset', None)
            if not limit:
                limit = 20
            if not offset:
                offset = 0

            # 撈出資料
            article = mongo.db.Article.find(query).sort(sortQuery).skip(int(offset)).limit(int(limit))
            if article:
                return dict(result='success', article=article,total=article.count())
            return dict(result='error', message='No record found')


if __name__=='__main__':
    print(ArticleList().GetAllDataCount())
    # ArticleList().GetArticleByKey(fromDate='20170921')

