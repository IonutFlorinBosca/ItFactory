import requests
from pprint import pprint

URL = 'https://jsonplaceholder.typicode.com/posts'
payload = {'title': 'poo', 'body': 'var', 'userId': 1}

response = requests.post(URL, json=payload)

if response.status_code == 201:
    data = response.json()
    pprint(data)
else:
    print(f'Request failed with status code: {response.status_code}')
