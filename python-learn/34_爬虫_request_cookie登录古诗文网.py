# 爬取这个网站有两个难点
# 1 是隐藏域 __VIEWSTATE    __VIEWSTATEGENERATOR 这两个类型都是hidden的
# 2 是验证码问题, 不是同一个对象访问会出现不同的验证码的, 会出现验证码一直错误

# 通过登录 然后进入主页面, 由于该网站用了反爬, 得要一步一步解决

# __VIEWSTATE: tHgFQZ4Ip2C9OnZtAHOhuJR5ysT3hcHjV9ApuBVRZwReHBMC8CyrGLs5UN9VF5WM+7YWpOEPkWgjh145dQ8nCg7tDj1i8PvQLSSlS42Ywl2WdViIpI7Kca5HiFoVt5sjtCJRL0qg0JJbnDILGpdwt4cmXwk=
# __VIEWSTATEGENERATOR: C93BE1AE
# from: http://so.gushiwen.cn/user/collect.aspx
# email: 1298311823@qq.com
# pwd: qwerqweqweqwe
# code: 0roq
# denglu: 登录

# __VIEWSTATE __VIEWSTATEGENERATOR code可能是一个变量(可以变化的值)
#   __VIEWSTATE __VIEWSTATEGENERATOR 一般情况下看不到的数据, 都在页面源代码中

import requests

# 登录页面url地址
url = "https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70"
}



# 获取页面源码, 看看有没有__VIEWSTATE的value值
response = requests.get(url=url, headers=headers)
content = response.text

from bs4 import BeautifulSoup

# 通过bs4来获取__VIEWSTATE的value值
soup = BeautifulSoup(content, "lxml")
# 返回的是列表, 所以取第一个
viewstate = soup.select("#__VIEWSTATE")[0].attrs.get("value")
viewstategenerator = soup.select("#__VIEWSTATEGENERATOR")[0].attrs.get("value")

# 获取验证码图片
code = soup.select("#imgCode")[0].attrs.get("src")
code_url = "https://so.gushiwen.cn" + code

# 使用session() 来访问验证码, 不然每次验证码对不上
session = requests.session()
response_code = session.get(url=code_url)
# 此时要使用二进制, 因为下载的是图片(content就是下载二进制的)
content_code = response_code.content
# wb就是将二进制写入到文件中
with open("code.jpg", "wb") as fp:
    fp.write(content_code)

# 获取验证码图片后, 下载到本地, 然后观察验证码, 输入到控制台,完成登录(还是手动的)
code_name = input("请输入你的验证码")

# 开始登录
url_post = "https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx"
data_post = {
    "__VIEWSTATE": viewstate,
    "__VIEWSTATEGENERATOR": viewstategenerator,
    "from": "http://so.gushiwen.cn/user/collect.aspx",
    "email": "1298311823@qq.com",
    "pwd": "qwer123456qaz",
    "code": code_name,
    "denglu": "登录"
}


# 用session来访问
response_post = session.post(url=url_post, headers=headers, data=data_post)
content_post = response_post.text

with open("gs.html", "w", encoding="utf-8") as fp:
    fp.write(content_post)