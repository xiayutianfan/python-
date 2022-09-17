# 使用urllib获取百度首页源码
import urllib.request
# 定义一个url
url = "http://www.baidu.com/"
# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)
# 获取响应中的页面的源码
content = response.read().decode("utf-8")
# 打印数据
print(content)