import requests

url_endpoint = 'http://api.noobtest.id/dummy/v1/users/8'

response = requests.delete(url_endpoint)

print(response.status_code)
print(response.text)