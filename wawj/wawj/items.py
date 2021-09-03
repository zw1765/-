# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WawjItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
    name= scrapy.Field()
    price= scrapy.Field()
    count_price= scrapy.Field()
    area= scrapy.Field()
    guanzhu_time= scrapy.Field()