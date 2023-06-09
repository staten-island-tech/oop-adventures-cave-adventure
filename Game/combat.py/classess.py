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


