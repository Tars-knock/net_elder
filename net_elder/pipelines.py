# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from sqlalchemy.orm import Session

from net_elder.items import NetElderItem
from utils.mysqlDriver import Driver, Url


class NetElderPipeline:
    def process_item(self, item, spider):
        return item


def url_convert(item: NetElderItem):
    res = Url(
        url=item.get('locate_url'),
        title=item.get('title'),
        description=item.get('description')
    )
    return res


class MysqlPipeline:
    def __init__(self):
        self.sqlSession = None

    def open_spider(self, spider):
        self.sqlSession = Driver()

    def process_item(self, item, spider):
        self.sqlSession.insert_url(url_convert(item))
        return item
