# -*- coding: utf-8 -*-
import scrapy


class BancosSpider(scrapy.Spider):
    name = 'bancos'
    allowed_domains = ['http://www.buscabanco.org.br/']
    start_urls = ['http://http://www.buscabanco.org.br/']

    def parse(self, response):
        body = Selector(response)
        token = to_str(body.xpath('//*[@id="app"]/form/input/@value'))

    def to_str(self, element):
      return element.extract()[0].encode("utf-8")