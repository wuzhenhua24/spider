__author__ = 'wuzhenhua'


import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = "http://category.dangdang.com/cp01.54.06.00.00.00-srsort_sale_amt_desc.html"
        source_code = requests.get(url)
        # just get the code, no headers or anything
        plain_text = source_code.text
        # BeautifulSoup objects can be sorted through easy
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a', {'class': 'pic'}):
            href = link.get('href')
            title = link.get('title')  # just the text, not the HTML
            #print(href)
            print(title)
            get_single_item_data(href)
        page += 1

def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    # if you want to gather information from that page
    for item_price in soup.findAll('span', {'id': 'salePriceTag'}):
        print(item_price.string)
    # if you want to gather links for a web crawler
    # for link in soup.findAll('a'):
    #     href = link.get('href')
    #     print(href)

trade_spider(1)