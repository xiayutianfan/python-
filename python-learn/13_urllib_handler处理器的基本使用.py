
# 使用handler来访问百度 获取网页

import urllib.request
url = "http://www.baidu.com"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54",
}

request = urllib.request.Request(url=url, headers=headers)

# 三个步骤 handler   build   open
# 获取handler对象
handler = urllib.request.HTTPHandler()
# 获取opener对象
opener = urllib.request.build_opener(handler)
# 调用open方法
response = opener.open(request)

content = response.read().decode("utf-8")
print(content)