#!/usr/bin/python
import requests
import sys

id = 2
users = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}').json()
todos = requests.get(f'https://jsonplaceholder.typicode.com/users/todos').json()

print(users["name"])
print("\t", todos)