import scrapy
from scrapy import item
from ..items import rankingItem
import json
import logging

No_data = 'None'
filename = '/home/nova/webdev-lessons/scraper-scrapy/amazon_scraper/url_dump/hasbro_profile_urls.txt'
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
            # logging.warning('There is no data in the ranking section....')
        except ValueError:
            yield No_data
        yield items

        
# TESTING URL:
# https://www.amazon.com/profilewidget/bio/amzn1.account.AEQWFRM5IA7FG7DCJTEWAPYUOSAQ?view=visitor