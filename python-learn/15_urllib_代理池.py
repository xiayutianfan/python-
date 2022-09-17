
proxies_pool = [
    {"http": "223.96.90.216:8085"},
    {"http": "111.3.118.247:30001"},
    {"http": "112.14.47.6:52024"},
    {"http": "47.92.113.71:80"},
    {"http": "118.163.13.200:8080"},
    {"http": "112.250.107.37:53281"},
    {"http": "221.5.80.66:3128"}
]

import random

proxies = random.choice(proxies_pool)

print(proxies)

url = "http://www.baidu.com/s?wd=ip"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54",
}

import urllib.request

request = urllib.request.Request(url=url, headers=headers)
handler = urllib.request.ProxyHandler(proxies=proxies)
opener = urllib.request.build_opener(handler)
response = opener.open(request)
content = response.read().decode("utf-8")

with open("proxy.html", "w", encoding="utf-8") as fp:
    fp.write(content)
