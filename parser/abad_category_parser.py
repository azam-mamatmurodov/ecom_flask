import requests
import json
import scrapy


class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://abad.uz/']

    def parse(self, response):
        for title in response.xpath('//div[@class="main_cats"]/a/div/text()').extract():
            print(title)
            yield {'title': title}


if __name__ == '__main__':
    spider = BlogSpider()
    spider.start_requests()