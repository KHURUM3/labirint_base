import scrapy
from urllib.parse import urljoin
import json


class LabirintspiderSpider(scrapy.Spider):
    name = 'labirintspider'

    # custom_settings = {
    #     'FEEDS': {'data/%(name)s_%(time)s.csv': {'format': 'csv', }}
    # }
    # allowed_domains = ['www.labirint.ru']
    # start_urls = ['http://www.labirint.ru/']

    def start_requests(self):
        keyword_list = ['стивен кинг']
        for keyword in keyword_list:
            labirint_search_url = f'https://www.labirint.ru/search/{keyword}/?stype=0&page=15'
            yield scrapy.Request(url=labirint_search_url, callback=self.discover_books_urls, meta={'keyword': keyword, 'page': 15})

    def discover_books_urls(self, response):
        page = response.meta['page']
        keyword = response.meta['keyword']

        search_books = response.css("div.genres-carousel__item")
        for book in search_books:
            relative_url = book.css("a.product-title-link::attr(href)").get()
            book_url = urljoin('https://www.labirint.ru', relative_url)
            yield scrapy.Request(url=book_url, callback=self.parse_book_data, meta={'keyword': keyword, 'page': page})

            ## Get All Pages
        if page == 15:
            available_pages = response.css(
                'a.pagination-number__text::text'
            ).getall()


            for page_num in available_pages:
                labirint_search_url = f'https://www.labirint.ru/search/{keyword}/?stype=0&page={page_num}'
                yield scrapy.Request(url=labirint_search_url, callback=self.discover_books_urls, meta={'keyword': keyword, 'page': page_num})


    def parse_book_data(self, response):

        price = response.css('span.buying-pricenew-val-number::text').get()
        if not price:
            price = response.css('span.buying-priceold-val::text').get()
        yield {
            "name" : response.css('div>h1::text').get(),
            "price" : price,
        }



