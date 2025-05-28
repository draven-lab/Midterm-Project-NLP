from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class SetnSpider(CrawlSpider):
    name = 'udn_key'
    custom_settings = {
        'DOWNLOAD_DELAY': '3',
        'FEED_EXPORT_ENCODING': 'utf-8',
    }
    allowed_domains = ['udn.com']

    search_keywords = [
        '行為','習慣'
    ]

    start_urls = [f'https://udn.com/search/word/2/{keyword.replace(" ", "%20")}' for keyword in search_keywords]

    allow_list = [r'/news/story/\d+/\d+']

    rules = [Rule(LinkExtractor(allow=allow_list), callback='parse_item', follow=True)]

    def parse_item(self, response):
        title = response.css('h1::text').get()
        ps = response.css('article p::text').getall()
        content = ''.join(ps)
        url = response.url
        yield {
            'title': title,
            'content': content,
            #'url': url,
        }
