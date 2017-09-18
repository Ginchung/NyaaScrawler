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

    def start_requests(self):
        url = 'https://sukebei.nyaa.si/?q=&f=0&c=2_0&p=%s'
        # 取得前兩頁的頁面
        for page in range(1,3):
            yield scrapy.Request(url=url % page, callback=self.parse)

    def parse(self, response):
        # 匹配目前頁數
        m = re.search("p=(\d)", response.url)
        if m:
            page = m.group(1)
        filename = 'Nyaa-ArticleList-page(%s).html' % page
        # 將html存至html檔
        with open(filename, 'wb') as f:
            f.write(response.body)


def gen_argv(s):
    sys.argv = s.split()
if __name__ == '__main__':
    gen_argv('scrapy crawl NyaaSpider')
    execute()