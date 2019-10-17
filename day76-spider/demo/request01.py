import requests, re, csv
from agents import *

class Tarenaspider(object):
    def __init__(self):
        self.url = "http://code.tarena.com.cn/"
        self.headers = headers
        self.auth = ("tarenacode", "code_2013")
        

    def getPage(self):
        resp = requests.get(self.url, auth=self.auth, headers=self.headers)
        resp.encoding = "utf-8"
        html = resp.text
        self.writePage(html)

    def writePage(self, html):
        p = re.compile("<a href=.*?>(.*?)/</a>", re.S)
        rList = p.findall(html)
        with open("Note.csv", "w", newline="") as f:
            writer = csv.writer(f)
            for r in rList:
                if r != "..":
                    writer.writerow([r])
        





if __name__ =="__main__":
    spider = Tarenaspider()
    spider.getPage()