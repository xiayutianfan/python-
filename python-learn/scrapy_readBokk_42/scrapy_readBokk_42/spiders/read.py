import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from scrapy_readBokk_42.items import ScrapyReadbokk42Item


class ReadSpider(CrawlSpider):
    name = 'read'
    allowed_domains = ['www.dushu.com']
    # 这里有个大坑, 如果是这样是获取不到第一页的
    # start_urls = ['https://www.dushu.com/book/1003.html']
    # 得要加上第一页
    start_urls = ['https://www.dushu.com/book/1003_1.html']

    rules = (
        Rule(LinkExtractor(
            allow=r'/book/1003_\d+\.html'),
             callback='parse_item',
            # follow: 是否跟进? 按照提取链接规则进行提取
            # 如果是False的话, 只能爬取13页数据, 如果改为True能一直爬取完
             follow=True),
    )

    def parse_item(self, response):
        img_list = response.xpath("//div[@class='bookslist']//img")
        for img in img_list:
            name = img.xpath("./@alt").extract_first()
            src = img.xpath("./@data-original").extract_first()

            book = ScrapyReadbokk42Item(name=name, src=src)
            yield book

