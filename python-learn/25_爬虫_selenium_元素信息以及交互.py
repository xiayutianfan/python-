from selenium import webdriver

path = "msedgedriver.exe"
browser = webdriver.Edge(path)

url = "https://www.baidu.com"
browser.get(url)

input = browser.find_element_by_id("su")

# 获取标签里class的属性值
print(input.get_attribute('class'))

# 获取标签名
print(input.tag_name)

# 获取元素文本, 就是    <div> 获取的是这里的内容, 如果没有就是空 <div/>, 获取的是标签两边中间的内容
a = browser.find_element_by_link_text("新闻")
print(a.text)