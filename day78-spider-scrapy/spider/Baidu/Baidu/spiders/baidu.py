# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    # 爬虫名称
    name = 'baidu'
    # 允许爬取的域名
    allowed_domains = ['www.baidu.com']
    # 初始的URL地址
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        print("*" * 50)
        with open("baidu.html", "w", encoding="utf-8") as f:
            f.write(response.text)
        print("我是parse函数执行成功后的输出.")
