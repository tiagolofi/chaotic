
import json
from PIL import Image
from re import sub
import pytesseract as pt

pt.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'

with open('database2.json', 'r') as file:

	data = json.load(file)

def path_img(name):

	return f'''images/{data.get(name)['type_card']}/{data.get(name)['chaotic_hash']}.png'''

def read_text_card(name, type_, is_loc):

	img = Image.open(path_img(name))
	w, h = img.size

	if is_loc:
		sz = (1600, 400)
	else:
		sz = (800, 400)

	dc = {
		'creature': (40, 220, w - 25, h - 40),
		'bg': (10, 220, w - 10, h - 40),
		'att': (10, 250, w - 10, h - 40),
		'mg': (10, 230, w - 10, h - 40),
		'loc': (30, 200, w - 10, h - 10)
	}

	try:
		new_img = img.crop(dc.get(type_)).resize(sz).convert(mode = 'L')   
		# new_img.show()
		return sub(r'\n', ' ', pt.image_to_string(new_img)).strip()
	except:
		return 'fail get text'

for i in data.keys():

	data.get(i)['text_card'] = sub(r'\W', '', sub(' ', '_', data.get(i)['text_card'])).replace('_', ' ').lower().strip()

	print(i)

with open('database2.json', 'w') as file:

	json.dump(data, file, indent = 2)

# print(read_text_card('Malvadine', type_ = 'creature', is_loc = False))

# creatures = ['overworlders', 'underworlders', 'mipedians', 'danians', 'marrillians']
# 
# for i in data.keys():
# 
# 	if data.get(i)['type_card'] in creatures:
# 		  
# 		data.get(i)['text_card'] = read_text_card(name = i, type_ = 'creature', is_loc = False)
# 
# 		print(i)
# 
# for i in data.keys():
# 
# 	if 'battlegear' in data.get(i)['type_card']:
# 		  
# 		data.get(i)['text_card'] = read_text_card(name = i, type_ = 'bg', is_loc = False)
# 
# 		print(i)
# 
# for i in data.keys():
# 
# 	if 'attack' in data.get(i)['type_card']:
# 		  
# 		data.get(i)['text_card'] = read_text_card(name = i, type_ = 'att', is_loc = False)
# 
# 		print(i)
# 
# for i in data.keys():
# 
# 	if 'mugic' in data.get(i)['type_card']:
# 		  
# 		data.get(i)['text_card'] = read_text_card(name = i, type_ = 'mg', is_loc = False)
# 
# 		print(i)
# 
# for i in data.keys():
# 
# 	if 'location' in data.get(i)['type_card']:
# 		  
# 		data.get(i)['text_card'] = read_text_card(name = i, type_ = 'loc', is_loc = True)
# 
# 		print(i)
# 
