
import json
import requests

from random import sample
from bs4 import BeautifulSoup

BASE_URL = 'https://chaotic.fandom.com'

LINKS = {
	# creatures
	'danians': 'https://chaotic.fandom.com/wiki/Category:Danians',
	'marrillians': 'https://chaotic.fandom.com/wiki/Category:M%27arrillians',
	'mipedians': 'https://chaotic.fandom.com/wiki/Category:Mipedians',
	'overworlders': 'https://chaotic.fandom.com/wiki/Category:OverWorlders',
	'underworlders': 'https://chaotic.fandom.com/wiki/Category:UnderWorld_Creatures',	
	# mugix
	'generic-mugic': 'https://chaotic.fandom.com/wiki/Category:Generic_Mugic',
	'marrillian-mugic': 'https://chaotic.fandom.com/wiki/Category:M%27arrillian_Mugic',
	'overworld-mugic': 'https://chaotic.fandom.com/wiki/Category:OverWorld_Mugic',
	'mipedian-mugic': 'https://chaotic.fandom.com/wiki/Category:Mipedian_Mugic',
	'underworld-mugic': 'https://chaotic.fandom.com/wiki/Category:UnderWorld_Mugic',	
	# locations
	'danians-location': 'https://chaotic.fandom.com/wiki/Category:Locations_in_Danian_Territory',
	'marrillian-location': 'https://chaotic.fandom.com/wiki/Category:Locations_in_M%27arrillian_Territory',
	'mipedian-location': 'https://chaotic.fandom.com/wiki/Category:Locations_in_Mipedian_Territory',
	'overworld-location': 'https://chaotic.fandom.com/wiki/Category:Locations_in_OverWorld_Territory',
	'underworld-location': 'https://chaotic.fandom.com/wiki/Category:Locations_in_UnderWorld_Territory',
	# elemental attacks
	'air-attacks': 'https://chaotic.fandom.com/wiki/Category:Air_Attacks',
	'earth-attacks': 'https://chaotic.fandom.com/wiki/Category:Earth_Attacks',
	'fire-attacks': 'https://chaotic.fandom.com/wiki/Category:Fire_Attacks',
	'water-attacks': 'https://chaotic.fandom.com/wiki/Category:Water_Attacks',
	# discipline attacks
	'courage-attacks': 'https://chaotic.fandom.com/wiki/Category:Courage_Attacks',
	'power-attacks': 'https://chaotic.fandom.com/wiki/Category:Power_Attacks',
	'speed-attacks': 'https://chaotic.fandom.com/wiki/Category:Speed_Attacks',
	'wisdow-attacks': 'https://chaotic.fandom.com/wiki/Category:Wisdom_Attacks',	
	# equipaments
	'battlegear': 'https://chaotic.fandom.com/wiki/Category:Battlegear'
}

def get_links(url):

	html = requests.get(url).content

	soup = BeautifulSoup(html, 'html.parser')

	links = soup.find_all(class_ = 'category-page__member-link')

	return [BASE_URL + i['href'] for i in links]

def get_image_link(url):

	html = requests.get(url).content

	soup = BeautifulSoup(html, 'html.parser')

	obj = soup.find(class_ = 'image')

	return obj['href'], obj.img['alt']

def chaotic_hash():

	letters_and_numbers = 'ABCDEFGHIJKLMOPQRSTUVXWYZ0123456789'

	return ''.join(sample(letters_and_numbers, 12))

db = {}

for i in LINKS.keys():

	parent_links = get_links(url = LINKS.get(i))

	print(i)

	for j in parent_links:

		try:

			link, name = get_image_link(url = j)

			print(j)

			db.update(
				{
					name: {
					'type_card': i,
					'parent_link': j,
					'img_url': link,
					'chaotic_hash': chaotic_hash()
					}
				} 
			)

		except:
	
			pass

with open('database.json', 'w') as file:

	json.dump(db, file, indent = 2)

print(
	json.dumps(db, indent = 2)
)

	