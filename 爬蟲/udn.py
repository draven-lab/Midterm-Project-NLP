from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class SetnSpider(CrawlSpider):
    name = 'udn'   # 定義spider 名稱
    custom_settings={
      'DOWNLOAD_DELAY':'3',  # 設定爬蟲時間延遲
      'FEED_EXPORT_ENCODING':'utf-8', # 設定文字編碼
    }
    allowed_domains = ['udn.com']  # 爬蟲執行網域
    
    start_urls = ['https://udn.com/news/index']  #爬蟲起始網頁
    allow_list = [r'/news/story/\d+/\d+'] #需要分析之網址格式

    # 當網址的格式符合allow_list的格式時，使用parse_item函式解析網頁，
    # 把網頁內的所有超連結加入追蹤清單中
    rules = [Rule(LinkExtractor(allow=allow_list), callback='parse_item', follow=True)]

    def parse_item(self, response):
        # 取出網頁新聞標題
        title = response.css('h1::text').get()
        # 取出網頁新聞內容
        ps = response.css('article p::text').getall()
        content = ''.join(ps)
        # 取出網址
        url = response.url
        yield {
          'title':title,
          #'content':content,
          'url':url,
        }
