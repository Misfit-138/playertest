import random


class Monster:

    def __init__(self, name, level, gold, sword, armor, shield, constitution, intelligence, wisdom, strength,
                 dexterity):
        self.name = name
        self.level = level
        self.gold = gold
        self.sword = sword
        self.armor = armor
        self.shield = shield
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.strength = strength
        self.dexterity = dexterity


    '''def swing(self, dexterity, strength, sword):
        monster_roll20 = random.randint(1, 20)
        dexterity_modifier = round((dexterity - 10) / 2)
        player_roll20 = random.randint(1, 20)
        monster_roll12 = random.randint(1, 12)
        strength_modifier = round((strength - 10) / 2)
        damage_to_monster = round(monster_roll12 + strength_modifier + sword)
        print(f"Monster rolls 20 sided die---> {monster_roll20}")
        print(f"Dexterity modifier {dexterity_modifier}")
        print(f"Player rolls 20 sided die ---> {player_roll20}")
        if monster_roll20 + dexterity_modifier > player_roll20:
            print(f"Monster hits!")
            print(f"Monster rolls 12 sided die---> {monster_roll12}")
            print(f'Monster Strength modifier---> {strength_modifier}')
            print (f"Monster does {damage_to_monster} points of damage!")
        else:
            print(f"Monster misses..")
            return'''

