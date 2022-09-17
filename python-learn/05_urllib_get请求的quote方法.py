import urllib.request
import urllib.parse

# wd= 后面直接写白鹿是不行的,得要转换
url = "https://www.baidu.com/s?wd="

headers = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54"
}

# 将白鹿转换成unicode编码格式
name = urllib.parse.quote("白鹿")

url = url + name

request = urllib.request.Request(url = url, headers = headers)

response = urllib.request.urlopen(request)

content = response.read().decode("utf-8")

print(content)