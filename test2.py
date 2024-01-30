## Import Labraries

import requests
import csv
import pandas as pd
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.common.exceptions import NoSuchElementException

##Lists
links_ID = []
url_list = [1019895, 1020330]
product = []


##Define Headers to avoid 403 response(error) when scraping
headers = {'method': 'GET',
        'Accept-Language': 'en-US,en;q=0.9,pt;q=0.8,es;q=0.7',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}


chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--headless")
chrome_options.add_argument(headers)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


## Function to TRY and Extract the individual data from each product in the Page being scraped
        
def extract_data(product, selector):
            try:
                return product.select_one(selector).text
            except AttributeError:
                return None




## Function to scrape the pages from the tree ID
        
def scraper(url_list):
    # Loop the list of URl's to scrape each page
    for url in url_list:
        
        # Define da page with the URL from the list
        page = f'https://www.sainsburys.co.uk/gol-ui/groceries/meat-and-fish/beef/beef-roasting-joints/c:{url}'

        driver.get(page)
        time.sleep(3)

        soup = BeautifulSoup(driver.page_source,'lxml')
        data = soup.select("#root > div.app > div.ln-o-page > div.ln-o-page__body > div > div > div > section > ul > li")

        # Loop inside the page to get the data from each item in the page
        for item in data:
            price_kg =  extract_data(item, 'select'),
            product_data = {
                'name': extract_data(item, 'h2.pt__info__description'),
                'price': extract_data(item, 'span.pt__cost__retail-price'),
                'price_per': extract_data(item, 'span.pt__cost__unit-price-per-measure'),
                'nectar_price': extract_data(item, 'span.pt__cost--price'),
                'price_kg': extract_data(item, 'select'),
                'product_link': item.find('a', href=True)['href']
            }
            # Condiction to save the data from each product if no special conditions are needed
            if product_data.get('price_kg') == None:
                print(product_data)

            else:
                link = product_data.get('product_link')
                print(link)

scraper(url_list)

print(product)