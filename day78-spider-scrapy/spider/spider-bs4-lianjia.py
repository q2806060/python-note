from bs4 import BeautifulSoup
import pymongo
import requests
from agents import *

class spiderLianjia(object):

    def __init__(self):
        self.url = "https://hf.lianjia.com/ershoufang/"
        self.headers = headers
        self.conn = pymongo.MongoClient(host="localhost", port=27017)
        self.db = self.conn["lianjiadb"]
        self.myset = self.db["ershoufang"]


    def getPage(self):
        res = requests.get(self.url, headers=self.headers)
        res.encoding = "utf-8"
        html = res.text
        self.parsePage(html)
    
    def parsePage(self, html):
        soup = BeautifulSoup(html, "lxml")
        rList = soup.find_all("li", attrs={"class":"clear LOGCLICKDATA"})
        for r in rList:
            houseInfo = r.find("div", attrs={"class":"houseInfo"})
            infoList = houseInfo.get_text().split("|")
            name = infoList[0].strip()
            htype = infoList[1].strip()
            area = infoList[2].strip()

            positionInfo = r.find("div", attrs={"class":"positionInfo"})
            pList = positionInfo.get_text().split("-")
            flooryear = pList[0].strip()
            address = pList[1].strip()

            totalInfo = r.find("div", attrs={"class":"totalPrice"})
            totalPrice = totalInfo.get_text()
            
            unitInfo = r.find("div", attrs={"class":"unitPrice"})
            unitPrice = unitInfo.get_text()
            
            d = {
                "name":name,
                "htype":htype,
                "area":area,
                "flooryear":flooryear,
                "address":address,
                "totalPrice":totalPrice,
                "unitPrice":unitPrice,
            }

            self.myset.insert_one(d)

    
    def workOn(self):
        self.getPage()


if __name__ == "__main__":
    spider = spiderLianjia()
    spider.workOn()