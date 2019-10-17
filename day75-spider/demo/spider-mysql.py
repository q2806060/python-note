from urllib import request, parse
from agents import *
import re, time, pymysql
import csv


class Maoyanspider(object):
    def __init__(self):
        self.baseurl = "https://maoyan.com/board/4?"
        self.headers = headers
        self.page = 1
        self.db = pymysql.connect("localhost", "root", "123456", "maoyandb", charset="utf8")
        self.cursor = self.db.cursor()
    
    def getPage(self, url):
        req = request.Request(url, headers=self.headers)
        resp = request.urlopen(req)
        html = resp.read().decode("utf-8")
        self.parsePage(html)

    
    def parsePage(self, html):
        s = re.compile('<div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?"releasetime">(.*?)</p>', re.S)
        rList = s.findall(html)
        self.writeMysql(rList)
    
    def writeMysql(self, rList):
        for rt in rList:
            sql = "insert into film values(%s,%s,%s)"
            self.cursor.execute(sql,[rt[0].strip(),rt[1].strip(),rt[2].strip()[5:15]])
            self.db.commit()
        
    

    def workOn(self):
        for i in range(10):
            key = parse.urlencode({
                "offset": i*10,
            })
            url = self.baseurl + key
            self.getPage(url)
            time.sleep(0.5)
            print("已爬取%s页。" % self.page)
            self.page += 1
        self.cursor.close()
        self.db.close()

if __name__ == "__main__":
    spider = Maoyanspider()
    spider.workOn()

