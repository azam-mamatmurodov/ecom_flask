import json
import os
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

root_url = "http://127.0.0.1:5000"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MEDIA_DIR = os.path.join(BASE_DIR, 'media')


@app.route('/', methods=['GET'])
def home():
    data = [
        "{}/products/".format(root_url),
        "{}/categories/".format(root_url),
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

    return jsonify(products_json)


@app.route('/media/<path:media_name>/', methods=['GET'])
def read_file(media_name):
    files = os.listdir(MEDIA_DIR)
    if media_name in files:
        f = open(os.path.join(MEDIA_DIR, media_name))
        return send_from_directory(MEDIA_DIR, media_name, mimetype='image/jpeg')
    return 'File not exist', 404


if __name__ == '__main__':
    app.run(debug=True)
