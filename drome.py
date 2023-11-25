
import json
from random import sample

class Drome():

    def __init__(self) -> None:

        self.IMG_FOLDER = 'images'
        self.CREATURES = ['overworlders', 'underworlders', 'mipedians', 'danians', 'marrillians']

        with open('database.json', 'r') as file:
            self.DATABASE = json.load(file)

    def format_image(self, type_card: str, hash: str) -> str:

        return f'''{self.IMG_FOLDER}/{type_card}/{hash}.png'''

    def ls_names(self) -> tuple:

        creatures = list({k for k, v in self.DATABASE.items() if v['type_card'] in self.CREATURES})
        creatures.sort()
        attacks = list({k for k, v in self.DATABASE.items() if 'attacks' in v['type_card']})
        attacks.sort()
        mugix = list({k for k, v in self.DATABASE.items() if 'mugic' in v['type_card']})
        mugix.sort()
        bg = list({k for k, v in self.DATABASE.items() if 'battlegear' in v['type_card']})
        bg.sort()

        return creatures, attacks, mugix, bg

    def get_creature_data(self, name: str) -> dict:

        return self.DATABASE.get(name)
    
    def get_creature(self, name: str) -> str:

        data = self.get_creature_data(name)
        return self.format_image(
            data['type_card'], data['chaotic_hash']
        )
    
    def get_location(self) -> str:

        list_locals = list({(v['type_card'], v['chaotic_hash']) for k, v in self.DATABASE.items() if 'location' in v['type_card']})
        local = sample(list_locals, 1)[0]
        return self.format_image(
            *local
        )

    def get_attack(self) -> str:
 
        list_attacks = list({(v['type_card'], v['chaotic_hash']) for k, v in self.DATABASE.items() if 'attacks' in v['type_card']})
        attack = sample(list_attacks, 1)[0]
        return self.format_image(
            *attack
        )

if __name__ == '__main__':

    x = Drome()

    print(x.get_creature(name = 'Phelphor'))
