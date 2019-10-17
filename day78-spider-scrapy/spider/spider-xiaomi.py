from multiprocessing import Queue 
from threading import Thread
import requests, time, json
from agents import *
import urllib.parse

class spiderXiaoMi(object):

    def __init__(self):
        self.url = "http://app.mi.com/categotyAllListApi?"
        self.headers = headers
        self.urlQueue = Queue()
        self.parseQueue = Queue()
    

    # URL入队列
    def getUrl(self):
        for page in range(20):
            params = {
                "page":str(page),
                "categoryId":"2",
                "pageSize":"30",
            }
            params = urllib.parse.urlencode(params)
            fullUrl = self.url + params
            self.urlQueue.put(fullUrl)



    # get获取URL，发请求，把响应入解析队列
    def getHtml(self):
        while True:
            if not self.urlQueue.empty():
                url = self.urlQueue.get()
                # 三步走
                res = requests.get(url, headers=self.headers)
                res.encoding = "utf-8"
                html = res.text
                self.parseQueue.put(html)
            else:
                break


    # get获取html，提取并保存数据
    def parseHtml(self):
        while True:
            if not self.parseQueue.empty():
                html = self.parseQueue.get()
                hList = json.loads(html)["data"]
                for h in hList:
                    link = "http://app.mi.com/details?id="+h["packageName"]
                    d = {
                        "name":h["displayName"],
                        "link":link,
                    }
                    with open("app.json", "a", encoding="utf-8") as f:
                        f.write(str(d)+"\n")
            else:
                break



    def workOn(self):
        # URL入队列
        self.getUrl()

        # 创建线程
        t1List = []
        # 存放所有解析线程列表
        t2List = []
        # 采集线程开始执行
        for i in range(5):
            t = Thread(target=self.getHtml)
            t1List.append(t)
            t.start()
        # 阻塞等待回收采集线程
        for j in t1List:
            j.join()
        # 所有解析线程开始执行
        for i in range(5):
            t = Thread(target=self.parseHtml)
            t2List.append(t)
            t.start()
        # 阻塞等待回收解析线程
        for j in t2List:
            j.join()
    
if __name__ == "__main__":
    start = time.time()
    spider = spiderXiaoMi()
    spider.workOn()
    end = time.time()
    print("执行时间：%.2f" % (end-start))