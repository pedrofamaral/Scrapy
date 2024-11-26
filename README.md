Web Scraping with Scrapy: Extracting Quotes
This repository contains an example project developed using the Scrapy framework, a powerful tool for web scraping in Python. The purpose of the project is to demonstrate how to create a spider to collect quotes, authors, and tags from the website Quotes to Scrape.

About the Project
The QuotesSpider performs the following tasks:

Automatically navigates through multiple pages of a website.
Extracts structured information, including:
Quote text;
Quote author;
Tags associated with each quote.
Ensures navigation between pages using dynamic links.
Main Files
quotes_spider.py: Main file containing the spider definition.
Expected Output: Extracted data can be exported to formats like JSON or CSV using Scrapy.
How to Run
Install Scrapy: Make sure Scrapy is installed in your environment:

pip install scrapy
Run the spider: In the terminal, navigate to the project directory and run the command:

scrapy crawl quotes
Export the data (optional): To save the results in a JSON or CSV file:


scrapy crawl quotes -o output.json
or

scrapy crawl quotes -o output.csv
Technologies Used
Python: Main programming language.
Scrapy: Web scraping framework.
CSS Selectors: For selecting and extracting data from HTML pages.

