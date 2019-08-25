import json

import requests

ENDPOINT = "https://grad4-backend.herokuapp.com/api/v1/company/activate-deactivate/"
# ENDPOINT = "http://193.176.241.131:8000/"

headers = {
    "Content-Type": "application/json",
    "Authorization": "JWT " + "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo3OCwidXNlcm5hbWUiOiJiYXJ0YXJhcnlhQGdtYWlsLmNvbSIsImV4cCI6MTU2NjU2ODE0NiwiZW1haWwiOiJiYXJ0YXJhcnlhQGdtYWlsLmNvbSIsIm9yaWdfaWF0IjoxNTY2NTY1NDQ2fQ.P3U9jYZqvDIPdollzPKZ65EZapdief3PeWcWt5E0nng",
}

data = {
    "id": 84,
}

post_data = json.dumps(data)
posted_response = requests.post(ENDPOINT, data=post_data, headers=headers)
# print(posted_response.content)
# print("----------------")
print(posted_response.text)
print("----------------")
