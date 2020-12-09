import scrapy
from ..items import AmazonScraperItem
from scrapy.http import Request
class ReviewSpider(scrapy.Spider):
    name = 'review'
    allowed_domains = ['amazon.in']
    # start_urls='https://www.amazon.in/Apple-MacBook-Air-13-3-inch-MQD32HN/product-reviews/B073Q5R6VR/ref=cm_cr_getr_d_paging_btm_next_3?ie=UTF8&reviewerType=all_reviews&pageNumber='
    BaseUrl='https://www.amazon.in/Apple-MacBook-Air-13-3-inch-MQD32HN/product-reviews/B073Q5R6VR/ref=cm_cr_getr_d_paging_btm_next_3?ie=UTF8&reviewerType=all_reviews&pageNumber='
    start_urls = []
    for i in range(0,25):
        start_urls.append(BaseUrl+str(i))

    @staticmethod
    def get_text(selector_list):
        return "".join(selector_list).replace("\n","").strip()



    def parse(self, response):
        item = AmazonScraperItem()
        for review in response.css('.review'):
            author = review.css('.a-profile-name ::text').extract()
            item['author'] = self.get_text(author)

            author_profile_url = review.css(' a.a-profile ::attr(href)').extract()
            item['author_profile_url'] = self.get_text(author_profile_url)

            title = review.css('.review-title-content span ::text').extract()
            item['title'] = self.get_text(title)

            review_content = review.css('.review-text-content ::text').extract()
            item['review_content'] = self.get_text(review_content)

            verified = review.css('.review-format-strip ::text').extract()
            item['verified'] = self.get_text(verified)

            rating = review.css('.review-rating span ::text').extract()
            item['rating'] = self.get_text(rating)

            date_of_review = review.css('.review-date ::text').extract()
            item['date_of_review'] = self.get_text(date_of_review)
            
            votes_helpful = review.css('.cr-vote-text ::text').extract()
            item['votes_helpful'] = self.get_text(votes_helpful)

            image_num = review.css('.review-image-tile-section ::attr(src)').extract()
            item['image_num'] = len(image_num)

            num_of_comments = review.css('.review-comment-total ::text').extract()
            item['num_of_comments'] = self.get_text(num_of_comments)

            yield item


            # next_page = response.css('.a-pagination > .a-last a')
            # if next_page:
            #     next_page_link = "https://www.amazon.in/Apple-MacBook-Air-13-3-inch-MQD32HN/product-reviews/B073Q5R6VR/ref=cm_cr_arp_d_paging_btm_3?ie=UTF8&amp;pageNumber=3&amp;reviewerType=all_reviews" # get href link here
            #     yield Request(next_page_link,callback=self.parse)
