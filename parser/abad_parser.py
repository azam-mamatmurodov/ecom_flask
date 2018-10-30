import json
from requests import get, post
endpoint = "https://abad.uz/catalog/ajaxfilter/{}/"

json_file = open('./parsed_data/cats.json', 'r')
cats = json.load(json_file)
products = []
for cat in cats:
	json_data = {
		'main_id': cat['id'],
		'pricelimit': '200;115910403',
		'limit': 40,
		'numb': 40
	}
	req = post(url=endpoint.format(cat['id']), data=json_data)
	res_data = req.json()
	res_data['cat_id'] = cat['id']
	res_data['pcat_id'] = 0
	products.append(res_data)
	for ch_cat in cat['children']:
		json_data = {
			'main_id': ch_cat['id'],
			'pricelimit': '200;115910403',
			'limit': 40,
			'numb': 40
		}
		req = post(url=endpoint.format(ch_cat['id']), data=json_data)
		res_data = req.json()
		res_data['cat_id'] = ch_cat['id']
		res_data['pcat_id'] = cat['id']
		products.append(res_data)
print(products)
# print(data[0])