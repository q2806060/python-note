from urllib import request, parse
from agents import *
import re, time, pymongo
import csv


class Maoyanspider(object):
    def __init__(self):
        self.baseurl = "https://maoyan.com/board/4?"
        self.headers = headers
        self.conn = pymongo.MongoClient("127.0.0.1", 27017)
        self.db = self.conn["maoyandb"]
        self.myset = self.db["film"]
        self.page = 1
    
    def getPage(self, url):
        req = request.Request(url, headers=self.headers)
        resp = request.urlopen(req)
        html = resp.read().decode("utf-8")
        self.parsePage(html)

    
    def parsePage(self, html):
        s = re.compile('<div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?"releasetime">(.*?)</p>', re.S)
        rList = s.findall(html)
        self.writeMongo(rList)
    
    def writeMongo(self, rList):
        # print(rList)
        for rt in rList:
            d = {
                "name":rt[0].strip(),
                "star":rt[1].strip(),
                "releasetime":rt[2].strip(),
            }
            self.myset.insert_one(d)
    
    def writePage(self, rList):
        with open("movie.csv", "a", newline="") as f:
            writer = csv.writer(f)
            for rt in rList:
                rList = list(rt)
                rList[1] = rList[1].strip()
                writer.writerow(rList)
    
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
    

if __name__ == "__main__":
    spider = Maoyanspider()
    spider.workOn()

