import json
import os
from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS
import socket

HOSTNAME = socket.gethostbyname(socket.gethostname())
PUBLIC_HOST = HOSTNAME
if HOSTNAME != '127.0.0.1':
    PUBLIC_HOST = '18.191.138.72'
PORT = 8081

app = Flask(__name__)
CORS(app)

BASE_URL = "http://{}:{}".format(PUBLIC_HOST, PORT)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MEDIA_DIR = os.path.join(BASE_DIR, 'media')


@app.route('/', methods=['GET'])
def home():
    data = [
        "{}/products/".format(BASE_URL),
        "{}/categories/".format(BASE_URL),
        "{}/media/".format(BASE_URL),
    ]
    return jsonify(data)


@app.route('/categories/', methods=['GET'])
def categories():
    categories_file = open('./parser/parsed_data/cats.json', 'r')
    categories_json = json.load(categories_file)
    return jsonify(categories_json)


@app.route('/products/', methods=['GET'])
def products():
    products_file = open('./parser/parsed_data/abad_products_new.json', 'r')
    products_json = json.load(products_file)

    category = request.args.get('cat')
    if category:
        new_products = []
        for product in products_json:
            if product['cat_id'] == category:
                new_products.append(product)
            elif product['pcat_id'] == category:
                new_products.append(product)
        products_json = new_products
    return jsonify(products_json)


@app.route('/products/<string:products_type>/', methods=['GET'])
def products_filter(products_type):
    products_file = open('./parser/parsed_data/abad_products_new.json', 'r')
    products_json = json.load(products_file)
    new_products = []

    for product in products_json:
        if product[products_type]:
            new_products.append(product)
    return jsonify(new_products)


@app.route('/products/detail/<string:product_slug>/', methods=['GET'])
def product_detail(product_slug):
    products_file = open('./parser/parsed_data/abad_products_new.json', 'r')
    products_json = json.load(products_file)

    prd = {}
    print(product_slug)
    for product in products_json:
        if product['slug'] == product_slug:
            prd = product
            break
    return jsonify(prd)


@app.route('/media/', methods=['GET'])
def media_files():
    files = os.listdir(MEDIA_DIR)
    new_files = []
    for file in files:
        new_files.append("{}{}".format(request.url, file))
    return jsonify(new_files)


@app.route('/media/<path:media_name>/', methods=['GET'])
def read_file(media_name):
    files = os.listdir(MEDIA_DIR)
    if media_name in files:
        return send_from_directory(MEDIA_DIR, media_name, mimetype='image/jpeg')
    return 'File not exist', 404


if __name__ == '__main__':
    app.run(debug=True, host=HOSTNAME, port=PORT)
