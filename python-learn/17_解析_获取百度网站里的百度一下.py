# 获取网页源码
# 解析, 解析服务器响应文件 etree.HTML()
# 打印

import urllib.request
url = "http://www.baidu.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54",
}

request = urllib.request.Request(url=url, headers=headers)
# 模拟浏览器访问网站
response = urllib.request.urlopen(request)

# 获取网页源码
content = response.read().decode("utf-8")

# 解析网页源码,获取想要数据
from lxml import etree

# 解析服务器响应的文件
tree = etree.HTML(content)
# 获取想要的数据, xpath返回值是一个list数据
result = tree.xpath("//input[@id='su']/@value")
print(type(result))
print(result[0])