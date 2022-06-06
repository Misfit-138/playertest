class Player:

    def __init__(self,name,constitution,intelligence,wisdom,strength,dexterity):
        self.name = name
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.strength = strength
        self.dexterity = dexterity

    def navigate(self):
        print("The player is navigating")

    def swing(self):
        print("The player swings and gets a random swing score added to his dexterity")

    def heals(self):
        print("The player takes a restorative tincture")