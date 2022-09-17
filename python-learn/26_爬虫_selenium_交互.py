# 如果出现验证, 可以加一下Cookie

from selenium import webdriver

path = "msedgedriver.exe"
browser = webdriver.Edge(path)

url = "https://www.baidu.com"

browser.get(url)

# 这个是为了能让人更可观的观察, 使用睡眠, 不然太快看不清
import time
time.sleep(2)

# 获取百度一下的文本框对象

input = browser.find_element_by_id("kw")

# 在文本框输入白鹿
input.send_keys("白鹿")

time.sleep(1)

# 获取百度一下的按钮
button = browser.find_element_by_id("su")
# 点击按钮
button.click()

time.sleep(2)

# 滑动窗口到底部
js_bottom = 'document.documentElement.scrollTop=100000'
browser.execute_script(js_bottom)

time.sleep(2)

# 获取下一页的按钮, 通过xpath获取 //a[@class='n']
next = browser.find_element_by_xpath("//a[@class='n']")

# 点击下一页
next.click()

time.sleep(2)

# 回到上一页
browser.back()

# 退出
browser.quit()