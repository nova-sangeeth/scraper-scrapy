import scrapy
from scrapy import item
from ..items import rankingItem
import json
import logging
class RankingSpider(scrapy.Spider):
    name = 'ranking'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/profilewidget/bio/amzn1.account.AEQWFRM5IA7FG7DCJTEWAPYUOSAQ?view=visitor']

    def parse(self, response):
        items = rankingItem()
        resp = json.loads(response.body)
        try:
            ranking = resp.get('topReviewerInfo').get('rank')
            items['ranking'] = ranking
        except:
            logging.warning('There is no data in the ranking section....')
        yield items

        
            