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


## API_URL to get tree and identify all PAGE ID to scrape and Categories

api_url = "https://www.sainsburys.co.uk/groceries-api/gol-services/product/v1/product/taxonomy"
#headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}


##Define Headers to avoid 403 response(error) when scraping

headers = {'method': 'GET',
        'Accept-Language': 'en-US,en;q=0.9,pt;q=0.8,es;q=0.7',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}


## Get response when testing to make sure response is 200

resp = requests.get(api_url, headers=headers)
print(resp)


##Define the inicial data and parse it 

r = requests.get(api_url, headers=headers).json()
data = r['data']

links_ID = []

## Final Loop to get individeal ID for each webpage to scrape and define the final names

def aisle(category_tree):
    c = 10
    for aisle in category_tree.get('category_children'):
        aisle_tree = {
            'department_name': category_tree.get('department_name'),
            'department_ID': category_tree.get('department_ID'),
            'category_name': category_tree.get('category_name'),
            'category_ID': category_tree.get('category_ID'),
            'aisle_name': aisle.get('name'),
            'aisle_ID': c,
            'page_ID': aisle.get('id')
        }
        c+=1
        if aisle.get('children') == []:
            links_ID.append(aisle_tree)
            
        else:
            shelve = aisle.get('children')
            d = 10
            for name in shelve:
                aisle_tree_2 = {
                'department_name': category_tree.get('department_name'),
                'department_ID': category_tree.get('department_ID'),
                'category_name': category_tree.get('category_name'),
                'category_ID': category_tree.get('category_ID'),
                'aisle_name': aisle.get('name'),
                'aisle_ID': c,
                'page_ID': aisle.get('id'),
                'shelve': name.get('name'),
                'shleve_ID': d,
                'web_ID': name.get('id')
            }
                d +=1
                links_ID.append(aisle_tree_2)
                
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


## Function for pages were options need to be choosen 

def scrape_product_page(link):
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


## Loop to define the secundary dictionaries

def category(items):
    b = 10
    for category in items.get('children'):
        category_tree = {
            'department_name': items.get('name'),
            'department_ID': items.get('department_ID'),
            'category_name': category.get('name'),
            'category_ID': b,
            'category_children': category.get('children')
        }
        b+=1
        aisle(category_tree)



## Loop the Data so get the main dictionaries

for department in data:
    a = 10
    department = {
        'name': department.get('name'),
        'department_ID': a,
        'children': department.get('children')
    }
    a+=1
    category(department)

    scrape = []

    for page in links_ID:
        #print(page.get('web_ID'))


        if page.get('web_ID') == None:
            scrape.append(page.get('page_ID'))
            #print(page.get('page_ID'))
            #print('========================')
        else:
            scrape.append(page.get('web_ID'))
            #print(page.get('web_ID'))
            #print('33333333333333333')
            
            
## Save tree in a CSV File

tree = pd.DataFrame(links_ID)
tree.to_csv('tree')
            

## Loop to get just the necessary ID Pages to scrape later

url_list = []

for link in links_ID:
    if link.get('web_ID') != None:
        url_list.append((link.get('web_ID')))
    else:
        url_list.append((link.get('page_ID')))


## Function to scrape the pages from the tree ID
        
def scraper(url_list):
    for url in url_list:

        page = f'https://www.sainsburys.co.uk/gol-ui/groceries/meat-and-fish/beef/beef-roasting-joints/c:{url}'
        
        headers = {'method': 'GET',
                'Accept-Language': 'en-US,en;q=0.9,pt;q=0.8,es;q=0.7',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--headless")
        chrome_options.add_argument(headers)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(page)
        time.sleep(3)
        soup = BeautifulSoup(driver.page_source,'lxml')
        data = soup.select("#root > div.app > div.ln-o-page > div.ln-o-page__body > div > div > div > section > ul > li")

        def extract_data(product, selector):
            try:
                return product.select_one(selector).text
            except AttributeError:
                return None

        product = []


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

    def scrape_product_page(link):
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
            product.append(web_data)

        for item in data:
            product_data = {
                'name': extract_data(item, 'h2.pt__info__description'),
                'price': extract_data(item, 'span.pt__cost__retail-price'),
                'price_per': extract_data(item, 'span.pt__cost__unit-price-per-measure'),
                'nectar_price': extract_data(item, 'span.pt__cost--price'),
                'price_kg': extract_data(item, 'select'),
                'product_link': item.find('a', href=True)['href']
            }
            if product_data.get('price_kg') == None:
                product.append(product_data)

            else:
                link = product_data.get('product_link')
                scrape_product_page(link)
                


        print(product)

       
        

           

scraper(url_list)



    

        
