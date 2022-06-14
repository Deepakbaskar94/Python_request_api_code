import requests
import json

api_url = "http://mithra.com/api/method/mithra.mithra.doctype.phq9_session.api.phqsessionpost"

headers = {"Content-Type": "application/json; charset=utf-8",
            "Accept":"application/json",
            "Authorization": "token 2559f591d98ea66:9e2cdc0890cc4eb"}
 
data = {
    "user_name": "deepak66",
}
 
response = requests.post(api_url, headers=headers, json=data)
 
print("Status Code", response.status_code)
print("JSON Response ", response.json())
