# -*- coding: utf-8 -*-
import requests
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
    for estado in estados:
      self.cidades(token, estado)

  def to_str(self, element):
    return element.extract()[0].encode("utf-8")

  def cidades(self, token, estado):
    url = "http://www.buscabanco.org.br/Home/ObterCidades"

    payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"uf\"\r\n\r\n GO\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"__RequestVerificationToken\"\r\n\r\n TclM9F6dymqGFEeIiVhpolRXC7x6O0njujuzXuFgZtveFfABkohZt29l8d86hlyDOVbQMRDz5zadQnkTWj-eXnuK7DPMeiqTGSpX0BrOtIs1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
    headers = {
        'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        'POST /Home/ObterCidades HTTP/1.1': "",
        'Host': "www.buscabanco.org.br",
        'Connection': "keep-alive",
        'Content-Length': "141",
        'Pragma': "no-cache",
        'Cache-Control': "no-cache",
        'Accept': "*/*",
        'Origin': "http://www.buscabanco.org.br",
        'X-Requested-With': "XMLHttpRequest",
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
        'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
        'Referer': "http://www.buscabanco.org.br/",
        'Accept-Encoding': "gzip, deflate",
        'Accept-Language': "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,af;q=0.6,sq;q=0.5",
        'Cookie': "_ga=GA1.3.1240525790.1544977833; _gid=GA1.3.1564232163.1544977833; __RequestVerificationToken=2zQkVukvh8yZynJ3sKNfrBni8bWy9NotWiM94rtC0StFGbDfR06zyCi_SXyCpoMXD-fRpqFfYakjEcVTHG4Z515U5IJaQwk2d-2TCuQBsqw1; ASP.NET_SessionId=ngq3ybkr5coakmrmkj2dase3; gsScrollPos-65149036=",
        'cache-control': "no-cache"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)
