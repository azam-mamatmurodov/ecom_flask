import os
import json
import random

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARSER_DIR = os.path.join(ROOT_DIR, 'parser')
PARSED_DATA_DIR = os.path.join(PARSER_DIR, 'parsed_data')
HOST_NAME = "127.0.0.1:5000"


def read_files():
    files = os.listdir(os.path.join(ROOT_DIR, 'media'))
    return files


category_file_path = os.path.join(PARSED_DATA_DIR, 'cats.json')
category_file = open(category_file_path)
category_file_json = json.load(category_file)


def random_category():
    ids = []
    chids = []
    new_cat = {}
    for cat in category_file_json:
        ids.append(cat['id'])
    random_pid_cat = random.choice(ids)
    random_chid_cat = 0
    for cat in category_file_json:
        if cat['id'] == random_pid_cat:
            children = cat['children']
            for chid_cat in children:
                chids.append(chid_cat['id'])
            random_chid_cat = random.choice(chids)
            for chid_cat in children:
                if chid_cat['id'] == random_chid_cat:
                    new_cat['id'] = random_chid_cat
                    new_cat['name'] = chid_cat['title']
                    break
            break
    return new_cat


def read_products():
    f = open(os.path.join(PARSED_DATA_DIR, 'abad_products.json'))
    rows = json.load(f)
    products = []
    files = read_files()
    for row in rows:
        for product in row['products']:
            main_img_url = product['main_img']
            img_name = str(main_img_url).split('/')[-1]
            if img_name in files:
                product['image'] = "http://{}/media/{}".format(HOST_NAME, img_name)
                product['category'] = random_category()
                del product['main_img']
                products.append(product)
    return products


# if __name__ == '__main__':
#     products = read_products()
#     encode = json.JSONEncoder().encode(o=products)
#     new_file = open(os.path.join(PARSED_DATA_DIR, 'abad_products_new.json'), 'w')
#     new_file.write(encode)
#     new_file.close()
