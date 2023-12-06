import requests


endpoint = "http://localhost:8000/api/products/111111111/"

response = requests.get(endpoint) 
# print(response.headers)
# print(response.text)
print(response.json())