import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractor import LinkExtractor
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import requests
import re
import csv
from random import randint




class QuotesSpider(CrawlSpider):#scrapy.Spider):
    name = "quotes" 
    DOWNLOADER_MIDDLEWARES = {
        'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 1
    }
    DOWNLOAD_DELAY = 10
    RANDOMIZE_DOWNLOAD_DELAY = True
    USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    custom_settings = {
        'DOWNLOAD_TIMEOUT': 10,
        'ROBOTSTXT_OBEY' : False,
        'HTTPERROR_ALLOWED_CODES' : [403, 404, 409, 503],
        'RETRY_ENABLED' : True,
    }

    

    def start_requests(self):
        link = 'https://rateyourmusic.com/customchart?page=%d&chart_type=top&type=album&year=alltime&genre_include=1&include_child_genres=1&genres=&include_child_genres_chk=1&include=both&origin_countries=&limit=none&countries=' 
        page_urls = [link % i for i in range(1,21)]
        #proxy_from_url = "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list.txt" 
        #proxy_list = re.findall('(\d+.\d+.\d+.\d+:\d+)', requests.get(proxy_from_url).text)

        with open('rymData.csv', 'w') as f:
                f.write('artist rymrat prat reviews\n')
                f.close()

        for page in page_urls:
            yield scrapy.Request(url=page, 
                                callback=self.parse, 
                                method='GET', 
                                meta={'proxy': '185.23.64.100:3130'}, 
                                #headers=header,
                                dont_filter = True)

    def parse(self, response):

        table = response.xpath('.//table[contains(@class,"mbgen")]/*')
        artists = table.xpath('.//span[contains(@class, "chart_detail_line1")]/a[1]/text()').extract()
        ratings= table.xpath('.//div[contains(@class, "chart_stats")]//b/text()').extract()
        
        with open('rymData.csv', 'a') as ratcsv:
            ratwriter = csv.writer(ratcsv, delimiter=' ')
            for i in range(len(artists)):
                ratwriter.writerow([artists[i]] + ratings[3*i:3*(i+1)])

#process = CrawlerProcess(get_project_settings())
#process.crawl('quotes')
#process.start() 