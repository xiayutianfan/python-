import scrapy

from scrapy_movie_041.items import ScrapyMovie041Item


class MvSpider(scrapy.Spider):
    name = 'mv'
    # 这里直接写网站域名,不然范围太小,回调函数不能执行
    allowed_domains = ['www.ygdy8.net']
    start_urls = ['https://www.ygdy8.net/html/gndy/china/index.html']

    def parse(self, response):
        # 要第一页的名字和第二页的图片
        #//div[@class='co_content8']//td[2]/b/a[2]/text()
        #//div[@class='co_content8']//td[2]/b/a[2]/@href
        a_list = response.xpath("//div[@class='co_content8']//td[2]/b/a[2]")
        for a in a_list:
            # 获取第一页的name和第二页的链接
            name = a.xpath("./text()").extract_first()
            href = a.xpath("./@href").extract_first()
            # 第二页链接
            url = "https://www.ygdy8.net" + href
            # 对第二页的链接发起访问
            # meta是一个字典, 把name传递过去
            yield scrapy.Request(url=url, callback=self.parse_second, meta={"name": name})

    def parse_second(self, response):
        # 坑, 写span看不见, 获取到none值
        # 检查一下xpath语法是否正确, span标签有可能获取不到
        # src = response.xpath("//div[@id='Zoom']/span/img/@src").extract_first()

        src = response.xpath("//div[@id='Zoom']//img/@src").extract_first()
        # 这里就可以接收到name的值了
        name = response.meta['name']

        movie = ScrapyMovie041Item(src=src, name=name)
        yield movie