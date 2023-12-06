import requests
from getpass import getpass

auth_endpoint = "http://localhost:8000/api/auth/"

username = 'root'
password = getpass()
auth_response = requests.post(auth_endpoint, json={'username':username, 'password':password})
headers = {'Authorization': f'Bearer {auth_response.json()['token']}'}

endpoint = "http://localhost:8000/api/products/"
response = requests.get(endpoint , headers =headers  ) 
# print(response.headers)
# print(response.text)
print(response.json())