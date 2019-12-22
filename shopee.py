import requests
import pandas as pd
from fake_useragent import UserAgent
import sys
from classes import Product,Shopee

def scrap_shopee(keyword_search,total_of_result):
    
    ua = UserAgent()
    userAgent = ua.random
    Shopee_url = 'https://shopee.sg'
    
    headers = {
    'User-Agent': userAgent,
    'Referer': '{}search?keyword={}'.format(Shopee_url, keyword_search)
    }
    url = 'https://shopee.sg/api/v2/search_items/?by=relevancy&keyword={}&limit=100&newest=0&oanrder=desc&page_type=search'.format(keyword_search)

    r = requests.get(url, headers = headers).json()
    
    
    # titles_list = []
    # prices_list = []
    # ratings_list = []
    # url_list = []
    product_lst = []
    
    for item in r['items']:
        # titles_list.append(item['name'])
        # prices_list.append("$"+str(item['price_min']/100000))
        # ratings_list.append(item['item_rating'].get("rating_star"))
        
        url = "https://shopee.sg/"
        for i in item['name']: 
            
            if i.isalpha() == True:
                url+=i
                
            elif i.isdigit() == True:
                url+=i
                
            else:
                if url[-1] == "-":
                    continue
                url+="-"
                
        # url_list.append(url+"-i.{}.{}".format(item['shopid'],item['itemid'])) #i wrote these based on the structure of the url by combining the name + shopid + itemid
        product_lst.append(Shopee(item['name'],"$"+str(item['price_min']/100000),item['item_rating'].get("rating_star"),url+"-i.{}.{}".format(item['shopid'],item['itemid'])))

    
    
    if len(product_lst)==0:
        print("Fail")
        sys.exit()
    
   
    df = pd.DataFrame([t.__dict__ for t in product_lst])
    print(df)
    
    return product_lst

scrap_shopee("food",10)
