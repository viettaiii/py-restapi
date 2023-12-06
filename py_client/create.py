import requests


endpoint = "http://localhost:8000/api/products/"

data = {
    "title":"This title 3"
}
response = requests.post(endpoint , json = data ) 
# print(response.headers)
# print(response.text)
print(response.json())