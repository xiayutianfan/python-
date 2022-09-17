# 以下内容 如果使用版本的selenium 大概语法是
# browser.find_elements(by=By.XPATH, value='//input[@id="su"]')
# browser.find_elements(by=By.TAG_NAME, value='input')

from selenium import webdriver

path = "msedgedriver.exe"
browser = webdriver.Edge(path)
url = "https://www.baidu.com"

browser.get(url)

# 元素定位
#   根据id查找对象
# button = browser.find_element_by_id("su")

#   根据属性的属性值来获取对象
# button = browser.find_element_by_name("wd")

#   根据xpath来获取对象, 返回的是列表
# button = browser.find_element_by_xpath("//input[@id='su']")

#   根据标签名来获取对象
# button = browser.find_element_by_tag_name("input")

#   使用bs4语法来获取对象
# button = browser.find_element_by_css_selector("#su")

#   获取a标签的超链接
button = browser.find_element_by_link_text("视频")
print(button)