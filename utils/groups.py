
import json
import shutil

with open('database.json', 'r') as file:

    data = json.load(file)

# print(set([data.get(i)['type_card'] for i in data.keys()]))

for i in data.keys():
    
    print(i)

    from_ = 'images/' + data.get(i)['chaotic_hash'] + '.png'

    dest_ = 'images2/' + data.get(i)['type_card'] + '/' + data.get(i)['chaotic_hash'] + '.png'

    shutil.copyfile(from_, dest_)
