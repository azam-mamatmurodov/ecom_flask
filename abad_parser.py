from requests import get
endpoint = "https://abad.uz/catalog/ajaxfilter/{}/"

products = []
for page in range(1,5):
    req = get(endpoint.format(page))
    data = req.json()
    products.append(data)
    print(products)
