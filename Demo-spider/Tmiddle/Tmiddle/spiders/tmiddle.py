# -*- coding: utf-8 -*-
import scrapy


class TmiddleSpider(scrapy.Spider):
    name = 'tmiddle'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        print("我是爬虫程序parse函数输出")
