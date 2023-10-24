
import json
import requests

with open('database.json', 'r') as file:

	data = json.load(file)

k = list(data.keys())

d = []

for i in k:

    if data.get(i)['type_card'] in ['overworlders', 'underworlders', 'mipedians', 'danians', 'marrillians'] and data.get(i)['stats']['Energy'] == 0:

        d.append(data.get(i))

with open('revisao.json', 'w') as file:

	json.dump(d, file, indent = 2)
