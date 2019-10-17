# -*- coding: utf-8 -*-
import scrapy
import urllib.parse
from ..items import SoItem
import json

class SoSpider(scrapy.Spider):
    name = 'so'
    allowed_domains = ['image.so.com']
    base_url = 'http://image.so.com/zj?'
    # 重写start_requests()方法
    def start_requests(self):
        # 想办法拼接URL地址，发送给调度器
        for page in range(3):
            params = {
                'ch':'beauty',
                'sn':str(page*30),
                'listtype':'new',
                'temp':'1',
            }
            # 完成1个完整的json文件的地址，发送给调度器如队列
            url = self.base_url + urllib.parse.urlencode(params)
            yield scrapy.Request(url, callback=self.parseImg)

    def parseImg(self, response):
        item = SoItem()
        # 获取响应的文本内容
        html = response.text
        html = json.loads(html)
        for img in html['list']:
            item["imgLink"] = img["qhimg_url"]
            yield item