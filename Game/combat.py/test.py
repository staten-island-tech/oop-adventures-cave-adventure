""" import uuid
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

weapons = []
ailments = []
inventory =["bandage"]

def combat():
    import random
    import attack
    n = random.randint(5,5)
    while n == 5 :
        print("You stumbled upon a spider swarm, and they seem hungry")
        enemy = "spider"
        if enemy == "spider swarm":
            enemyhp = 125
        elif enemy == "goblin":
            enemyhp = 50 
        elif enemy == "bandit":
            enemyhp = 100
        elif enemy == "mimic":
            enemyhp = 75
        elif enemy == "wanderer":
            enemyhp = 150
        else: 
            enemyhp = 4820 
        def endingscenedie():
            print(f" {name} has unfortunatley died ")
            print(inventory)
            retry = input("Would you like to retry Y / N ")
            if retry == "N":
                exit()

        turn = True
        while turn == True:
            playerhp = int(input("hp input "))
            if playerhp <= int(0):
                endingscenedie()
            if playerhp >= int(100):
                playerhp = 100
            move = input("What will you do? Attack, Utility, or Heal? ")
            if move == "Attack":
                attack()
                n = 0
            elif move == "Heal":
                if playerhp <= int(0):
                    endingscenedie()
                elif playerhp >= int(1):
                    eplayerhp = playerhp + 20
                    if eplayerhp > 100:
                        eplayerhp = 100
                        print(eplayerhp)
                        n = 0
                        break
                    else:
                        print(eplayerhp)
                        n = 0
                        break
            else:
                print(inventory)
                input_3 = input("What would you like to use? ")
                if input_3.lower == "bandage":
                    eplayerhp = playerhp + 30
                    print(eplayerhp)
                    n = 0
                    break
                elif input_3.lower == "health potion":
                    eplayerhp = playerhp + 60
                    print(eplayerhp)
                    n = 0
                    break
                elif input_3.lower == "great health potion":
                    eplayerhp = playerhp + 90
                    print(eplayerhp)
                    n = 0
                    break
                elif input_3.lower == "soda":
                    print("The sweet flavor of the soda rejuvenates your weary body. You feel a new wave of power.")
                    ailments.append("soda")
                    n = 0
                    break

    if n == 4:
        print("You encounter a goblin, a green imp-like creature with fangs")
        enemy = "goblin"
        if enemy == "spider swarm":
            enemyhp = 125
        elif enemy == "goblin":
            enemyhp = 50 
        elif enemy == "bandit":
            enemyhp = 100
        elif enemy == "mimic":
            enemyhp = 75
        elif enemy == "wanderer":
            enemyhp = 150
        else: 
            enemyhp = 4820 
        turn = True
        while turn == True:
            move = input("What will you do? Attack, Utility, or Heal? ")
            if move == "Attack":
                attack()
                n = 0
            elif move == "Heal":
                if playerhp <= int(0):
                    endingscenedie()
                elif playerhp >= int(1):
                    eplayerhp = playerhp + 20
                if eplayerhp > 100:
                    eplayerhp = 100 
                    print(eplayerhp)
                else:
                    print(eplayerhp)
                n = 0
            else:
                print(inventory)
                input_3 = ("What would you like to use?")
                if input_3.lower == "bandage":
                    playerhp + 30
                    print(playerhp)
                    n= 0
                elif input_3.lower == "health potion":
                    playerhp + 60
                    print(playerhp)
                    n=0
                elif input_3.lower == "great health potion":
                    playerhp + 90
                    print(playerhp)
                    n=0
                elif input_3.lower == "soda":
                    print("The sweet flavor of the soda rejuvenates your weary body. You feel a new wave of power.")
                    ailments.append("soda")
                    n=0

    if n == 3 :
        print("You have come across a bandit trying to steal your treasure")
        enemy = "bandit"
        if enemy == "spider swarm":
            enemyhp = 125
        elif enemy == "goblin":
            enemyhp = 50 
        elif enemy == "bandit":
            enemyhp = 100
        elif enemy == "mimic":
            enemyhp = 75
        elif enemy == "wanderer":
            enemyhp = 150
        else: 
            enemyhp = 4820 
        turn = True
        while turn == True:
            move = input("What will you do? Attack, Utility, or Heal? ")
            if move == "Attack":
                attack()
                n=0
            elif move == "Heal":
                if playerhp <= int(0):
                    endingscenedie()
                elif playerhp >= int(1):
                    eplayerhp = playerhp + 20
                if eplayerhp > 100:
                    eplayerhp = 100 
                    print(eplayerhp)
                else:
                    print(eplayerhp)
                n=0
            else:
                print(inventory)
                input_3 = ("What would you like to use?")
                if input_3.lower == "bandage":
                    playerhp + 30
                    print(playerhp)
                    n=0
                elif input_3.lower == "health potion":
                    playerhp + 60
                    print(playerhp)
                    n=0
                elif input_3.lower == "great health potion":
                    playerhp + 90
                    print(playerhp)
                    n=0
                elif input_3.lower == "soda":
                    print("The sweet flavor of the soda rejuvenates your weary body. You feel a new wave of power.")
                    ailments.append("soda")
                    n=0

    if n == 2:
        print("You have happened upon a mimic, a creature who disguises itself as a chest and kills any who tries to open it")
        enemy = "mimic"
        if enemy == "spider swarm":
            enemyhp = 125
        elif enemy == "goblin":
            enemyhp = 50 
        elif enemy == "bandit":
            enemyhp = 100
        elif enemy == "mimic":
            enemyhp = 75
        elif enemy == "wanderer":
            enemyhp = 150
        else: 
            enemyhp = 4820 
        turn = True
        while turn == True:
            move = input("What will you do? Attack, Utility, or Heal? ")
            if move == "Attack":
                attack()
                n=0
            elif move == "Heal":
                if playerhp <= int(0):
                    endingscenedie()
                elif playerhp >= int(1):
                    eplayerhp = playerhp + 20
                if eplayerhp > 100:
                    eplayerhp = 100 
                    print(eplayerhp)
                else:
                    print(eplayerhp)
                n=0
            else:
                print(inventory)
                input_3 = ("What would you like to use?")
                if input_3.lower == "bandage":
                    playerhp + 30
                    print(playerhp)
                    n=0
                elif input_3.lower == "health potion":
                    playerhp + 60
                    print(playerhp)
                    n=0
                elif input_3.lower == "great health potion":
                    playerhp + 90
                    print(playerhp)
                    n=0
                elif input_3.lower == "soda":
                    print("The sweet flavor of the soda rejuvenates your weary body. You feel a new wave of power.")
                    ailments.append("soda")
                    n=0

    if n == 1 :
        print("You come across a mysterious wanderer with malicious intent")
        enemy = "wanderer"
        if enemy == "spider swarm":
            enemyhp = 125
        elif enemy == "goblin":
            enemyhp = 50 
        elif enemy == "bandit":
            enemyhp = 100
        elif enemy == "mimic":
            enemyhp = 75
        elif enemy == "wanderer":
            enemyhp = 150
        else: 
            enemyhp = 4820 
        turn = True
        while turn == True:
            move = input("What will you do? Attack, Utility, or Heal? ")
            if move == "Attack":
                attack()
                n=0
            elif move == "Heal":
                if playerhp <= int(0):
                    endingscenedie()
                elif playerhp >= int(1):
                    eplayerhp = playerhp + 20
                if eplayerhp > 100:
                    eplayerhp = 100 
                    print(eplayerhp)
                else:
                    print(eplayerhp)
                n=0
            else:
                print(inventory)
                input_3 = ("What would you like to use?")
                if input_3.lower == "bandage":
                    playerhp + 30
                    print(playerhp)
                    n=0
                elif input_3.lower == "health potion":
                    playerhp + 60
                    print(playerhp)
                    n=0
                elif input_3.lower == "great health potion":
                    playerhp + 90
                    print(playerhp)
                    n=0
                elif input_3.lower == "soda":
                    print("The sweet flavor of the soda rejuvenates your weary body. You feel a new wave of power.")
                    ailments.append("soda")
                    n=0

combat() """

ailments = []
inventory = ["bandage"]


print(inventory)
playerhp = 100
input_3 = input("What would you like to use?")
if input_3 == "bandage":
    playerhp + 30
    print(playerhp)
elif input_3.lower == "health potion":
    playerhp + 60
    print(playerhp)
elif input_3.lower == "great health potion":
    playerhp + 90
    print(playerhp)
elif input_3.lower == "soda":
    print("The sweet flavor of the soda rejuvenates your weary body. You feel a new wave of power.")
    ailments.append("soda")