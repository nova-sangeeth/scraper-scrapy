import scrapy
import json
from ..items import ProfileItem
import logging

filename = ''
No_data = "None"


class ProfileSpider(scrapy.Spider):
    name = 'profile'
    allowed_domains = ['amazon.com']
    # start_urls = ['https://www.amazon.com/hz/gamification/api/contributor/dashboard/amzn1.account.AHZLBXPETESTONLY4FHXAIWEA']

    def __init__(self, filename=filename):
        if filename:
            with open(filename, 'r') as r:
                self.start_urls = r.readlines()

    def parse(self, response):
        item = ProfileItem()
        try:
            resp = json.loads(response.body)
            helpful = resp.get('reviews').get('reviewsCountData').get('count')
            item['total_review'] = helpful
            visibility = resp.get('reviews').get('reviewsCountData').get('visibilityText')
            item['visibility_status'] = visibility
            #store the page url for reference if required.
            helpful = resp.get('helpfulVotes').get('helpfulVotesData').get('count')
            item['helpful_votes'] = helpful
            page_url = response.url
            item['page_url'] = page_url
        except ValueError:
            yield No_data
        yield item

# THE AJAX REQUEST URL FOR THE RANKING IN A PARTICULAR PROFILE IS:(replace the necessary account and run it in a file.)
# https://www.amazon.com/hz/gamification/api/contributor/dashboard/amzn1.account.AHZLBXPEMVTESTONLYHXAIWEA
# https://www.amazon.com/hz/gamification/api/contributor/dashboard
