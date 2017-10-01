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

# 當勾選無碼的checkbox時 要搜尋的關鍵字 用 |  分隔 ，因為會直接拿來當regex字串
UncensoredKeyWords = "fc2|carib|10musume|加勒比|Heydouga|kin8tengoku|tokyo|1pondo|Heyzo|一本道|金8天國|東京熱|アジア天國|asiatengoku|1000giri|無碼|gachi"