# -*- coding: utf-8 -*-


BOT_NAME = 'NyaaCrawler'
SPIDER_MODULES = ['NyaaCrawler.spiders']
NEWSPIDER_MODULE = 'NyaaCrawler.spiders'
ROBOTSTXT_OBEY = False
ITEM_PIPELINES = {
   'NyaaCrawler.pipelines.NyaacrawlerPipeline': 300,
}

MONGODB_HOST = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "Nyaa"
MONGODB_COLLECTION = "Article"

# 資料庫用的日期格式
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
