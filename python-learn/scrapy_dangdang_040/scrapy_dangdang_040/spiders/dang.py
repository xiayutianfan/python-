import scrapy
from scrapy_dangdang_040.items import ScrapyDangdang040Item


class DangSpider(scrapy.Spider):
    name = 'dang'
    # 如果是多页下载, 那么必须要调整 allowed_domains的范围,一般情况下,只写域名
    allowed_domains = ['search.dangdang.com']
    start_urls = ['http://search.dangdang.com/?key=%CA%C0%BD%E7%C3%FB%D6%F8/']

    base_url = "http://search.dangdang.com/?key=%CA%C0%BD%E7%C3%FB%D6%F8"
    page = 1

    def parse(self, response):

        # pipelines.py (管道) 下载数据
        # items.py 定义数据结构(你要下载什么数据,这些数据都有什么)
        # src = //ul[@id='component_59']/li/a/img/@data-original
        # alt = //ul[@id='component_59']/li/a/img/@alt
        # price = //ul[@id='component_59']/li//span[@class='search_now_price']/text()
        # author = //ul[@id='component_59']/li//p[@class='search_book_author']/span[1]/a[1]/text()
        # 所有的seletor的对象, 都可以再次调用xpath方法
        li_list = response.xpath("//ul[@id='component_59']/li")

        for li in li_list:
            # 再次调用xpath
            # 而且返回的是列表, 得使用extract要提取
            # 这个图片有懒加载, 所以src获取不到图片
            # src = li.xpath(".//a/img/@src").extract_first()

            # 第一本书的图片和其他书图片的属性不一样, 所以第一本书获取的是none值
            # 第一本书的src可以使用, 其他则不能, 得要使用@data-original
            src = li.xpath(".//a/img/@data-original").extract_first()

            # 如果能获取到src, src=src
            if src:
                src = src
            else:
                # 获取不到走这行代码; 就是第一本书
                src = li.xpath(".//a/img/@src").extract_first()

            name = li.xpath(".//a/img/@alt").extract_first()
            price = li.xpath(".//span[@class='search_now_price']/text()").extract_first()
            author = li.xpath(".//p[@class='search_book_author']/span[1]/a[1]/text()").extract_first()

            # 这里参数名不能乱写, 要和items里面的属性一一对应
            book = ScrapyDangdang040Item(src=src, name=name, author=author, price=price)

            # 获取一个book对象就交给pipelines(管道)
            yield book

# 每一页爬取的业务逻辑,基本都是一样的,所以只需要将执行的那个页码的请求再次调用parse方法
# 第二页的请求 http://search.dangdang.com/?key=%CA%C0%BD%E7%C3%FB%D6%F8&page_index=2
# 第三页就是page_index=3
            if self.page < 100:
                self.page += 1
                url = self.base_url + "&page_index" + str(self.page)
                # 怎么去调用parse方法
                # scrapy.Request就是scrapy.get请求
                # url是请求地址
                # callback是要执行的函数, 不允许加()
                yield scrapy.Request(url=url, callback=self.parse)