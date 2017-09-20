# -*- coding: utf-8 -*-
import pymongo
from .items import ArticleList
from scrapy.conf import settings
class NyaacrawlerPipeline(object):
    def __init__(self):
        clinet = pymongo.MongoClient(settings['MONGODB_HOST'], settings['MONGODB_PORT'])
        db = clinet[settings['MONGODB_DB']]
        self.dataset = db[settings['MONGODB_COLLECTION']]

        # 建立索引
        self.dataset.create_index([('title', pymongo.ASCENDING)] ,unique=True)


    def process_item(self, item, spider):
        print
        'MongoDBItem', item
        """ 判断类型 存入MongoDB """
        if isinstance(item, ArticleList):
            try:
                print(dict(item))
                post_id = self.dataset.insert_one(dict(item)).inserted_id
            except Exception:
                pass
        return item
