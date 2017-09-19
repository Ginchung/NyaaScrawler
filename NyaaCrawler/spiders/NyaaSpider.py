#coding:utf-8
import requests
import logging
import scrapy
from NyaaCrawler.items import ArticleList
from scrapy.http import Request
from scrapy.cmdline import execute
import re
import json
import random
import sys


class NyaaSpider(scrapy.Spider):
    name = 'NyaaSpider'
    host = 'https://sukebei.nyaa.si/'
    logging.getLogger("requests").setLevel(logging.WARNING
                                          )  # 将requests的日志级别设成WARNING
    logging.basicConfig(
        level=logging.DEBUG,
        format=
        '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
        datefmt='%a, %d %b %Y %H:%M:%S',
        filename='cataline.log',
        filemode='w')

    # 參數page:選擇要取得幾頁資料
    # 用法:scrapy crawl NyaaSpider -a page=5
    def __init__(self, page=2, *args, **kwargs):
        super(NyaaSpider, self).__init__(*args, **kwargs)
        self.page = page

    def start_requests(self):
        NyaadevUrl = 'https://sukebei.nyaa.si/?q=&f=0&c=2_0&p=%s'
        NyaacatUrl = 'https://sukebei.pantsu.cat/search/%s'
        # 取得前兩頁的頁面
        for page in range(1, self.page):
            yield scrapy.Request(url=NyaadevUrl % page, callback=self.parseNyaadev)
            # yield scrapy.Request(url=NyaacatUrl % page, callback=self.parseNyaacat)

    # search NyaaDev
    def parseNyaadev(self, response):
        # 匹配目前頁數
        m = re.search("p=(\d+)", response.url)
        if m:
            page = m.group(1)
        filename = 'NyaaDev-ArticleList-page(%s).html' % page
        # 將html存至html檔
        with open(filename, 'wb') as f:
            f.write(response.body)

    # search NyaaCat
    def parseNyaacat(self,response):
        # 匹配目前頁數
        m = re.search("search/(\d+)", response.url)
        if m:
            page = m.group(1)
        filename = 'NyaaCat-ArticleList-page(%s).html' % page
        # 將html存至html檔
        with open(filename, 'wb') as f:
            f.write(response.body)


def gen_argv(s):
    sys.argv = s.split()
if __name__ == '__main__':
    gen_argv('scrapy crawl NyaaSpider')
    execute()