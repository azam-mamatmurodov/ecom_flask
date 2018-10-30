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
category_file = open(category_file_path, 'r')
category_file_json = json.load(category_file)


def get_category(cat_id):
    cat_id = str(cat_id)

    for cat in category_file_json:
        if str(cat['id']) == cat_id:
            return cat
        else:
            for chcat in cat['children']:
                if str(chcat['id']) == cat_id:
                    return chcat


def correct_products():
    pass


def read_products():
    f = open(os.path.join(PARSED_DATA_DIR, 'abad_products.json'))
    rows = json.load(f)
    new_products = []
    files = read_files()
    for row in rows:
        for product in row['products']:
            main_img_url = product['main_img']
            img_name = str(main_img_url).split('/')[-1]
            if img_name in files:
                product['image'] = "http://{}/media/{}".format(HOST_NAME, img_name)
                product['cat_id'] = row['cat_id']
                product['pcat_id'] = row['pcat_id']
                product['cat'] = get_category(row['cat_id'])
                product['pcat'] = get_category(row['pcat_id'])
                product['featured'] = random.randint(0, 1)
                product['top_rated'] = random.randint(0, 1)
                product['new'] = random.randint(0, 1)
                del product['main_img']

                new_products.append(product)
    return new_products


if __name__ == '__main__':
    # products = read_products()
    # encode = json.JSONEncoder().encode(o=products)
    # new_file = open(os.path.join(PARSED_DATA_DIR, 'abad_products_new.json'), 'w')
    # new_file.write(encode)
    # new_file.close()
    f = open(os.path.join(PARSED_DATA_DIR, 'abad_products_new2.json'))
    rows = json.load(f)
    new_products = []
    for row in rows:
        try:
            row['cat']['children'] = []
            print(row['cat']['children'])
        except Exception as e:
            print(row['id'])
            pass
        new_products.append(row)
    print(new_products)
    encode = json.JSONEncoder().encode(o=new_products)
    new_file = open(os.path.join(PARSED_DATA_DIR, 'abad_products_new.json'), 'w')
    new_file.write(encode)
    new_file.close()