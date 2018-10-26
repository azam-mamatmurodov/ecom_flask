from flask import Flask, request, jsonify

from data import products

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    data = {
        'message': 'Successful homepage',
        'status': 200
    }
    return jsonify(data)

@app.route('/api/v1/products/', methods=['GET'])
def product_list():
    return jsonify(products.data)


if __name__ == '__main__':
    app.debug = True
    app.run()
