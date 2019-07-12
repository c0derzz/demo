# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DemoPipeline(object):
    def process_item(self, item, spider):
        print("-----process_item excute-----",spider.name)
        return item
    def open_spider(self,spider):
        print("-----open_spider excute-----",spider.name)
    def close_spider(self,spider):
        print("-----close_spider excute-----",spider.name)
