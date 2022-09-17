# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyDangdang040Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 你要下载什么数据,这些数据都有什么

    # 图片
    src = scrapy.Field()
    # 书名
    name = scrapy.Field()
    # 作者
    author = scrapy.Field()
    # 价格
    price = scrapy.Field()
