#coding:utf-8
from NyaaCrawler.spiders.Utility import Utility
from NyaaCrawler.items import ArticleList
import requests
import logging
import scrapy
from scrapy.http import Request
from scrapy.cmdline import execute
import re
import json
import random
import sys




class NyaaSpider(scrapy.Spider):
    name = 'NyaaSpider'
    host = 'https://sukebei.nyaa.si/'
    # logging.getLogger("requests").setLevel(logging.WARNING
    #                                       )  # 将requests的日志级别设成WARNING
    # logging.basicConfig(
    #     level=logging.DEBUG,
    #     format=
    #     '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    #     datefmt='%a, %d %b %Y %H:%M:%S',
    #     filename='cataline.log',
    #     filemode='w')

    # 參數page:選擇要取得幾頁資料
    # 用法:scrapy crawl NyaaSpider -a page=5
    def __init__(self, page=2, *args, **kwargs):
        super(NyaaSpider, self).__init__(*args, **kwargs)
        try:
            page = max(1, int(page))
        except (ValueError, TypeError):
            page = 1

        self.util = Utility()
        # 因為python的range不包含指定數字 所以+1
        self.page = page + 1
        self.sort = ''
        self.searchkeyword = ''
        self.category  = ''
        self.sortOrder = ''
        self.sortKey = ''
        self.fromDate = ''
        self.toDate = ''
        self.maxage = ''
        self.minSize = ''
        self.maxSize = ''


    def start_requests(self):
        NyaadevUrl = 'https://sukebei.nyaa.si/?q=&f=0&c=2_0&p=%s'
        # Rss位址 %s參數是頁數
        NyaacatUrl = 'https://sukebei.pantsu.cat/feed/p/%s?'
        NyaacatQuery = self.util.NyaaCatBuildUrl(
                                        NyaacatUrl, sort=self.sort, fromDate=self.fromDate, toDate=self.toDate, maxage=self.maxage,
                                        order=self.sortOrder, minSize=self.minSize, maxSize=self.maxSize, c=self.category)
        # 取得指定頁數的頁面
        for page in range(1, self.page):
            # yield scrapy.Request(url=NyaadevUrl % page, callback=self.parseNyaadev)
            # 組合出NyaaCat的Query Url
            yield scrapy.Request(url=NyaacatQuery % page, callback=self.parseNyaacat)

    # search NyaaDev
    # p.s. 此站不給RSS filter 直接爬page
    def parseNyaadev(self, response):
        # 匹配目前頁數
        m = re.search("p=(\d+)", response.url)
        if m:
            page = m.group(1)
        filename = 'NyaaDev-ArticleList-page(%s).html' % page
        # 將html存至html檔
        with open(filename, 'wb') as f:
            f.write(response.body)





    # search NyaaCat by RSS feed
    def parseNyaacat(self,response):
        # 匹配目前頁數
        m = re.search("p/(\d+)", response.url)
        if m:
            page = m.group(1)
        else:
            page = 0
        filename = 'NyaaCat-ArticleList-page(%s).html' % page
        # 將html存至html檔
        with open(filename, 'wb') as f:
            f.write(response.body)

        # 取得RSS每個影片的物件
        items = response.xpath('//channel/item')
        # 取出影片資訊
        for i in items:
            videoInfo = ArticleList()
            videoInfo["title"] = i.xpath('title/text()').extract()[0] # 文章標題
            videoInfo["torrent"] = i.xpath('link/text()').extract()[0] # 種子連結
            videoInfo["ImagePath"] = i.xpath('description/text()').extract()[0] # 取出預覽圖位址
            videoInfo["articlelink"] = i.xpath('guid/text()').extract()[0] # 文章連結
            videoInfo["pubDate"] = i.xpath('pubDate/text()').extract()[0] # 發佈日期
            videoInfo["size"] = i.xpath('enclosure/@length').extract()[0] # 檔案大小
            yield videoInfo


def gen_argv(s):
    sys.argv = s.split()
if __name__ == '__main__':
    # LOG_ENABLED 是否在console顯示log
    gen_argv('scrapy crawl NyaaSpider -s LOG_ENABLED=False -a page=2')
    # gen_argv('scrapy crawl NyaaSpider -a page=2')
    execute()