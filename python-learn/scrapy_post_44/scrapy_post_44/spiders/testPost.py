import scrapy

import json

class TestpostSpider(scrapy.Spider):
    name = 'testPost'
    allowed_domains = ['fanyi.baidu.com']
    # post请求必须要有参数
    # start_urls没有用了, parse方法也没有用了
    # start_urls = ['https://fanyi.baidu.com/sug/']
    #
    # def parse(self, response):
    #     pass

    def start_requests(self):
        url = "https://fanyi.baidu.com/sug"
        data = {
            "kw": "final"
        }
        yield scrapy.FormRequest(url=url, formdata=data, callback=self.parse_second)

    # response 就是上面Post请求的返回值
    def parse_second(self, response):
        content = response.text
        # 编码问题, 得用json解决
        obj = json.loads(content)
        print(obj)

