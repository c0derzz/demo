# -*- coding: utf-8 -*-
import os
import json
import codecs
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DemoPipeline(object):
    def process_item(self, item, spider):
        '''
        保存爬取的数据到json中
        :param item:
        :param spider:
        :return:
        '''
        base_dir = os.getcwd()
        filename = 'D:\work-self\scrapy-demo\demo\demo\\data\\weather.json'
        with codecs.open(filename, 'a') as f:
            line = json.dumps(dict(item), ensure_ascii=False) + '\n'
            f.write(line)
        return item
