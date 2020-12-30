import requests
import json

URL = 'http://localhost:8000/create-parameter'

def backdoor_add_parameter(key, value):
    data = {
        'name': key,
        'name_vn': value['name'],
        'description': value['description'],
        'unit': value['unit'],
        'upper': float(value['upper']),
        'lower': float(value['lower']),
        'recommend': float(value['recommend'])
    }
    r = requests.post(URL, data=data)
    print(r.status_code)

table = json.load(open('data/table.json'))

for t in table:
    for name in table[t]:
        backdoor_add_parameter(name, table[t][name])
# for code in codes:
#     if code:
#         backdoor_add_code(code)


'''
{
    "table_1": {
        "tua_may": {
            "index": "3,4",
            "description": "con cặc",
            "name": "Tua máy",
            "unit": "hpm",
            "upper": "100",
            "lower": "200",
            "recommend": "150",
            "formula": "formula cai con cac"
        },
        '''