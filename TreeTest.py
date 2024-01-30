import requests
from csv import DictReader

#https://www.sainsburys.co.uk/groceries-api/gol-services/product/v1/product/taxonomy

api_url = "https://www.sainsburys.co.uk/groceries-api/gol-services/product/v1/product/taxonomy"
#headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

headers = {'method': 'GET',
        'Accept-Language': 'en-US,en;q=0.9,pt;q=0.8,es;q=0.7',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
resp = requests.get(api_url, headers=headers)
print(resp)
r = requests.get(api_url, headers=headers).json()
data = r['data']


def categories (department_children):
    b = 10
    for category in department_children:
        category_name = category.get('name')
        print(category_name)
        #category_ID = b
        #category_children = category.get('children')
        
        b+=1
    

def page_ID(data):
    a = 10
    b = 10
    for department in data:
        department_name = department.get('name')
        department_ID = a
        department_children = department.get('children')
        category_name = categories (department_children)
        a+=1
        
        #categories (department_children)
        print(category_name)
        
        



if __name__ == '__main__':
    page_ID(data)
    