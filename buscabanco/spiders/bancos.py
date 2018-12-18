# -*- coding: utf-8 -*-
import json
from scrapy import *

class BancosSpider(Spider):
  name = 'bancos'
  start_urls = ['http://www.buscabanco.org.br']

  def parse(self, response):
    print('Estou aqui na pagina {}'.format(response.url))
    body = Selector(response)
    token = self.to_str(body.xpath('//*[@id="app"]/form/input/@value'))
    estados = [self.to_str(estado.xpath('@value')) for estado in body.xpath('//*[@id="UF"]/option')]
    estados.pop(0)
    cookie = response.headers.getlist("Set-Cookie")
    for estado in estados:
      yield FormRequest(url = "http://www.buscabanco.org.br/Home/ObterCidades",
                        method = "POST",
                        formdata = {'__RequestVerificationToken': token, 'uf' : estado},
                        callback=self.get_cidade)
  def get_cidade(self, response):
    print(response.request)
    cidades = json.loads(response.body)
    for cidade in cidades:
        print(cidade["Municipio"])

  def get_agencias(self, response):
    

  def to_str(self, element):
    return element.extract()[0].encode("utf-8")
