# 使用edge无界面浏览器有毒, selenium版本只能是 3.141的
# 可以用chrome, 使用教程 https://www.bilibili.com/video/BV1Db4y1m7Ho?p=83&spm_id_from=pageDriver&vd_source=08b490f15a36482d2afb1bfff53292fb

import time
from msedge.selenium_tools import EdgeOptions
from msedge.selenium_tools import Edge

# 以下代码相当于写死的
def share_browser():
    # 实现无可视化界面操作
    options = EdgeOptions()
    # 使用谷歌内核，（至于为什么没有edge内核，我在库里找不到相关代码）
    options.use_chromium = True
    # 这里和谷歌浏览器不一样的是我们不需要加入--，在headless和disable-gpu前面
    options.add_argument('headless')
    options.add_argument('disable-gpu')
    # 实现规避检测
    options.add_argument('--disable-blink-features=AutomationControlled')
    # 实例化浏览器对象,替代了原来的实例化浏览器对象
    browser = Edge(executable_path=r"msedgedriver.exe", options=options)
    return browser


browser = share_browser()
# 向网站发送请求
browser.get('https://www.baidu.com/')
# 输出网址页面代码r
print(browser.save_screenshot("jd.png"))
# 时间停留是2秒
time.sleep(2)
# 关闭窗口
browser.quit()