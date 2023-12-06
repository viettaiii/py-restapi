import requests


endpoint = "http://localhost:8000/api/"

response = requests.post(endpoint ) 
# print(response.headers)
# print(response.text)
print(response.json())