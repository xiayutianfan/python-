# 导入selenium
from selenium import webdriver

# 创建浏览器操作对象
path = "msedgedriver.exe"
# 4.0以上的selenium 是不用传递path的
# 最重要的是 首字母要大写 Edge Chrome
# 学习的同学在setting里面找到对应的project右侧找到selenium双击进入右下角specify version勾选，右侧框中换成3.3.1版本
browser = webdriver.Edge(path)

# 访问网站
url = "https://www.jd.com/"

browser.get(url)

content = browser.page_source
print(content)