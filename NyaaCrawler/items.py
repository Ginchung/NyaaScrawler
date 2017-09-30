# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


# 文章列表
class ArticleList(Item):
    site = Field() # 種子站的名稱
    title = Field()  # 標題
    articlelink = Field()  # 文章連結
    torrent = Field()  # 種子連結
    seeder = Field()
    leecher = Field()
    downloads = Field()
    size = Field()
    pubDate = Field()  # 發佈時間
    CreateTime = Field()  # 建立日期
    ImagePath = Field()  # 預覽圖位址
    IsDownload = Field()  # 是否已下載
    IsView = Field()  # 是否已觀看
