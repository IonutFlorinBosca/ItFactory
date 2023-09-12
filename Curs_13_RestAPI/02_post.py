import requests
from pprint import pprint

URL = 'https://jsonplaceholder.typicode.com/posts'
payload = {'title': 'poo', 'body': 'var', 'userId': 1}
# payload trebuie sa aiba formatul unui post
# payload este postarea pe care vrem sa o adaugam in baza de date/pe care sa o
# persiste serverul

response = requests.post(URL, json=payload)

# 201 -> codul specific created
if response.status_code == 201:
    data = response.json()
    pprint(data)
else:
    print(f'Request failed with status code: {response.status_code}')
