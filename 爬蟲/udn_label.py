from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class SetnSpider(CrawlSpider):
    name = 'udn_label'
    custom_settings = {
        'DOWNLOAD_DELAY': '3',
        'FEED_EXPORT_ENCODING': 'utf-8',
    }
    allowed_domains = ['udn.com']

    # 關鍵字列表
    search_keywords = ['行為 習慣']
    keyword_list = ['行為', '習慣']  # 用來標註 label

    start_urls = [f'https://udn.com/search/word/2/{keyword.replace(" ", "%20")}' for keyword in search_keywords]

    allow_list = [r'/news/story/\d+/\d+']

    rules = [Rule(LinkExtractor(allow=allow_list), callback='parse_item', follow=True)]

    def parse_item(self, response):
        title = response.css('h1::text').get()
        ps = response.css('article p::text').getall()
        content = ''.join(ps)
        url = response.url

        # 加上 Label：如果內文有出現關鍵字，則標記為 1，否則為 0
        label = 1 if any(keyword in content for keyword in self.keyword_list) else 0

        yield {
            'title': title,
            'content': content,
            'label': label,
            # 'url': url,  # 可以選擇要不要留網址
        }
