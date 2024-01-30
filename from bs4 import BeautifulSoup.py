from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager








chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_experimental_option("detach", True)
# chrome_options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url='https://groceries.asda.com/aisle/price-match/view-all-price-match/view-all-price-match/1215686354045-1215686354052-1215686354053'
driver.get(url)
driver.maximize_window()
time.sleep(5)
#accept cookie
driver.find_element(By.XPATH,'//*[@id="onetrust-button-group-parent"]/div/button[1]').click()
time.sleep(2)
soup=BeautifulSoup(driver.page_source,'lxml')
html=soup.select_one('div.co-product-list > ul:nth-child(1)')
for item in html:
    print(item.text)