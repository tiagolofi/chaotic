
import json
import requests
import os

with open('database.json', 'r') as file:

    data = json.load(file)

def save_image(name, url):

    img = requests.get(url).content

    with open(f'images/{name}.png', 'wb') as handler:

        handler.write(img)

for i in data.keys():

    if data.get(i)['chaotic_hash'] + '.png' not in os.listdir('images/'):

        save_image(name = data.get(i)['chaotic_hash'], url = data.get(i)['img_url'])

        print(i)
