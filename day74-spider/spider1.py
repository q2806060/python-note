import urllib.request, urllib.parse

url = "http://www.baidu.com/s?"
key = urllib.parse.urlencode({"wd":"美女"})
url += key
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
}

request = urllib.request.Request(url, headers=headers)

resp = urllib.request.urlopen(request)
html = resp.read().decode("utf-8")
print(resp.geturl())