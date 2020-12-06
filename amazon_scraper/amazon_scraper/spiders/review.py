import scrapy
from ..items import AmazonScraperItem
import unicodedata
import re

class ReviewSpider(scrapy.Spider):
    name = 'review'
    # allowed_domains = ['amazon.com']
    start_urls = [
        'https://www.amazon.com/gp/product/B07HRJL27Z?pf_rd_r=A7QB96297GNS6SR3JXAM&pf_rd_p=9d9090dd-8b99-4ac3-b4a9-90a1db2ef53b&th=1',
        'https://www.amazon.com/OtterBox-COMMUTER-Case-iPhone-11/dp/B07W7F4P63/ref=zg_bs_3081461011_7?_encoding=UTF8&psc=1&refRID=C0ZGH59RZJKECSE3Z136',
        'https://www.amazon.com/Spigen-Ultra-Hybrid-Designed-iPhone/dp/B07T2NBLX9/ref=zg_bs_3081461011_9?_encoding=UTF8&psc=1&refRID=C0ZGH59RZJKECSE3Z136',
        'https://www.amazon.com/Apple-AirPods-Charging-Latest-Model/dp/B07PXGQC1Q/ref=zg_bs_12097478011_2?_encoding=UTF8&psc=1&refRID=XFYTSEEJT5T9SFP2KGZD',
        'https://www.amazon.com/TOZO-Bluetooth-Wireless-Headphones-Waterproof/dp/B07J2Z5DBM/ref=zg_bs_12097478011_7?_encoding=UTF8&psc=1&refRID=XFYTSEEJT5T9SFP2KGZD',
        'https://www.amazon.com/Samsung-Bluetooth-Wireless-Charging-Included/dp/B07MWCNR3W/ref=zg_bs_12097478011_48?_encoding=UTF8&psc=1&refRID=XFYTSEEJT5T9SFP2KGZD',
        'https://www.amazon.com/Portable-Charger-Anker-PowerCore-20100mAh/dp/B00X5RV14Y/ref=zg_bs_7073960011_3?_encoding=UTF8&psc=1&refRID=8DRCQVGGT0H3KAEDQYKH',
        'https://www.amazon.com/INIU-High-Speed-Flashlight-Powerbank-Compatible/dp/B07CZDXDG8/ref=zg_bs_7073960011_5?_encoding=UTF8&psc=1&refRID=8DRCQVGGT0H3KAEDQYKH'
        ]

    def parse(self, response):
        items = AmazonScraperItem()

        title = response.css('.a-text-bold span::text').extract()
        reviewer = response.css('.a-profile-name::text').extract()
        rating = response.xpath('.//i[@data-hook="review-star-rating"]//text()').extract()
        review = response.xpath('.//span[@data-hook="review-body"]//text()').extract()
        votes = response.css('.cr-vote-text::text').extract()
        verified_review = response.css('.a-color-state::text').extract()
        date_of_review = response.css('.review-date::text').extract()
        num_of_images = len(response.xpath('//img').extract())
        #-------------------------------
        items['title'] = title
        items['reviewer'] = reviewer
        items['rating'] = rating
        items['review'] = review
        items['votes'] = votes
        items['verified_review'] = verified_review
        items['date_of_review'] = date_of_review
        items['num_of_images'] = num_of_images
        
        yield items