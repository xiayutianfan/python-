import urllib.request

url = "http://www.baidu.com/"
response = urllib.request.urlopen(url)

#一个类型和六个方法 -- <class 'http.client.HTTPResponse'>
# print(type(response))

content = response.read()

# 返回状态码
# print(response.getcode())

# 返回url地址
# response.geturl()

# 获取状态信息
# response.getheaders()
