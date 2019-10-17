# -*- coding: utf-8 -*-
import scrapy


class DaneiSpider(scrapy.Spider):
    name = 'danei'
    allowed_domains = ['tts.tmooc.cn']
    start_urls = ['http://tts.tmooc.cn/']

    def parse(self, response):
        pass
