import urllib.request
import urllib.parse
from agents import *
import random
import json

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

headers = {"User-Agent": random.choice(lst)}

key = input("请输入要翻译的内容：")

data = {
    "i":key,
    "from":"AUTO",
    "to":"AUTO",
    "smartresult":"dict",
    "client":"fanyideskweb",
    "salt":"15511718029454",
    "sign":"4d086fa60f1fae57c736a17af50c29bc",
    "ts":"1551171802945",
    "bv":"b33a2f3f9d09bde064c9275bcb33d94e",
    "doctype":"json",
    "version":"2.1",
    "keyfrom":"fanyi.web",
    "action":"FY_BY_REALTIME",
    "typoResult":"false",
}

data = urllib.parse.urlencode(data).encode("utf-8")
req = urllib.request.Request(url, data=data, headers=headers)
resp = urllib.request.urlopen(req)
html = resp.read().decode("utf-8")
rDict = json.loads(html)
res = rDict["translateResult"][0][0]["tgt"]
print(res)