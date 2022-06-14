import requests
import json

api_url = "http://192.168.2.156/api/method/mithra.mithra.doctype.user_table.login.login"

headers = {"Content-Type": "application/json; charset=utf-8",
            "Accept":"application/json",
            "Authorization": "token c043b3fae600f17:b7d57f73ccc6f7e"}
 
data = {
    "user_name": "deepak46",
    "password": "deepak4646",
}
 
response = requests.get(api_url, headers=headers, json=data)
 
print("Status Code", response.status_code)
print("JSON Response ", response.json())