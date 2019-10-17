# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DmbjItem(scrapy.Item):
    # define the fields for your item here like:
    bookTitle = scrapy.Field()
    zhNum = scrapy.Field()
    zhName = scrapy.Field()
    zhLink = scrapy.Field()
    
