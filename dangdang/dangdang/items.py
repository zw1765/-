# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DangdangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    search_now_price=scrapy.Field()
    search_comment_num=scrapy.Field()
    dd_name=scrapy.Field()
    
