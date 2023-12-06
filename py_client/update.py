import requests


endpoint = "http://localhost:8000/api/products/1/update/"

data = {
    "title":"This title update 2"
}
response = requests.patch(endpoint , json = data ) 
# print(response.headers)
# print(response.text)
print(response.json())