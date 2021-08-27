import scrapy
from ..items import DangdangItem

class MydangdangSpider(scrapy.Spider):
    name = 'mydangdang'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://category.dangdang.com/pg1-cp01.01.02.00.00.00.html']

    def parse(self, response,**kwargs):
        pass
        
        title=response.xpath('/html/body/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li/p[1]/a/text()').extract()
        search_now_price=response.xpath('/html/body/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li/p[3]/span[1]/text()').extract()
        search_comment_num=response.xpath('/html/body/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li/p[4]/a/text()').extract()
        dd_name=response.xpath('/html/body/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li/p[5]/span[3]/a/text()').extract()
        yield DangdangItem(title=title,dd_name=dd_name,search_now_price=search_now_price,search_comment_num=search_comment_num)