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
            # 链接规则
            LinkExtractor(
                # allow：满足括号中“正则表达式”的值会被提取，如果为空，则全部匹配。
                allow=('text/page/\d/',), # 允许href的值
                # restrict_xpaths：使用xpath表达式，和allow共同作用过滤链接。
                restrict_xpaths = ('//ul[@class="pagination"]',)
            ),
            # 回调函数
            callback = 'parse',
            # 跟随爬取
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
        