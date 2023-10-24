
import json
import requests
import re
from bs4 import BeautifulSoup

with open('database.json', 'r') as file:

	data = json.load(file)

def get_info(url):

	html = requests.get(url).content

	soup = BeautifulSoup(html, 'html.parser')

	try:

		table = soup.find('table').text

		data = {
			'Courage': int(re.search('Courage:(.*?)\xa0', table).group(1)),
			'Power': int(re.search('Power:(.*?)\xa0', table).group(1)),
			'Wisdom': int(re.search('Wisdom:(.*?)\xa0', table).group(1)),
			'Speed': int(re.search('Speed:(.*?)\xa0', table).group(1)),
			'Energy': int(re.search('Energy:(.*?)\xa0', table).group(1))
		}

	except:

		data = {
			'Courage': 0,
			'Power': 0,
			'Wisdom': 0,
			'Speed': 0,
			'Energy': 0
		}

	return data

for i in data.keys():

	if data.get(i)['type_card'] in ['overworlders', 'underworlders', 'mipedians', 'danians', 'marrillians']:

		data.get(i)['stats'] = get_info(data.get(i)['parent_link'])

		print(i)

with open('database2.json', 'w') as file:

	json.dump(data, file, indent = 2)
