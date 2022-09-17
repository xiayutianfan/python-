from lxml import etree

# xpath解析
# 本地文件使用的是 etree.parse()
# 服务器响应的数据 response.read().decode("utf-8") .....使用的是etree.HTML()

# 解析本地文件
tree = etree.parse("16_解析_xpath的基本适用.html")
print(tree)


# 查找ul下面的li (//查找所有子孙节点, 不考虑层级关系; / 直接查找子节点)
# li_list = tree.xpath("//ul/li")

# 查找所有有id属性的标签  (/text()可用获取里面的内容)
# li_list = tree.xpath("//ul/li[@id]/text()")
# print(li_list)
# print(len(li_list))

# 查找id为l1的标签 (@id='li' 要注意引号问题)
# li_list = tree.xpath("//ul/li[@id='l1']/text()")
# print(li_list)

# 查找到id为li标签的class属性值
# li = tree.xpath("//ul/li[@id='l1']/@class")
# print(li)

# 查询id包含l的标签
# li = tree.xpath("//ul/li[contains(@id,'l')]/text()")
# print(li)

li = tree.xpath("//ul/li[starts-with(@id,'l')]/text()")
print(li)


# 如果标签是这种的话 div class="container"
# 可以这样获取    //div[@class='container']