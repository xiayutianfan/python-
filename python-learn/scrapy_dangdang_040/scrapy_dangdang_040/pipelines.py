# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# 如果想使用管道的话, 必须在settings中开启管道 ITEM_PIPELINES
class ScrapyDangdang040Pipeline:

    # 推荐使用open_spider   close_spider
    # 在爬虫文件开始之前就执行的方法
    def open_spider(self, spider):
        self.fp = open("book.json", "w", encoding="utf-8")


    # item 就是 yield的book对象
    def process_item(self, item, spider):

        # 解决文件操作过于频繁
        # write方法必须要写一个字符串, 不允许是其他对象, 得要强转一下
        self.fp.write(str(item))

        '''
        以下方法不推荐使用, 因为每次传递过来一个对象就打开一次文件,操作IO太频繁了.

        # 第一个问题, write方法必须要写一个字符串, 不允许是其他对象, 得要强转一下
        # 第二个问题, w 会每一个对象都打开一次文件, 然后覆盖之前的内容,最后关闭文件, 得用a
        with open('book.json', 'a', encoding='utf-8') as fp:
            fp.write(str(item))
        '''



        return item

    # 在爬虫执行完之后, 执行的方法
    def close_spider(self, spider):
        self.fp.close()


import urllib.request
# 多条管道开启(下载图片)
# 1.定义管道类
# 2.在settings开启管道 'scrapy_dangdang_040.pipelines.DangDangDownloadPipelines': 301
class DangDangDownloadPipelines:
    def process_item(self, item, spider):
        url = 'http:' + item.get('src')
        fileName = './books/' + item.get('name') + '.jpg'
        urllib.request.urlretrieve(url=url, filename=fileName)
        return item

