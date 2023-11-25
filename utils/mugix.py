
import json
import webbrowser
import pyautogui as pg

# pg.displayMousePosition()

with open('database.json', 'r') as file:

	data = json.load(file)
	
for i in data.keys():

	if data.get(i)['type_card'] in ['overworlders', 'underworlders', 'mipedians', 'danians', 'marrillians']:
		
		pg.click(x = 2326, y = 334)

		pg.hotkey('ctrl', 'w')

		webbrowser.open_new('file:///c%3A/Users/User/Documents/envs/chaotic/images/' + data.get(i)['chaotic_hash'] + '.png')

		try:

			data.get(i)['mugix'] = int(input(f'''{i}: ''')) # digitar na mão

		except:

			data.get(i)['mugix'] = int(input(f'''{i}: ''')) # digitar na mão

with open('database2.json', 'w') as file:

	json.dump(data, file, indent = 2)
