import requests

payload = {
    "token": "ARzxBv7V__MacelIGRTLVA",
    "data": {
      "productName": "productName",
      "productSize": "productSize",
      "productOrderStatus": "productOrderStatus",
     "colorText": "colorText",
      "colorHex": "colorHex",
      "colorRGB": "colorRGB",
      "colorHSL": "colorHSL",
      "currencyName": "currencyName",
      "currencySymbol": "currencySymbol",
      "currencyCode": "currencyCode",
      "companyName": "companyName",
      "companyDepartment": "companyDepartment",
      "companyIndustry": "companyIndustry",
      "_repeat": 500

    }
};

r = requests.post("https://app.fakejson.com/q", json = payload)
print(r.json())
