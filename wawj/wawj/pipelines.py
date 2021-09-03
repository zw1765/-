# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class WawjPipeline:

    
    def process_item(self, item, spider):
        print(item)
        self.db=pymysql.connect(
            user='root',password='Uplooking_123',
            database='spiders'
            )
        self.cur=self.db.cursor()
        try:
            sql='insert into wawj(name,price,count_price,area,guanzhu_time) values("%s","%s","%s万","%s","%s")'%(item['name'],item['price'],item['count_price'],item['area'],item['guanzhu_time'])
            self.cur.execute(sql)
            self.db.commit()
        except Exception as e:
            print(e)
        else:
            
            print(item, 'ok!')
        return item
