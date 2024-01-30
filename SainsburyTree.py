import requests

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
for main_dict in data:
    main_list = main_dict.get('children')
    for aux_dict in main_list:
        aux_list = aux_dict.get('children')
        for last_dict in aux_list:
            last_list = last_dict.get('children')
            id = last_dict.get('id')
            if last_list == []:
                print(id)
                print(last_dict.get('name'))
                print(main_dict.get('name'))

            else:
                for final_id in last_list:
                    id_2 = final_id.get('id')


                    
                    print(id_2)
                    print(final_id.get('name'))
                    print(main_dict.get('name'))
                    print('===================')