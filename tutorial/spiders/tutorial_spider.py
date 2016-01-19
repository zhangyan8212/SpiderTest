# -*- coding: utf-8 -*-
'''
Created on 2016年1月19日

@author: zy
'''
import scrapy 
'''hahaha
'''

class tutorialSpider(scrapy.Spider):
    name = "tutorial"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)