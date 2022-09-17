import scrapy


class BaiduSpider(scrapy.Spider):
    # 爬虫的名字, 用于运行爬虫的时候使用的值
    name = 'baidu'
    # 允许访问的域名
    allowed_domains = ['www.baidu.com']
    # 起始的url地址, 指的是第一次要访问的域名
    start_urls = ['http://www.baidu.com/']

    # 是执行start_urls之后 执行的方法, 方法中的response就是返回的对象
    # 相当于 response = urllib.request.urlopen()
    #       response = requests.get()
    def parse(self, response):
        print("在settings.py里面把ROBOTSTXT_OBEY这个协议注释掉~")
