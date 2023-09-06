import requests
from pprint import pprint

"""
Spre deosebire de 'put', metoda 'patch' actualizeaza doar campurile care apar in payload si nu sterge niciun fel de 
date de la resursele existente.
"""

URL = 'https://jsonplaceholder.typicode.com/posts/1'
payload = {'title': 'abc'}
response = requests.patch(URL, json=payload)

if response.status_code == 200:
    data = response.json()
    pprint(data)
else:
    print(f'Request failed with status code: {response.status_code}')
