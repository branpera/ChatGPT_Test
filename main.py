# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# res = requests.get('https://stackoverflow.com/questions/26000336')
# print(res)


import requests
import json

# Get access token:
headers = {"Content-Type": "application/x-www-form-urlencoded"}
r = requests.post("https://accounts.spotify.com/api/token", headers=headers, data={"grant_type": "client_credentials", "client_id": "dad831679b5c44e9b0c42686e97a9486", "client_secret": "34c1341a75ae4c00833cb831113ebcdd"})
request_token_result = r.text
token_dict = json.loads(request_token_result)
authorization = token_dict['token_type'] + ' ' + token_dict['access_token']
print(token_dict)
new_reqeust = requests.get("https://api.spotify.com/v1/artists/4Z8W4fKeB5YxbusRsdQVPb", headers={'Authorization': authorization})
artists_dict = json.loads(new_reqeust.text)
