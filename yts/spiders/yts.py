import scrapy

from yts.items import BooksItem
from yts.items import MovieItem

#class BookSpider(scrapy.Spider):
#    name = "book"
#    allowed_domains = ["books.toscrape.com"]
#    start_urls = ["https://books.toscrape.com/"]
#
#    def start_requests(self):
#        for url in self.start_urls:
#            yield scrapy.Request(
#                url, callback=self.parse, errback=self.log_error
#            )
#
#    def parse(self, response):
#        """
#        @url https://books.toscrape.com
#        @returns items 20 20
#        @returns request 1 50
#        @scrapes url title price 
#        """
#        for book in response.css("article.product_pod"):
#            item = BooksItem()
#            item["url"] = book.css("h3 > a::attr(href)").get()
#            item["title"] = book.css("h3 > a::attr(title)").get()
#            item["price"] = book.css(".price_color::text").get()
#            yield item
#        next_page = response.css("li.next>a::attr(href)").get()
#        if next_page:
#            next_page_url = response.urljoin(next_page)
#            self.logger.info(
#                f"Navigating to next page with URL {next_page_url}."
#            )
#            yield scrapy.Request(url=next_page_url,callback=self.parse,errback=self.log_error)
#    def log_error(self, failure):
#        self.logger.error(repr(failure))

class MovieSpider(scrapy.Spider):
    name = "movie"
    allowed_domains = ["yts.mx"]
    start_urls = ["https://yts.mx/browse-movies?page=1"]
    page_number = 1
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url, callback=self.parse, errback=self.log_error
            )

    def parse(self, response):
        """
        @url https://yts.mx/browse-movies
        @returns items 20 20
        @returns request 1 50
        @scrapes url title year 
        """
        for movie in response.css("div.browse-movie-wrap"):
            item = MovieItem()
            item["title"] = movie.css("a.browse-movie-title::text").get()
            item["url"] = movie.css("a.browse-movie-title::attr(href)").get()
            item["year"] = movie.css(".browse-movie-year::text").get()
            yield item
        self.page_number +=1
        next_page = f'https://yts.mx/browse-movies?page={self.page_number}'
        if response.css('div.browse-movie-wrap'):
            #next_page_url = response.urljoin(next_page)
            self.logger.info(
                f"Navigating to next page with URL {next_page}."
            )
            yield scrapy.Request(url=next_page,callback=self.parse,errback=self.log_error)
        if not response.css('div.browse-movie-wrap'):
            return #No hay mas peliculas
    def log_error(self, failure):
        self.logger.error(repr(failure))