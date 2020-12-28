# Scrapy settings for amazon_scraper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'amazon_scraper'

SPIDER_MODULES = ['amazon_scraper.spiders']
NEWSPIDER_MODULE = 'amazon_scraper.spiders'
PROXY_POOL_ENABLED = True

RETRY_TIMES = 10
RETRY_HTTP_CODES = [500, 502, 503, 504, 400, 403, 404]
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'amazon_scraper (+http://www.yourdomain.com)'
# USER_AGENT = 'Mozilla/5.0 (compatible;Googlebot/2.1; +http://www.google.com/bot.html)'
# USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.55'
USER_AGENT ='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
# Obey robots.txt rules
ROBOTSTXT_OBEY = False
DEPTH_LIMIT = 1000
# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 5
# TOR_IPROTATOR_ENABLED  =  True 
# TOR_IPROTATOR_CHANGE_AFTER  =  10# number of requests made to the same IP address
# TOR_IPROTATOR_ALLOW_REUSE_IP_AFTER  =  #

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 8
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 20
# CONCURRENT_REQUESTS_PER_IP = 20

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}
# ROTATING_PROXY_LIST = [
#    #  'proxy1.com:8000',
#    #  'proxy2.com:8031',
#     # ...
# ]
# ROTATING_PROXY_LIST_PATH = '/home/novasangeeth/Code--dev/scraper-scrapy/amazon_scraper/amazon_scraper/proxy-list.txt'
# ROTATING_PROXY_LIST_PATH = '/home/nova/webdev-lessons/scraper-scrapy/amazon_scraper/amazon_scraper/proxy-lists/google-approved-list.txt'
ROTATING_PROXY_LIST_PATH = '/home/novasangeeth/Code--dev/scraper-scrapy/amazon_scraper/amazon_scraper/proxy-lists/proxy-list-3.txt'
# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
   'amazon_scraper.middlewares.AmazonScraperSpiderMiddleware': 543,
}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'amazon_scraper.middlewares.AmazonScraperDownloaderMiddleware': 543,
   # 'scrapy_proxy_pool.middlewares.ProxyPoolMiddleware': 610,
   # 'scrapy_proxy_pool.middlewares.BanDetectionMiddleware': 620,
   'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
   'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
   'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
   'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
   # 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware' :  110 , 
   # 'tor_ip_rotator.middlewares.TorProxyMiddleware' :  100 
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'amazon_scraper.pipelines.AmazonScraperPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 10
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 2.0
# Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG = True

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = [500, 502, 503, 504, 400, 403, 404, 408]
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
