# -*- coding: utf-8 -*-
'''
Created on 2016年1月21日

@author: zy
'''
#/html/body/div[4]/div[2]/table/tbody/tr[2]/td[2]
#/html/body/div[4]/div[2]/table/tbody/tr[2]/td[1]/a
#/html/body/div[4]/div[2]/table/tbody/tr[2]/td[2]
#/html/body/div[4]/div[2]/table/tbody/tr[2]/td[2]
#//div[4]/div[2]/table/tbody/tr[1]/th[1]
from scrapy.spider import Spider  
from scrapy.selector import Selector  
from scrapy import log  
import logging
import codecs

from tutorial.items import Price

class B2cfSpider(Spider):
    name = "b2cf"
    allowed_domains = ["hq.b2cf.cn/"]
    start_urls = [
        "http://hq.b2cf.cn/sgjg/6352_1.shtml", #农合网水果价格网址
    ]
    ELASTICSEARCH_LOG_LEVEL= logging.INFO
    
    def printhxs(self,hxs):
        for a in hxs:
            print(a.encode('utf-8'))
            
    def parse(self, response):
        #print(response)
        #print(response.xpath('//div[@class="hqListBox fl dp mt5"]/table/tbody/tr[@class="double"]').extract())
        #print(response.xpath('//html/body/div[@id="body"]/div[@class="hqListBox fl dp mt5"]/table/tbody/tr[@class="double"]').extract())
        #print(response.xpath('//tr/td').extract())
        #for sel in response.xpath('//tr[@class="double"]'):       
            #print(sel)
            #item = Price()
            #item['product'] = sel.xpath('td[1]/a/text()').extract()[0].encode('utf-8')
            #item['price'] = sel.xpath('td[2]/text()').extract()[0].encode('utf-8')
            #yield item
        target_encoding =  'utf-8'
        sel = Selector(response)
        sites = sel.xpath('//tr[@class="double"]')
        items = []
        
        look = codecs.lookup('utf-8')
        for site in sites:
            item = Price()
            product = site.xpath('td[1]/a/text()').extract()
            price = site.xpath('td[2]/text()').extract()
            
            #self.printhxs(product)
            #self.printhxs(price)
            item['product'] = [p1.encode('utf-8') for p1 in product ]
            item['price'] = [p2.encode('utf-8') for p2 in price]
            
            items.append(item)
            #items = str[items]
            #print('\xe6\x9e\xa3')
            #记录
            log.msg("拼接对象中...")
            
        log.msg("拼接结束...")
        #print(look.encode(items[0]))
        yield items[0]
            
    