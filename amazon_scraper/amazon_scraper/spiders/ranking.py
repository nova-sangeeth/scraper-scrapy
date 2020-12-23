import scrapy
from scrapy import item
from ..items import rankingItem
import json
import logging


filename = '/home/novasangeeth/Code--dev/scraper-scrapy/amazon_scraper/url_dump/think_fun_profile.txt'
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
        resp = json.loads(response.body)
        ranking = resp.get('topReviewerInfo').get('rank')
        items['ranking'] = ranking
        # logging.warning('There is no data in the ranking section....')
        yield items

        
# TESTING URL:
# https://www.amazon.com/profilewidget/bio/amzn1.account.AEQWFRM5IA7FG7DCJTEWAPYUOSAQ?view=visitor