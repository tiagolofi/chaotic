
import json
import requests
import re
from bs4 import BeautifulSoup

with open('database.json', 'r') as file:

	data = json.load(file)

def get_elem(url):

	html = requests.get(url).content

	soup = BeautifulSoup(html, 'html.parser')

	try:

		list_elem = set([i['alt'] for i in soup.find_all('img') if re.match(r'Earth|Air|Fire|Water', i['alt'])])

		return [i.split('-')[0] for i in list_elem if 'Inactive' not in i]

	except:

		return []

# print(get_elem(url = data.get('Odu-Bathax')['parent_link']))

for i in data.keys():

	if data.get(i)['type_card'] in ['overworlders', 'underworlders', 'mipedians', 'danians', 'marrillians']:

		data.get(i)['elements'] = get_elem(data.get(i)['parent_link'])

		print(i)

with open('database2.json', 'w') as file:

	json.dump(data, file, indent = 2)