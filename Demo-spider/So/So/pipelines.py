# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 导入scrapy的图片管道类
from scrapy.pipelines.images import ImagesPipeline
import scrapy

class SoPipeline(ImagesPipeline):
    # 重写ImagesPipeline
    def get_media_requests(self, item, info):
        # 交给调度器入队列，会自动将结果保存到settings.py中的IMAGES_STORE变量的路径中
        yield scrapy.Request(item["imgLink"])
        
