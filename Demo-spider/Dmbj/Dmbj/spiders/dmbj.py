# -*- coding: utf-8 -*-
import scrapy
from ..items import DmbjItem


class DmbjSpider(scrapy.Spider):
    name = 'dmbj'
    allowed_domains = ['www.daomubiji.com']
    start_urls = ['http://www.daomubiji.com/dao-mu-bi-ji-1']

    def parse(self, response):
        item = DmbjItem()
        articles = response.xpath('//article[@class="excerpt excerpt-c3"]')
        for article in articles:
            infoList = article.xpath('./a/text()').extract()[0].split()
            item["bookTitle"] = infoList[0]
            item["zhNum"] = infoList[1]
            item["zhName"] = infoList[2]
            item["zhLink"] = article.xpath('./a/@href').extract()[0]

            yield item
        
