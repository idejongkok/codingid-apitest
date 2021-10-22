import requests

url_endpoint = 'http://api.noobtest.id/dummy/v1/users'

query = {"email": "aria@zz.com","name": "aria"}

response = requests.post(url_endpoint, json=query)

print(response.status_code)
print(response.text)
