# -*- coding: utf-8 -*-
import pymongo
import pymysql
from .settings import *

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DmbjPipeline(object):
    def process_item(self, item, spider):

        print("*" * 50)
        print(item['bookTitle'])
        print(item['zhName'])
        print(item['zhNum'])
        print(item['zhLink'])
        print('*' * 50)
        return item


# 存入mongodb数据库的管道
class DmbjMongoPipeline(object):

    def __init__(self):
        self.conn = pymongo.MongoClient(MONGO_HOST, MONGO_PORT)
        self.db = self.conn[MONGO_DB]
        self.myset = self.db[MONGO_SET]


    def process_item(self, item, spider):
        bookInfo = dict(item)
        self.myset.insert_one(bookInfo)
        return item

    
