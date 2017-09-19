# -*- coding: utf-8 -*-
import pymongo
from .items import ArticleList
class NyaacrawlerPipeline(object):
    def __init__(self):
        clinet = pymongo.MongoClient("localhost", 27017)
        db = clinet["Nyaa"]
        self.dataset = db["Article"]
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
