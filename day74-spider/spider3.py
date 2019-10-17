import urllib.parse
import urllib.request

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",

}
url = "https://tieba.baidu.com/f?"
k = input("请输入爬取的贴吧：")

for p in range(0, 1001, 50):
    key = {
        "kw":k,
        "ie":"utf-8",
        "pn":p,
    }
    key = urllib.parse.urlencode(key)
    url += key
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req)
    html = resp.read().decode("utf-8")
    with open("t"+str(p)+".html", "w", encoding="utf-8") as f:
        f.write(html)

print("save ok")