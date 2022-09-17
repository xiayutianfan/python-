import scrapy


class BmSpider(scrapy.Spider):
    name = 'bm'
    allowed_domains = ['https://car.autohome.com.cn/price/brand-15-29.html']
    # 注意: 如果请求的接口是html为结尾, 不用在后面加 /
    start_urls = ['https://car.autohome.com.cn/price/brand-15-29.html']

    def parse(self, response):
        names = response.xpath("//div[@class='main-title']/a/text()")
        prices = response.xpath("//span[@class='font-arial']/text()")
        for i in range(len(names)):
            name = names[i].extract()
            price = prices[i].extract()
            print("车名: " + name + ", 价格: " + str(price))