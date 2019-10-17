import urllib.request
import urllib.parse
from agents import *
import random

url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1551241062746&di=c2250d4b3c206ace3dd6c3682ced606d&imgtype=0&src=http%3A%2F%2Fwww.windows7en.com%2Fuploads%2Fallimg%2F141222%2F1-141222102029394.jpg"
headers = {
    "User-Agent":random.choice(lst),
}

req = urllib.request.Request(url, headers=headers)
resp = urllib.request.urlopen(req)
html = resp.read()
with open("p.jpg", "wb") as p:
    p.write(html)
print("save ok.")
