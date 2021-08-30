# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class QiushiPipeline:
    def process_item(self, item, spider):
        print(item)
        with open('./data/qiushi.txt', 'a',encoding='utf-8') as fp:
            fp.write(f'{str(item)}\n\n')
        return item
