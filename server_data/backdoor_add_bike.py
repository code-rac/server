import requests

URL = 'http://localhost:8000/create-bike'

def backdoor_add_bike(line):
    ecu_id,name,generation,code,start_at,cc,is_used = line.split(',')
    data = {
        'name': name,
        'ecu_id': ecu_id,
        'generation': generation,
        'code': code,
        'start_at': start_at,
        'is_used': is_used,
        'cc': cc
    }
    r = requests.post(URL, data=data)
    print(r.status_code)

names = open('data/bike.csv').read().strip().split('\n')[1:]
print(names)
for name in names:
    if name:
        backdoor_add_bike(name)


