import urllib.request
import urllib.parse
import json

# post请求

url = "https://fanyi.baidu.com/sug"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54"
}

data = {
    "kw":"china"
}

# post请求的参数, 必须要进行编码
data = urllib.parse.urlencode(data).encode("utf-8")

# post请求是不会拼接在url后面的, 而是需要放在请求对象定制的参数中
request = urllib.request.Request(url, data, headers)

# 发送请求

response = urllib.request.urlopen(request)

content = response.read().decode("utf-8")

obj = json.loads(content)

print(obj)