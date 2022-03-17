from unittest import result
import requests
import json
import dataset

class ShopifyScraper():

    def __init__(self, baseurl):
        self.baseurl = baseurl

    def downloadjson(self, page):
        r = requests.get(self.baseurl + f'products.json?limit=250&page={page}', timeout=5)
        if r.status_code != 200:
            print('Bad Status Code: ', r.status_code)
        if len(r.json()['products']) > 0:
            data = r.json()['products']
            return data

        else:
            return

    def parsejson(self, jsondata):
        #print(jsondata)
        products = []

        for prod in jsondata:
            #print(prod['title'])
            mainid = prod['id']
            title = prod['title']
            published_at = prod['published_at']
            product_type = prod['product-type']
            for v in prod['variants']:
                #print(v['id'])
                item = {
                    'id': mainid,
                    'title': title,
                    'published_at': published_at,
                    'product_type': product_type,
                    'varid': v['id'],
                    'vartitle': v['title'],
                    'sku': v['sku'],
                    'price': v['price'],
                    'available': v['available'],
                    'created_at': v['created_at'],
                    'updated_at': v['updated_at'],
                    'compare_at-price': v['compare_at_price']
                }
                products.append(item)
            return products




def main():
    allbirds = ShopifyScraper('https://www.allbirds.co.uk/')
    results = []
    for x in range(1,10):
        data = allbirds.downloadjson(page)
        print('Getting page: ', page)
        try:
            results.append(allbirds.parsedata(data))
        except:
            print(f'Completed, total pages = { page - 1}')
            break
        return results

if __name__ == '__main__':

    db = dataset.connect('sqlite:///products.db')
    table = db.create_table('allbirds', primary_id =' varid')  
    products = main()
    totals = [item for i in products for item in i]
    #print(len(totals))

    for p in totals:
        if not table.find_one(varid=p['varid']):
            table.insert(p)