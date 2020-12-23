import scrapy
import json
from ..items import ProfileItem
import logging

filename = '/home/novasangeeth/Code--dev/scraper-scrapy/amazon_scraper/url_dump/think_fun_profile.txt'

class ProfileSpider(scrapy.Spider):
    name = 'profile'
    allowed_domains = ['amazon.com']
    # start_urls = []
    def __init__(self, filename=filename):
        if filename:
                with open(filename, 'r') as r:
                    self.start_urls = r.readlines()

    def parse (self, response):
        item = ProfileItem()
        resp = json.loads(response.body)
        try:
            helpful = resp.get('helpfulVotes').get('helpfulVotesData').get('count')
            item['helpful_votes'] = helpful
        except:
            logging.debug('Helpful votes not available..')
        try:
            helpful = resp.get('reviews').get('reviewsCountData').get('count')
            item['total_review'] = helpful
        except:
            logging.debug('total_review  not available..')
        try:
            item['page_url'] = response.request.url
        except:
            logging.debug('The url is not available.')

        yield item
            
# THE AJAX REQUEST URL FOR THE RANKING IN A PARTICULAR PROFILE IS:(replace the necessary account and run it in a file.)
# https://www.amazon.com/hz/gamification/api/contributor/dashboard/amzn1.account.AHZLBXPEMVGLNEEXYCZ4FHXAIWEA
