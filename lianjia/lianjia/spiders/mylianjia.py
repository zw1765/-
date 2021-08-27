import scrapy
from ..items import LianjiaItem


class MylianjiaSpider(scrapy.Spider):
    name = 'mylianjia'
    allowed_domains = ['lianjia.com']
    start_urls = ['https://sz.lianjia.com/ershoufang/pg1/']

    def parse(self, response,**kwargs):
        

        title=response.xpath('/html/body/div[4]/div[1]/ul/li/div[1]/div[1]/a/text()').extract()
        hous_name=response.xpath('/html/body/div[4]/div[1]/ul/li/div[1]/div[2]/div/a[1]/text()').extract()
        hous_info=response.xpath('/html/body/div[4]/div[1]/ul/li/div[1]/div[3]/div/text()').extract()
        totalPrice=response.xpath('/html/body/div[4]/div[1]/ul/li/div[1]/div[6]/div[1]/span/text()').extract()
        unitPrice=response.xpath('/html/body/div[4]/div[1]/ul/li/div[1]/div[6]/div[2]/span/text()').extract()
        
        yield LianjiaItem(title=title, hous_name=hous_name, totalPrice=totalPrice, unitPrice=unitPrice,hous_info=hous_info)
        

        
        