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


category = "testing_items"
filename  = "testing_rankings"
extension = ".csv"

class AmazonScraperPipeline:
    def __init__(self):

        self.file = open(f"{filename}-{category}{extension}", 'wb')
        self.exporter = CsvItemExporter(self.file)
        self.exporter.start_exporting()
    
    def close_spider(self, review):
        self.exporter.finish_exporting()
        self.file.close()   
        
    def process_item(self, ProfileItem, review):
        self.exporter.export_item(ProfileItem)
        return ProfileItem
   
