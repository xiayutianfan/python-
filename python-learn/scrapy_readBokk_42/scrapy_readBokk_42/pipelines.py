# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScrapyReadbokk42Pipeline:

    def open_spider(self, spider):
        self.fp = open("book.json", "w", encoding="utf-8")

    def process_item(self, item, spider):
        self.fp.write(str(item))
        return item

    def close_spider(self, spider):
        self.fp.close()


# 可以加载settings文件
from scrapy.utils.project import get_project_settings
import pymysql
# 自己造一条管道, 并且去settings配置
class MySqlPipeline:

    # 连接mysql
    def open_spider(self, spider):
        settings = get_project_settings()
        self.host = settings["DB_HOST"]
        self.port = settings["DB_PORT"]
        self.user = settings["DB_USER"]
        self.password = settings["DB_PASSWORD"]
        self.db = settings["DB_DB"]
        self.charset = settings["DB_CHARSET"]

        self.connect()
# 这几个参数是必须的
    def connect(self):
        self.con = pymysql.connect(
            host = self.host,
            port = self.port,
            user = self.user,
            password = self.password,
            db = self.db,
            charset = self.charset
        )
        # 这个是执行sql语句的
        self.corsor = self.con.cursor()


    def process_item(self, item, spider):

        sql = 'insert into book(name, src) values("{}", "{}")'.format(item['name'], item['src'])
        self.corsor.execute(sql)
        self.con.commit()

        return item


    def close_spider(self, spider):
        self.corsor.close()
        self.con.close()
