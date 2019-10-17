# -*- coding: utf-8 -*-
import scrapy
from ..items import TengxunItem


class TengxunSpider(scrapy.Spider):
    name = 'tengxun'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?start=0']
    baseurl = 'https://hr.tencent.com/position.php?start='

    def parse(self, response):
        for page in range(0, 3041, 10):
            url = self.baseurl + str(page)
            # 交给调度器，并指定解析函数
            yield scrapy.Request(url, callback=self.getHtml)
    

    def getHtml(self, response):
        item = TengxunItem()
        # 基准xpath节点对象列表
        baseList = response.xpath('//tr[@class="even"] | //tr[@class="odd"]')
        for base in baseList:
            item["zhName"] = base.xpath('./td[1]/a/text()').extract()[0]
            item["zhType"] = base.xpath('./td[2]/text()').extract()[0]
            item["zhNum"] = base.xpath('./td[3]/text()').extract()[0]
            item["zhAddress"] = base.xpath('./td[4]/text()').extract()[0]
            item["zhTime"] = base.xpath('./td[5]/text()').extract()[0]
            item["zhLink"] = base.xpath('./td[1]/a/@href').extract()[0]

            yield item