import  requests, time, random, json
from hashlib import md5
from agents import *


class  youdaoSpider(object):
    
    def __init__(self):
        self.url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

        self.e = input("请输入查询单词:")
        
        self.ts = str(int(time.time()*1000))

        self.headers = headers

        self.sm = md5()
        self.sm.update("5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36".encode())
        self.bv = self.sm.hexdigest()

        self.salt = self.ts + str(random.randint(0,10))

        self.s1 = "fanyideskweb" + self.e + self.salt + "p09@Bn{h02_BIEe]$P^nG"
        self.sm2 = md5()
        self.sm2.update(self.s1.encode())
        self.sign = self.sm2.hexdigest()

        self.data = {
            "i":self.e,
            "from":"AUTO",
            "to":"AUTO",
            "smartresult":"dict",
            "client":"fanyideskweb",
            "salt":self.salt,
            "sign":self.sign,
            "ts":self.ts,
            "bv":self.bv,
            "doctype":"json",
            "version":"2.1",
            "keyfrom":"fanyi.web",
            "action":"FY_BY_REALTIME",
            "typoResult":"false",
        }

    def getPage(self):
        resp = requests.post(self.url, data=self.data, headers=self.headers)
        resp.encoding = "utf-8"
        html = resp.text
        self.parsePage(html)

    def parsePage(self, html):
        print(html)

        rDict = json.loads(html)
        print("翻译：", rDict["translateResult"][0][0]["tgt"])
        try:
            rList = rDict["smartResult"]["entrie"]
            print("解释：", "".join(rList))


    def workOn(self):
        self.getPage()


if __name__ == "__main__":
    spider = youdaoSpider()
    spider.workOn()



