import requests

URL = 'http://localhost:8000/backdoor-add-code'

def backdoor_add_code(code):
    data = {'name': code}
    r = requests.post(URL, data=data)
    print('added ', code)

codes = open('data/codes.txt').read().strip().split('\n')

for code in codes:
    if code:
        backdoor_add_code(code)