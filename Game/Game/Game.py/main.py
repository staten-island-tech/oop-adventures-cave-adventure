from app import random_1
random = random_1
from everything import attacking
attacks = attacking
import random

print("Once upon a time there was a small village named Giron, and they were a completely self-sufficient community that seldomly interacted with foreigners. However, one day a small mysterious dungeon appeared out of thin air and reeked havoc on the surrounding environment. The ground was infected with the miasma being emitted from the dungeon's opening, and monsters never seen before started coming out of the dungeon. The once peaceful village was turned into a deserted ghostown within 2 years of the formation of the dungeon. Now, the place has become a legend with only rumors of its existence being spread.")
print("It is now up to you to vanquish the evil dungeoon, save the village, and maybe become rich while you're at it.")
print(" ")
import uuid
class Adventurer:
    def __init__(self, id, name, rank):
        self.id = id
        self.name = name
        self.rank = rank
class Warrior(Adventurer):
    def __init__(self, id, name, rank, sword):
        super().__init__(name, id, rank)
        self.sword = sword
    def __str__(self):
        return f"{self.name}, {self.rank}, {self.sword}, {self.id}"
class Mage(Adventurer):
    def __init__(self, id, name, rank, magic):
        super().__init__(name, id, rank)
        self.magic = magic
    def __str__(self):
        return f"{self.name}, {self.rank}, {self.magic}, {self.id}"
class Spearman(Adventurer):
    def __init__(self, name, id, rank, spear):
        super().__init__(name, id, rank)
        self.spear = spear
    def __str__(self):
        return f"{self.name}, {self.rank}, {self.spear}, {self.id}"
    
def create_new_warrior(name, rank, sword):
    id = str(uuid.uuid4())
    new_warrior = Warrior(id, name, rank, sword)
    print(new_warrior)
def create_new_mage(name, rank, magic):
    id = str(uuid.uuid4())
    new_mage = Mage(id, name, rank, magic)
    print(new_mage)
def create_new_spearman(name, rank, spear):
    id = str(uuid.uuid4())
    new_spearman = Spearman(id, name, rank, spear)
    print(new_spearman)

add_more_adventurers = "Y"

while add_more_adventurers == "Y":
    user_request = input("What type of adventurer do you want to add? Warrior/Mage/Spearman ")
    if user_request == "Warrior":
        name = input("What is their name? ")
        rank = input("What is their rank? ")
        sword = "Sword user"
        create_new_warrior(name, rank, sword)
        add_more_adventurers = "N"
    if user_request == "Mage":
        name = input("What is their name? ")
        rank = input("What is their rank? ")
        magic = "Magic user"
        create_new_mage(name, rank, magic)
        add_more_adventurers = "N"
    if user_request == "Spearman":
        name = input("What is their name? ")
        rank = input("What is their rank? ")
        spear = "Spear user"
        create_new_spearman(name, rank, spear)
        add_more_adventurers = "N"

inventory_2 = []

if user_request == "Spearman":

    print(f"{name} hails from the Empire of Corilia, they graduated from the Empirial Academy known for the best spearmen, and is currently working as a {rank} adventurer.")
if user_request == "Mage":

    print(f"{name} was born in the magical country of Hayrun that is known for its Magical Tower which pioneers all magical studies on the continent. He is currently working as a {rank} adventurer")
if user_request == "Warrior":

    print(f"{name} is a warrior from the warrior tribes of the Jing Steppes, and they boast the greatest military on the continent comprsied exclusively of swordmen. They were sent out on a quest to become a true warrior and is now a {rank} adventurer.")\
    
print("")
print(f"{name} adventures out in order to find the dungeon, they come across the ruins of Giron and know they are close.")
print("")
print(f"{name} fights against hunger and dehydration in order to find the dungeon, and 2 weeks after their adventure started they find the opening to the dungeon.")
print("")

paths = True
while paths == True:
    decision_1 = input(f"{name} comes across a fork in the dunegeon with 1 path being dark, 1 eerie, and 1 well lit. Which path should they go down? Dark? Eerie? Or Lit? ")
    if decision_1 == "Dark":
        print("You feel the prickly sensation of thorns on your finger and the item turns out to be a flower crown. I wonder what it can be used for?...")
        inventory_2.append("flower")
        attacks.combat()
        break
    if decision_1 == "Eerie":
        print("You wander around a random room trying to make your way through.")
        random.random()
        break
    if decision_1 == "Lit":
        attacks.combat()
        break
    else: 
        paths = True

attacks.combat()

cave = True
while cave == True:
    ending = input("Will you go deeper? Or will you try and go out of the cave? (Respond with Deeper or Escape)")
    if ending == "Deeper":
        print(f"{name} decides to go deeper into the dungeon and ends up in a huge room with an altar in the middle. You feel a strong urge to place something upon the altar...")
        print(inventory_2)
        altar = input("What item shall you place upon the altar?")
        if altar == "flower":
            print(f"The wall facing {name} opens up and reveals huge piles of gold and mythical items, your name will forever go down in history as the one to clear The Dungeon. The End")
            break
    if ending == "Escape":
        print(f"The adventure of {name} has sadly come to an end without anyone knowing of what he achieved. Instead of wealth and fame they chose to save themself.")
        break
    else:
        cave = True