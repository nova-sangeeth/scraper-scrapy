import scrapy
from ..items import rankingItem
import json
import logging

filename = ''

No_data = 'None'
class RankingSpider(scrapy.Spider):
    name = 'ranking'
    allowed_domains = ['amazon.com']
    # start_urls = ['']

    def __init__(self, filename=filename):
        if filename:
            with open(filename, 'r') as url_list:
                self.start_urls = url_list.readlines()

    def parse(self, response):
        items = rankingItem()
        try:
            resp = json.loads(response.body)
            ranking = resp.get('topReviewerInfo').get('rank')
            items['ranking'] = ranking
            page_url = response.url
            items['page_url'] = page_url
        except ValueError:
            logging.warning('There is no data in the ranking section....')
            yield No_data
        yield items

        
# TESTING URL:
# https://www.amazon.com/profilewidget/bio/amzn1.account.AEQWFRM5TESTINGONLYAPYUOSAQ?view=visitor
# https://www.amazon.com/profilewidget/bio