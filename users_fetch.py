import requests

payload = {
    "token": "ARzxBv7V__MacelIGRTLVA",
    "data": {
      "companyName": "companyName",
      "companyDepartment": "companyDepartment",
      "companyIndustry": "companyIndustry",
      "user": {
    	"first_name": "nameFirst",
    	"last_name": "nameLast",
    	"email": "internetEmail",
    	"nickname": "personNickname",
    	"password": "personPassword",
    	"avatar": "personAvatar"
      },
      "address": {
    	"building": "addressBuilding",
    	"street": "addressFullStreet",
    	"city": "addressCity",
    	"state": "addressState",
    	"country": "addressCountry",
    	"zip": "addressZipCode"
      },
      "credit_card": {
      	"number": "bankCCNumber",
      	"cvv": "bankCCCVV",
      	"expiry": "bankCCExpiry",
     	"type": "bankCCName"
      },
      "_repeat": 500
    }
}
r = requests.post("https://app.fakejson.com/q", json = payload)
print(r.text)
