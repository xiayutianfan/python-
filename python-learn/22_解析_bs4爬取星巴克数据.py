import urllib.request

url = "https://www.starbucks.com.cn/menu/"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54"
}

request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode("utf-8")

from bs4 import BeautifulSoup

soup = BeautifulSoup(content, "lxml")
# xpath 语法是这样获取数据的 //ul[@class='grid padded-3 product']//strong/text(),
# 得要转换成bs4语法
name_list = soup.select("ul[class='grid padded-3 product'] strong")
for name in name_list:
    print(name.string)