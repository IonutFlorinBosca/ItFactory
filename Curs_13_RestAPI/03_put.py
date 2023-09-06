import requests
from pprint import pprint

# ! metoda 'put' face overwrite la intregul obiect astfel ca s-ar putea sa-i stearga anumite date
"""
Daca vrem sa pastram datele anterioare:
    - pastram in payload datele pe care nu vrem sa le modificam
    - folosim metoda 'patch'
"""

URL = 'https://jsonplaceholder.typicode.com/posts/1'
payload = {'title': 'abc'}
response = requests.put(URL, json=payload)

if response.status_code == 200:
    data = response.json()
    pprint(data)
else:
    print(f'Request failed with status code: {response.status_code}')
