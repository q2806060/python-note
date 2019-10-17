import requests, os
from lxml import etree
# from agents import *

class tbImgSpider(object):

    def __init__(self):
        self.tb = input("请输入要爬取的贴吧：")
        self.start = int(input("请输入起始页："))
        self.end = int(input("请输入终止页："))
        self.headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        }
        self.baseUrl = "http://tieba.baidu.com/f?"
        self.baseMainUrl = "http://tieba.baidu.com/"
        self.c = 0
        
        

    def getMainPage(self, params):
        try:
            resp = requests.get(self.baseUrl,params=params,headers=self.headers)
        except Exception as e:
            print(e)
            return
        resp.encoding = "utf-8"
        html = resp.text
        # 解析出贴吧首页的html文件
        self.parseMainPage(html)


    def parseMainPage(self, html):
        parseHtml = etree.HTML(html)
        tList = parseHtml.xpath(
            '//div[@class="t_con cleafix"]/div/div/div/a/@href'
            )
        # 解析出来的是爬取页面地址列表
        self.getPage(tList)

    def getPage(self, rList):
        for u in rList:
            try:
                resp = requests.get(self.baseMainUrl + u, headers=self.headers)
            except Exception as e:
                print(e)
                continue
            resp.encoding = "utf-8"
            html = resp.text
            # 解析得到每一页的html文件
            self.parsePage(html)


    def parsePage(self, html):
        parseHtml = etree.HTML(html)
        rList = parseHtml.xpath(
            '//div[@class="pb_content clearfix"]//div[@class="d_post_content j_d_post_content "]/img[@class="BDE_Image"]/@src'
            )
        # 得到的是每一页所有的图片地址
        self.saveImg(rList)
    
    def saveImg(self, rList):
        for i in rList:
            name = i.split('/')[-1]
            filename = os.path.dirname(__file__)
            root = os.path.join(filename,"images")
            if not os.path.exists(root):
                os.mkdir(root)
            imgname = os.path.join(filename, "images", name)
            try:
                r = requests.get(i)
            except Exception as e:
                print(e)
                continue
            with open(imgname,"wb") as f:
                f.write(r.content)
                self.c += 1
                print("已抓取%d张图片." % self.c)


    def workOn(self):
        for i in range(self.start, self.end+1):
            params = {
                "kw":self.tb,
                "pn":i*50,
            }
            self.getMainPage(params)

if __name__ == "__main__":
    spider = tbImgSpider()
    spider.workOn()
    