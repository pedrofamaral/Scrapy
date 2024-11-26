import scrapy
from ..items import BookItem

class BookstoreSpider(scrapy.Spider):
    name = 'bookstore'
    allowed_domains = ['fictional-bookstore.com']
    start_urls = ['https://fictional-bookstore.com/books']

    def parse(self, response):
        # Assuming each book is in a div with class 'book-item'
        for book in response.css('div.book-item'):
            item = BookItem()
            item['title'] = book.css('h2.book-title::text').get()
            item['author'] = book.css('span.book-author::text').get()
            item['price'] = book.css('span.book-price::text').get()
            item['isbn'] = book.css('span.book-isbn::text').get()
            yield item

        # Follow pagination links
        next_page = response.css('a.next-page::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

