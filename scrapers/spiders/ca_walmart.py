import scrapy
from bs4 import BeautifulSoup
from scrapers.items import ProductItem
from scrapy.crawler import CrawlerProcess

class CaWalmartSpider(scrapy.Spider):
    name = "ca_walmart"
    allowed_domains = ["walmart.ca"]
    start_urls = ["https://www.walmart.ca/en/grocery/fruits-vegetables/fruits/N-3852"]
    headers = {
            'dnt': '1',
            'accept-encoding': 'gzip, deflate, sdch, br',
            'accept-language': 'en-US,en;q=0.8',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'cache-control': 'max-age=0',
            'authority': 'www.walmart.ca',
            'cookie': 'JSESSIONID=E227789DA426B03664F0F5C80412C0BB.restapp-108799501-8-112264256; cookieLanguageType=en; deliveryCatchment=2000; marketCatchment=2001; zone=2; originalHttpReferer=; walmart.shippingPostalCode=V5M2G7; defaultNearestStoreId=1015; walmart.csrf=6f635f71ab4ae4479b8e959feb4f3e81d0ac9d91-1497631184063-441217ff1a8e4a311c2f9872; wmt.c=0; userSegment=50-percent; akaau_P1=1497632984~id=bb3add0313e0873cf64b5e0a73e3f5e3; wmt.breakpoint=d; TBV=7; ENV=ak-dal-prod; AMCV_C4C6370453309C960A490D44%40AdobeOrg=793872103%7CMCIDTS%7C17334',
            'referer': 'https://www.walmart.ca/en/grocery/fruits-vegetables/fruits/N-3852',
        }
    def parse(self, response):
        

        yield scrapy.Request(url = 'https://www.walmart.ca/en/grocery/fruits-vegetables/fruits/N-3852',callback = self.parse_item,  cookies={'currency': 'USD', 'country': 'UY'},meta={'dont_merge_cookies': True},headers=self.headers)
    
    
    def parse_item(self, response):
        content = response.selector.xpath('//*[@id="shelf-thumbs"]/div')
        list_content = content.css('article>div>a::attr(href)').getall()
        link = list_content[0]
        print("LINK -> "+str(link))
        url2 = 'https://www.walmart.ca'+str(link)
        yield scrapy.Request(url = url2,callback = self.parse_intern_item,cookies={'currency': 'USD', 'country': 'UY'},meta={'dont_merge_cookies': True},headers=self.headers)
    def parse_intern_item(self,response):
        product_type = response.xpath('body').get()
        soup = BeautifulSoup(product_type, 'html.parser')
        print(str(type(response.request)))
        print(soup)




