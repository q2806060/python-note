import requests, lxml, json, csv, os
from agents import *

class doubanMovie(object):
     
    def __init__(self):
        self.baseUrl = "https://movie.douban.com/j/chart/top_list?"
        self.mt = input("请输入要爬取的电影类型：")
        self.mc = int(input("请输入要去取的电影个数："))
        self.headers = headers
        self.d = {
            "剧情":11,
            "喜剧":24,
            "动作":5,
            "爱情":13,
            "科幻":17,
            "动画":25,
            "悬疑":10,
            "惊悚":19,
            "恐怖":20,
            "纪录片":1,
            "短片":23,
            "情色":6,
            "同性":26,
            "音乐":14,
            "歌舞":7,
            "家庭":28,
            "儿童":8,
            "传记":2,
            "历史":4,
            "战争":22,
            "犯罪":3,
            "西部":27,
            "奇幻":16,
            "冒险":15,
            "灾难":12,
            "武侠":29,
            "古装":30,
            "运动":18,
            "黑色电影":31,
        }
        self.typeM = self.d[self.mt]
        self.num = 0

    def getPage(self):
        params = {
            "type":self.typeM,
            "interval_id":"100:90",
            "action":"",
            "start": 0,
            "limit": self.mc,
        }
        resp = requests.get(self.baseUrl, params=params, headers=self.headers)
        resp.encoding = "utf-8"
        html = resp.text
        self.parsePage(html)

    
    def parsePage(self, html):
        mList = json.loads(html)
        for movie in mList:
            self.saveData(movie)


    def saveData(self, movie):
        movie_name = movie["title"]
        movie_score = movie["score"]
        mList = [movie_name, movie_score]
        with open("movies.csv","a", newline="") as m:
            self.num += 1
            writer = csv.writer(m)
            writer.writerow(mList)
            print("已爬取%d个电影." % self.num)



    def workOn(self):
        self.getPage()



if __name__ == "__main__":
    spider = doubanMovie()
    spider.workOn()