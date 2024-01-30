import requests
import json
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.common.exceptions import NoSuchElementException

## Define pages to scrape for dferent weights

links = [
    'https://www.sainsburys.co.uk/gol-ui/product/sainsburys-21-day-matured-unfatted-top-side-top-rump-british-beef-roasting-joint-approx-14kg-',
    'https://www.sainsburys.co.uk/gol-ui/product/sainsburys-21-day-matured-british-beef-slow-roasting-joint-approx-14kg-',
    'https://www.sainsburys.co.uk/gol-ui/product/sainsburys-30-day-matured-british-beef-roasting-joint-taste-the-difference-approx-14kg-',
    'https://www.sainsburys.co.uk/gol-ui/product/sainsburys-matured-british-beef-short-ribs-taste-the-difference-x2-approx-15kg-'
        ]

## Define Headers to avoid errors
headers = {'method': 'GET',
        'Accept-Language': 'en-US,en;q=0.9,pt;q=0.8,es;q=0.7',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

## Define parametrs and options to render WebPage

chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--headless")
chrome_options.add_argument(headers)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

## Function to find the diferent elements in the page
def extract_info(selector):
    try:
        return driver.find_element(By.XPATH, selector).text
    except NoSuchElementException:
        pass


## Function to change the diferent options on the product page
    
def change_options(selector):
    try:
        return driver.find_element(By.XPATH, selector).click()
    except NoSuchElementException:
            pass


## Function to extract data inside product page
    
def page_data(selector):
    try:
        return soup.select_one(selector).text
    except AttributeError:
        return None


## Loop all Link's

for link in links:
    driver.get(link)
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source,'lxml')
    base_selector = soup.find('select', id=True)['id']
    selectors = [f'//*[@id="{base_selector}"]/option[1]',
                  f'//*[@id="{base_selector}"]/option[2]',
                  f'//*[@id="{base_selector}"]/option[3]',
                  f'//*[@id="{base_selector}"]/option[4]',
                  f'//*[@id="{base_selector}"]/option[5]']
    for selector in selectors:
        change_options(selector)
        
        time.sleep(3)
        soup = BeautifulSoup(driver.page_source,'lxml')
        #weight = extract_info(selector)
        name  = page_data('h1.pd__header'), extract_info(selector)
        price = page_data('span.pd__cost__retail-price')
        #price_2 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[2]/div[2]/div/div/div/div/section[1]/div/div/div[2]/div[6]/div[1]/div/div[2]/span[2]').text
        price_per = page_data('span.pd__cost__unit-price-per-measure')
        nectar_price = page_data('span.pd__cost--price')
        web_data = {
            'name': (page_data('h1.pd__header'), extract_info(selector)),
            'price': page_data('span.pd__cost__retail-price'),
            'price-per': page_data('span.pd__cost__unit-price-per-measure'),
            'nectar_price': page_data('span.pd__cost--price'),
            'product_link': link
        }
        print(web_data)