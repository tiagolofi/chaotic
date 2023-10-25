
import json
from random import sample

class Drome():

    def __init__(self):

        self.img_folder = 'images/'
        
        self.creatures = ['overworlders', 'underworlders', 'mipedians', 'danians', 'marrillians']

        with open('database.json', 'r') as file:

            self.db = json.load(file)

    # def filter_db(self, type_card):
    #     return {k: v for k, v in self.db.items() if type_card in v['type_card']}

    def format_image(self, hash):

        return self.img_folder + hash + '.png'

    def location_random(self):

        hashs = {k: v['chaotic_hash'] for k, v in self.db.items() if 'location' in v['type_card']}

        return self.format_image(
            hash = sample(list(hashs.values()), 1)[0]
        )

    def get_names_creatures(self):

        return list({k: v for k, v in self.db.items() if v['type_card'] in self.creatures}.keys())

    def get_names_attacks(self):

        return list({k: v for k, v in self.db.items() if 'attacks' in v['type_card']}.keys())

    def get_names_mugix(self):

        return list({k: v for k, v in self.db.items() if 'mugic' in v['type_card']}.keys())

    def get_names_bg(self):

        return list({k: v for k, v in self.db.items() if 'battlegear' in v['type_card']}.keys())

    def get_card(self, name):

        return self.db.get(name)

    def get_attacks(self, cards):

        all_attacks = {k: v for k, v in self.db.items() if k in cards}

        return all_attacks, sum(list({k: v['build_cost'] for k, v in all_attacks.items()}.values()))

if __name__ == '__main__':

    x = Drome()

    print(x.location_random())

    print(
        x.get_attacks(cards = x.get_names_attacks()[2:5])
    )