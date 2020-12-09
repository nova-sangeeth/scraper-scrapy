# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exporters import CsvItemExporter, JsonItemExporter
from .items import AmazonScraperItem
from .spiders import review
import unicodedata
import json

   
class AmazonScraperPipeline:
    def open_spider(self, review):
        self.file = open('items.json', 'w')

    def close_spider(self, review):
        self.file.close()

    def process_item(self, AmazonScraperItem, review):
        line = json.dumps(ItemAdapter(AmazonScraperItem).asdict()) + "\n"
        self.file.write(line)
        return AmazonScraperItem 