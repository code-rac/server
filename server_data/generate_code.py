import pandas as pd
import string 
import random

random.seed(0)

with open('data/codes.txt', 'w') as fp:
	for i in range(20):
		code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=32))
		fp.write(code + '\n')
