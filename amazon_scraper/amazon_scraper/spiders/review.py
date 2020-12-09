import scrapy
from ..items import AmazonScraperItem
import unicodedata
import re

class ReviewSpider(scrapy.Spider):
    name = 'review'
    allowed_domains = ['amazon.com']
    BaseUrl='https://www.amazon.in/Spigen-Ultra-Hybrid-Designed-iPhone/product-reviews/B07T2NBLX9/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews&pageNumber='
    start_urls = []
    for i in range(1,50):
        start_urls.append(BaseUrl+str(i))

    @staticmethod
    def get_text(selector_list):
        return "".join(selector_list).replace("\n","").strip()



    def parse(self, response):
        item = AmazonScraperItem()
        for review in response.css('.review'):
            author = review.css('.a-profile-name').extract()
            item['title'] = self.get_text(author)
            title = review.css('.review-title-content span').extract()
            item['title'] = self.get_text(title)
            review_content = review.css('.review-text-content').extract()
            item['review_content'] = self.get_text(review_content)
            verified = review.css('.review-format-strip').extract()
            item['verified'] = self.get_text(verified)
            rating = review.css('.review-title-content span').extract()
            item['rating'] = self.get_text(rating)
            date_of_review = review.css('.review-rating span').extract()
            item['date_of_review'] = self.get_text(date_of_review)
        yield item