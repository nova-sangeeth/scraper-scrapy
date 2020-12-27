# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exporters import CsvItemExporter, JsonItemExporter
from .items import AmazonScraperItem, ProfileItem
from .spiders import review
import unicodedata
class AmazonScraperPipeline:
    def __init__(self):
        self.file = open("kids_against_maturity_profile_ranking.csv", 'wb')
        self.exporter = CsvItemExporter(self.file)
        # self.exporter = JsonItemExporter(self.file, encoding='utf-8')
        self.exporter.start_exporting()
    
    def close_spider(self, review):
        self.exporter.finish_exporting()
        self.file.close()
        
    def process_item(self, ProfileItem, review):
        self.exporter.export_item(ProfileItem)
        return ProfileItem
   