import scrapy
from ..items import WawjItem

class MywawjSpider(scrapy.Spider):
    name = 'mywawj'
    allowed_domains = ['bj.5i5j.com']
    start_urls = ['https://bj.5i5j.com/ershoufang/?wscckey=a3ad0d7409b85bf5_1630652575']

    def parse(self, response):
        # print(response.text)
        li_list=response.xpath('//div[@class="list-con-box"]/ul/li')
        for li in li_list:
            name=li.xpath('./div[2]/h3/a/text()').get()
            price=li.xpath('./div[2]/div[1]/div/p[2]/text()').get()
            count_price=li.xpath('./div[2]/div[1]/div/p[1]/strong/text()').get()
            area=li.xpath('./div[2]/div[1]/p[1]/text()').get()
            guanzhu_time=li.xpath('./div[2]/div[1]/p[3]/text()').get()  #关注人数、发布房源时间、近30天带看次数等字段
            
            
            yield WawjItem(name=name, price=price, 
                           count_price=count_price, area=area,
                           guanzhu_time=guanzhu_time
                           )
            
            
