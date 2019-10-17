# -*- coding: utf-8 -*-
import scrapy
# from 项目目录名.模块名 import 类名
# from Csdn.items import CsdnItem
from ..items import CsdnItem


class CsdnSpider(scrapy.Spider):
    name = 'csdn'
    # 允许爬取的域名
    allowed_domains = ['blog.csdn.net']
    # 起始URL地址
    start_urls = ['https://blog.csdn.net/qq_41185868/article/details/87886811']

    def parse(self, response):
        item = CsdnItem()
        # 提取3个数据
        # response.xpath得到的结果为选择器对象[<selector....>]
        # extract()函数从选择器中取出结果
        item['title'] = response.xpath('//h1[@class="title-article"]/text()').extract()[0]
        item['time'] = response.xpath('//div[@class="article-bar-top"]/span[@class="time"]/text()').extract()[0]
        item['number'] = response.xpath('//span[@class="read-count"]/text()').extract()[0]

        yield item