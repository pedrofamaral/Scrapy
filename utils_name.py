#Extração de dados
def parse(self, response):
    title = response.css("title::text").get()
    yield {"url": response.url, "title": title}

#Seguir links
next_page = response.css("a.next::attr(href)").get()
if next_page:
    yield response.follow(next_page, self.parse)
