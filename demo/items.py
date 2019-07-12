# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
#天气实体
class WeatherItem(scrapy.Item):
    #日期
    day = scrapy.Field()
    #天气
    wea = scrapy.Field()
    #温度
    tem = scrapy.Field()
    #风力
    wind=scrapy.Field()
    pass