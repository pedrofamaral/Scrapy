import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'  # Nome do spider
    start_urls = ['http://quotes.toscrape.com']  # URL inicial

    def parse(self, response):
        # Seleciona as citações na página
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),  # Texto da citação
                'author': quote.css('span small.author::text').get(),  # Autor
                'tags': quote.css('div.tags a.tag::text').getall(),  # Tags
            }

        # Pega o link da próxima página, se existir
        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)  # Faz o scraping da próxima página
