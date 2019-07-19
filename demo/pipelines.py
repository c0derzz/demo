# -*- coding: utf-8 -*-
import os
import json
import codecs
import pymysql
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

#写入数据到mysql 如果需要可以配置到settings ITEM_PIPELINES 中来执行
class W2Mysql(object):
    def process_item(self,item,spider):
        # 日期
        day = item['day']
        # 天气
        wea = item['wea']
        # 温度
        tem = item['tem']
        # 风力
        wind = item['wind']

        # 和本地的scrapyDB数据库建立连接
        connection = pymysql.connect(
            host='localhost',  # 连接的是本地数据库
            user='root',  # 自己的mysql用户名
            passwd='123456',  # 自己的密码
            db='scrapyDB',  # 数据库的名字
            charset='utf8mb4',  # 默认的编码方式：
            cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                # 创建更新值的sql语句
                sql = """INSERT INTO WEATHER(day,wea,tem,wind)
                                VALUES (%s, %s,%s,%s,%s,%s)"""
                # 执行sql语句
                # excute 的第二个参数可以将sql缺省语句补全，一般以元组的格式
                cursor.execute(sql, (day, wea, tem, wind))
                # 提交
            connection.commit()
        finally:
            #关闭连接
            connection.close()
        return item