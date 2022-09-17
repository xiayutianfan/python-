import urllib.request

url = "http://www.baidu.com/s?wd=ip"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54",
}

request = urllib.request.Request(url=url, headers=headers)

# response = urllib.request.urlopen(request)

proxies = {
    'http': "223.96.90.216:8085"
}

handler = urllib.request.ProxyHandler(proxies=proxies)
opener = urllib.request.build_opener(handler)
response = opener.open(request)

content = response.read().decode("utf-8")

with open("daili.html", "w", encoding="utf-8") as fp:
    fp.write(content)