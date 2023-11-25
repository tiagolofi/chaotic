
import json
from os import listdir
import re

with open('database.json', 'r') as file:

	data = json.load(file)
	
lista = [re.sub(r'\.png', '', i) for i in listdir('images/')]

for i in data.keys():

    if data.get(i)['chaotic_hash'] not in lista:
        
        print(i)