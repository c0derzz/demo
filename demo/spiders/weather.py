# -*- coding: utf-8 -*-
import scrapy
from demo.items import WeatherItem

class WeatherSpider(scrapy.Spider):
    name = 'weather'
    allowed_domains = ['weather.com.cn']
    start_urls = ['http://www.weather.com.cn/weather/101010100.shtml']

    def parse(self, response):
        lis = response.xpath('//ul[@class="t clearfix"]/li')
        #保存每天天气信息
        items=[]
        for li in lis:
            item = WeatherItem()
            item['day'] = li.xpath('./h1/text()').extract()[0]
            item['wea'] = li.xpath('./p[@class="wea"]/text()').extract()[0]
            item['tem'] = li.xpath('./p[@class="tem"]/span/text()').extract()
            windStr=''
            for win in li.xpath('./p[@class="win"]/span'):
                windStr + win.xpath('text()').extract()[0]
            item['wind'] = windStr
            items.append(item)
        print(items)
        return items
