import scrapy
import json
from ..items import ProfileItem
import logging
filename = '/home/novasangeeth/Code--dev/scraper-scrapy/amazon_scraper/amazon-profile-url.txt'
class ProfileSpider(scrapy.Spider):
    name = 'profile'
    allowed_domains = ['amazon.in']
    # start_urls = [        
        # URL FOR THE RANKING OF A PROFILE
        # 'https://www.amazon.in/hz/gamification/api/contributor/dashboard/amzn1.account.AFMGTWLMQURCOY3RL3NSYMPCA4YA'
        # ----------------------------
        # URL_FOR THE MAIN PROFILE 
    #     'https://www.amazon.com/profilewidget/bio/amzn1.account.AEQWFRM5IA7FG7DCJTEWAPYUOSAQ?view=visitor',
    #     'https://www.amazon.com/profilewidget/bio/amzn1.account.AF74F4YECD534QQGRXDVEEU6BQAQ?view=visitor'
    # ]

    def __init__(self, filename=filename):
        if filename:
                with open(filename, 'r') as r:
                    self.start_urls = r.readlines()

    def parse (self, response):
        item = ProfileItem()
        resp = json.loads(response.body)
        try:
            ranking = resp.get('topReviewerInfo').get('rank')
            item['ranking'] = ranking
        except:
            logging.warning('Ranking is not available')
        try:
            helpful = resp.get('helpfulVotes').get('helpfulVotesData').get('count')
            item['helpful_votes'] = helpful
        except:
            logging.warning('Helpful votes not available..')
        try:
            helpful = resp.get('reviews').get('reviewsCountData').get('count')
            item['total_review'] = helpful
        except:
            logging.warning('total_review  not available..')
        yield item
            
# THE AJAX REQUEST URL FOR THE RANKING IN A PARTICULAR PROFILE IS:(replace the necessary account and run it in a file.)
# https://www.amazon.com/profilewidget/bio/amzn1.account.AEQWFRM5IA7FG7DCJTEWAPYUOSAQ?view=visitor