import requests

URL = 'http://localhost:8000/create-bike'

def backdoor_add_bike(name):
    data = {'name': name}
    r = requests.post(URL, data=data)
    print(r.status_code)

names = open('data/bikes.txt').read().strip().split('\n')

for name in names:
    if name:
        backdoor_add_bike(name)


