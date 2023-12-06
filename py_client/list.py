import requests


endpoint = "http://localhost:8000/api/products/"


response = requests.get(endpoint  ) 
# print(response.headers)
# print(response.text)
print(response.json())