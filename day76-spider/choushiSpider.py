import requests, os 
import pymongo
from lxml import etree
from agents import *
import pymongo



class qiushiSpider(object):

    def __init__(self):
        self.url = "https://www.qiushibaike.com/text/"
        self.headers = headers
        self.conn = pymongo.MongoClient("127.0.0.1", 27017)
        self.db = self.conn["qiushidb"]
        self.myset = self.db["duanzi"]

    
    def getPage(self):
        resp = requests.get(self.url, headers=headers)
        resp.encoding = "utf-8"
        html = resp.text
        self.parsePage(html)


    def parsePage(self, html):
        parseHtml = etree.HTML(html)
        # 获取全部节点
        baseList = parseHtml.xpath('//div[contains(@id,"qiushi_tag_")]')
        for base in baseList:
            d = {}
            # 用户昵称
            if base.xpath('./div/a/h2/text()')[0]:
                username = base.xpath('./div/a/h2/text()')[0].strip()
            else:
                username = "匿名用户"
            # 段子内容
            content = base.xpath('.//div[@class="content"]/span/text()')
            c = ""
            for i in content:
                c += i.strip()
            # 评论数量
            pinglun = base.xpath('.//i[@class="number"]/text()')[0]
            # 好笑数量
            haoxiao = base.xpath('.//i[@class="number"]/text()')[1]
            d["username"] = username
            d["content"] = c
            d["pinglun"] = pinglun
            d["haoxiao"] = haoxiao
            self.saveData(d)

    

    def saveData(self, d):
        self.myset.insert_one(d)

    
    def workOn(self):
        self.getPage()   


if __name__ == "__main__":
    spider = qiushiSpider()
    spider.workOn()
