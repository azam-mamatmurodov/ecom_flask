import json
from flask import Flask, request, jsonify
from flask_restful import Resource, Api

from data import products

app = Flask(__name__)
api = Api(app)

@app.route('/', methods=['GET'])
def home():
    data = {
        'message': 'Successful homepage',
        'status': 200
    }
    return jsonify(data)

class ProductsResource(Resource):
    def get(self):
        f = open('./products.json', 'r')
        products_json = json.load(f)
        return products_json

    def post(self):
        da1 = request.form.get('title')
        print(da1)
        return 'Created', 201


api.add_resource(ProductsResource, '/products/')

if __name__ == '__main__':
    app.run(debug=True)
