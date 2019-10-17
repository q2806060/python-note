import urllib.parse
import urllib.request


headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
}
key = input("请输入要搜索的内容：")
key = urllib.parse.urlencode({"wd":key,})

url = "https://www.baidu.com/s?" + key

req = urllib.request.Request(url, headers=headers)
resp = urllib.request.urlopen(req)
html = resp.read().decode("utf-8")

with open("t.txt", "w", encoding="utf-8") as f:
    f.write(html)

print("save ok.")