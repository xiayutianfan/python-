from bs4 import BeautifulSoup

# 解析本地文件 来讲bs4的基础语法

# 加载本地文件, 默认打开文件编码格式是gbk, 需要指定编码
soup = BeautifulSoup(open("21_解析_bs4的使用.html", encoding="utf-8"), 'lxml')

# 根据标签名查找标签节点, 找到的是第一个符合条件的数据, 不管层级关系?
# print(soup.a)
# 获取标签的属性和属性值
# print(soup.a.attrs)

# bs4的一些函数
# find 第一个符合条件的数据
# print(soup.find("a"))
# # 根据title条件来查找
# print(soup.find("a", title="a1"))
# # 根据class条件来查找
# print(soup.find("a", class_="321"))

# find_all
# 返回的是一个列表并且返回所有标签
# print(soup.find_all("a"))
# 如果想获取多个标签的数据, 那么参数得以列表的形式
# print(soup.find_all(["a", "span"]))
# limit的作用是查找前几个数据
# print(soup.find_all("li", limit=2))

# select
# select方法返一个列表并且返回多个数据
# print(soup.select("a"))
# 通过. 代表class, 如果class属性全是数字,那么会报错
# print(soup.select('.a321'))
# 通过# 代表id
# print(soup.select("#a123"))

# 属性选择器
# 查找a标签中有id的
# print(soup.select("a[id]"))

# 查找a标签中id是a1234的
# print(soup.select("a[id='a1234']"))


# 层级选择器
#   后代选择器
# 找到div下的 li
# print(soup.select("div li"))
# 子代选择器
# 某标签中的一级子标签
# print(soup.select("div > ul > li"))

# 找到a标签和li标签的所有对象
# print(soup.select("a, li"))

# 节点信息
#   获取节点内容, 由于返回的是列表, 所以取元素第一个
# obj = soup.select("#d1")[0]
# 如果是老版的bs4, 内容有标签是获取不到的
# print(obj.string)
# 这个是通用
# print(obj.get_text())

# 节点属性
# obj = soup.select("#p1")[0]
# 返回的是标签的名字
# print(obj.name)
# 将属性值作为一个字典返回
# print(obj.attrs)

# 获取节点的属性
obj = soup.select("#p1")[0]
print(obj.attrs.get("class"))
print(obj.get("class"))
print(obj["class"])