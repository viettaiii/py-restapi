import requests


endpoint = "http://localhost:8000/api/"

response = requests.get(endpoint , params= {'abc':'123' , "a":1}  , json={"query":"Hello world!"}) 
# print(response.text)
print(response.json())