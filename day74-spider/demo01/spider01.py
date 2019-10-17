import urllib.parse
import urllib.request
import random, time
from agents import *

class Baiduspider(object):
    def __init__(self):
        self.baseurl = "https://tieba.baidu.com/f?"
    
    def getPage(self, url, lst):
        req = urllib.request.Request(url, headers={"User-Agent":random.choice(lst)})
        resp = urllib.request.urlopen(req)
        html = resp.read().decode("utf-8")
        return html
    
    def parsePage(self):
        pass
    
    def writePage(self, filename, html):
       with open(filename, "w", encoding="utf-8") as f:
           f.write(html)

    def workOn(self):
        name = input("请输入贴吧名：")
        start = int(input("请输入开始爬取页："))
        end = int(input("请输入终止页："))
        key = urllib.parse.urlencode({"kw":name})
        for page in range(start, end+1):
            pn = (page - 1) * 50
            url = self.baseurl + key + "&pn=" + str(pn)

            html = self.getPage(url, lst)
            filename = "第"+str(page)+"页.html"
            self.writePage(filename, html)
            print("第%s页爬取成功" % page)

if __name__ == "__main__":
    start = time.time()
    spider = Baiduspider()
    spider.workOn()
    end = time.time()
    print("执行时间：%.2f秒" % (end - start))
        