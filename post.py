import requests
import json

api_url = "http://192.168.2.156/api/resource/User Table"

headers = {"Content-Type": "application/json; charset=utf-8",
            "Accept":"application/json",
            "Authorization": "token c043b3fae600f17:b7d57f73ccc6f7e"}
 
data = {
    "user_name": "deepak66",
    "password": "deepak6666",
    "role": "participant"
}
 
response = requests.post(api_url, headers=headers, json=data)
 
print("Status Code", response.status_code)
print("JSON Response ", response.json())