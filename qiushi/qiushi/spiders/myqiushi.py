import scrapy
from ..items import QiushiItem
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor


class MyqiushiSpider(CrawlSpider):
    name = 'myqiushi'
    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    
    rules = [
        Rule(
            
            LinkExtractor(
               
                allow=('text/page/\d/',), 
                
                restrict_xpaths = ('//ul[@class="pagination"]',)
            ),
            
            callback = 'parse',
            
            follow=True
        )
    ]
    
    def parse(self, response):
        div_list=response.xpath('//div[@class="col1 old-style-col1"]/div')
        for div in div_list:
            author=div.xpath('./div[1]/a[2]/h2/text()').get()
            href=div.xpath('./a[1]/@href').get()
            href='https://www.qiushibaike.com'+href
            
            yield scrapy.Request(
                url = href,
                callback=self.parse_detail,
                cb_kwargs={'author':author}
                )
            
    def parse_detail(self,response,**kwargs):
        author=kwargs['author']
        content=response.xpath('//div[@class="content"]/text()').getall()
        # print(content)
        content='\n'.join([con.replace('\n','') for con in content])
        yield QiushiItem(author=author,content=content)
        