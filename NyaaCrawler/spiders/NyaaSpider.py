#coding:utf-8
from NyaaCrawler.spiders.Utility import Utility
from NyaaCrawler.items import ArticleList
import requests
import logging
import scrapy
from scrapy.http import Request
from scrapy.cmdline import execute
import re
import sys
from dateutil import parser




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
    def __init__(self, *args, **kwargs):
        super(NyaaSpider, self).__init__(*args, **kwargs)
        try:
            page = max(1, int(kwargs.get('page')))
        except (ValueError, TypeError):
            page = 1

        self.util = Utility()
        # 因為python的range不包含指定數字 所以+1
        self.page = page + 1
        self.sort = kwargs.get('sort','')
        self.q = kwargs.get('q','')
        self.sortOrder = kwargs.get('o','')
        self.fromDate = kwargs.get('fromDate','')
        self.toDate = kwargs.get('toDate','')
        self.maxage = kwargs.get('maxage','')
        self.minSize = kwargs.get('minSize','')
        self.maxSize = kwargs.get('maxSize','')
        self.NyaadevUrl = 'https://sukebei.nyaa.si/'
        self.NyaacatUrl = 'https://sukebei.pantsu.cat/feed/p/%s'

    def start_requests(self):
        NyaaDevQuery = self.util.BuildUrl(self.NyaadevUrl,q=self.q, f='0', c='2_0') + '&p=%s'
        # Rss位址 %s參數是頁數 寫死catalog
        NyaacatQuery = self.util.BuildUrl(
                                        self.NyaacatUrl, sort=self.sort, fromDate=self.fromDate, toDate=self.toDate, maxage= self.maxage,
                                        order=self.sortOrder, minSize=self.minSize, maxSize=self.maxSize, c='2', q=self.q)
        # 取得指定頁數的頁面
        for page in range(1, self.page):
            yield scrapy.Request(url=NyaaDevQuery % page, callback=self.parseNyaadev)
            yield scrapy.Request(url=NyaacatQuery % page, callback=self.parseNyaacat)

    # search NyaaDev
    # p.s. 此站不給RSS filter 直接爬page
    def parseNyaadev(self, response):
        # 匹配目前頁數
        # m = re.search("p=(\d+)", response.url)
        # if m:
        #     page = m.group(1)
        # else:
        #     page = 0
        # filename = 'NyaaDev-ArticleList-page(%s).html' % page
        # # 將html存至html檔
        # with open(filename, 'wb') as f:
        #     f.write(response.body)

        items = response.xpath('//table//tr')
        for i in items:
            try:
                videoInfo = ArticleList()
                videoInfo["title"] = i.xpath('td[2]/a/text()').extract()[0]  # 影片標題
                videoInfo["articlelink"] = self.NyaadevUrl + i.xpath('td[2]/a/@href').extract()[0]  # 文章連結
                videoInfo["torrent"] = self.NyaadevUrl + i.xpath('td[3]/a[1]/@href').extract()[0]  # 種子連結 有torrent跟磁力 只取torrent
                videoInfo["size"] = self.util.convertSize(i.xpath('td[4]/text()').extract()[0])  # size
                videoInfo["pubDate"] = self.util.strToDateTime(i.xpath('td[5]/text()').extract()[0])  # date
                videoInfo["seeder"] = i.xpath('td[6]/text()').extract()[0]  # seeder
                videoInfo["leecher"] = i.xpath('td[7]/text()').extract()[0]  # leecher
                videoInfo["downloads"] = i.xpath('td[8]/text()').extract()[0]  # downloads

                # 如果有match到文章網址 就去爬文章的預覽圖
                if (re.search('/view/\d+', videoInfo["articlelink"])):
                    yield Request(videoInfo["articlelink"], callback=self.NyaaDevDetail, meta={'videoInfo': videoInfo})
            except IndexError:
                pass
            continue

    def NyaaDevDetail(self, response):
        videoInfo = response.meta['videoInfo']
        # 取出文章頁面的description區塊
        item = response.xpath('//*[@id="torrent-description"]').extract()[0]
        # 取出description區塊的url連結
        urls = self.util.GetUrlFromHtml(item)
        # 將預覽圖存檔
        videoInfo["ImagePath"] = urls
        yield videoInfo





    # search NyaaCat by RSS feed
    def parseNyaacat(self,response):
        # 匹配目前頁數
        # m = re.search("p/(\d+)", response.url)
        # if m:
        #     page = m.group(1)
        # else:
        #     page = 0
        # filename = 'NyaaCat-ArticleList-page(%s).html' % page
        # # 將html存至html檔
        # with open(filename, 'wb') as f:
        #     f.write(response.body)

        # 取得RSS每個影片的物件
        items = response.xpath('//channel/item')

        # 取出影片資訊
        for i in items:
            videoInfo = ArticleList()
            videoInfo["title"] = i.xpath('title/text()').extract()[0] # 文章標題
            videoInfo["torrent"] = i.xpath('link/text()').extract()[0] # 種子連結
            urls = self.util.GetUrlFromHtml(i.xpath('description/text()').extract()[0])
            videoInfo["ImagePath"] = urls  # 取出預覽圖位址
            videoInfo["articlelink"] = i.xpath('guid/text()').extract()[0] # 文章連結
            videoInfo["pubDate"] = self.util.strToDateTime(i.xpath('pubDate/text()').extract()[0]) # 發佈日期
            videoInfo["size"] = self.util.convertSize(i.xpath('enclosure/@length').extract()[0]) # 檔案大小
            yield videoInfo


def gen_argv(s):
    sys.argv = s.split()
if __name__ == '__main__':
    # LOG_ENABLED 是否在console顯示log
    #gen_argv('scrapy crawl NyaaSpider -s LOG_ENABLED=False -a page=2')
    gen_argv('scrapy crawl NyaaSpider -a page=30')
    execute()