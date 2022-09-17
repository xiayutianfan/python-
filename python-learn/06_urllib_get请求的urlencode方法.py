import urllib.request
import urllib.parse

# urlencode 应用场景: 多个参数的时候

# https://www.baidu.com/s?wd=%白鹿&sex=女

# data = {
#     "wd" : "白鹿",
#     "sex" : "女"
# }
#
# a = urllib.parse.urlencode(data)
# print(a)

base_url = "https://www.google.com.hk/search?"

data = {
    "q":"白鹿"
}

data = urllib.parse.urlencode(data)
# 请求资源路径
url = base_url + data

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54"
}

request = urllib.request.Request(url = url, headers = headers)

response = urllib.request.urlopen(request)

content = response.read().decode("utf-8")

print(content)
