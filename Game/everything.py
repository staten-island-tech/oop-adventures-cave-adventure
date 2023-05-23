
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

weapons = []
ailments = []
inventory =["bandage"]

if user_request == "Spearman":
    weapons.append("iron_spear")
if user_request == "Mage":
    weapons.append("sand_magic")
if user_request == "Warrior":
    weapons.append("flame_sword")

def endingscenedie():
                            print(f" {name} has unfortunatley died ")
                            print(inventory)
                            retry = input("Would you like to retry Y / N ")
                            if retry == "N":
                                exit()


def combat():
    import random
    n = random.randint(1,5)
    print(n)
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
        turn = True
        while turn == True:
                move = input("What will you do? Attack, Utility, or Heal? ")
                if move == "Attack":
                    print(weapons)
                    weapon = input("Which weapon will you use ")
                    if weapon == "iron_spear":
                        if "soda" in ailments.append:
                            enemyhp - 50
                            print(enemyhp)
                        else:
                            enemyhp - 25
                            print(enemyhp)
                            if enemyhp <= 0:
                                print("You have killed your enemy")
                    elif weapon == "flame_sword":
                        if "soda" in ailments.append:
                             enemyhp - 60
                             print(enemyhp)
                        else:
                            enemyhp - 30
                            print(enemyhp)
                            if enemyhp <= 0:
                                print("You killed the enemy")
                    elif weapon == "sand_magic":
                        if "soda" in ailments.append:
                            enemyhp - 80
                            print(enemyhp)
                        else:
                            enemyhp - 40
                            print(enemyhp)
                            if enemyhp <= 0:
                                print("You killed the enemy")
                    elif weapon == "throwable_bike":
                        if "soda" in ailments.append:
                            enemyhp - 140
                            print(enemyhp)
                        else:
                            enemyhp - 70
                            print(enemyhp)
                            if enemyhp <= 0:
                                print("You killed the enemy")
                    elif weapon == "throwable_motorcycle":
                        if "soda" in ailments.append:
                            enemyhp - 200
                        else:
                            enemyhp - 100
                            if enemyhp <= 0:
                                print("You killed the enemy")
                    turn = False
                elif move == "Heal":
                    playerhp = 100
                    if playerhp <= int(0):
                        endingscenedie()
                    elif playerhp >= int(1):
                        eplayerhp = playerhp + 20
                        if eplayerhp > 100:
                            eplayerhp = 100 
                            print(eplayerhp)
                        else:
                            print(eplayerhp)
                    turn = False
                else:
                    playerhp = 100
                    print(inventory)
                    input_3 = input("What would you like to use?")
                    if input_3 == "bandage":
                        playerhp + 30
                        if playerhp > 100:
                            playerhp = 100 
                            print(playerhp)
                        else:
                            print(playerhp)
                    elif input_3 == "health potion":
                        playerhp + 60
                        if playerhp > 100:
                            playerhp = 100 
                            print(playerhp)
                        else:
                            print(playerhp)
                    elif input_3 == "great health potion":
                        playerhp + 90
                        if playerhp > 100:
                            playerhp = 100 
                            print(playerhp)
                        else:
                            print(playerhp)
                    elif input_3 == "soda":
                        print("The sweet flavor of the soda rejuvenates your weary body. You feel a new wave of power.")
                        ailments.append("soda")
                    else:
                        endingscenedie()
                    turn = False
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
        turn = True
        while turn == True:
                move = input("What will you do? Attack, Utility, or Heal? ")
                if move == "Attack":
                    print(weapons)
                    weapon = input("Which weapon will you use ")
                    if weapon == "iron_spear":
                        if "soda" in ailments.append:
                            enemyhp - 50
                            print(enemyhp)
                        else:
                            enemyhp - 25
                            print(enemyhp)
                            if enemyhp <= 0:
                                print("You have killed your enemy")
                    elif weapon == "flame_sword":
                        if "soda" in ailments.append:
                            enemyhp - 60
                            print(enemyhp)
                        else:
                            enemyhp - 30
                            print(enemyhp)
                            if enemyhp <= 0:
                                print("You killed the enemy")
                    elif weapon == "sand_magic":
                        if "soda" in ailments.append:
                            enemyhp - 80
                            print(enemyhp)
                        else:
                            enemyhp - 40
                            print(enemyhp)
                            if enemyhp <= 0:
                                print("You killed the enemy")
                    elif weapon == "throwable_bike":
                        if "soda" in ailments.append:
                            enemyhp - 140
                            print(enemyhp)
                        else:
                            enemyhp - 70
                            print(enemyhp)
                            if enemyhp <= 0:
                                print("You killed the enemy")
                    elif weapon == "throwable_motorcycle":
                        if "soda" in ailments.append:
                            enemyhp - 200
                            print(enemyhp)
                        else:
                            enemyhp - 100
                            print(enemyhp)
                            if enemyhp <= 0:
                                print("You killed the enemy")
                    turn = False
                elif move == "Heal":
                    playerhp = 100
                    if playerhp <= int(0):
                        endingscenedie()
                    elif playerhp >= int(1):
                        playerhp = playerhp + 20
                        if playerhp > 100:
                            playerhp = 100 
                            print(playerhp)
                        else:
                            print(playerhp)
                    turn = False
                else:
                    print(inventory)
                    input_3 = input("What would you like to use?")
                    if input_3 == "bandage":
                        playerhp + 30
                        if playerhp > 100:
                            playerhp = 100 
                            print(playerhp)
                        else:
                            print(playerhp)
                    elif input_3 == "health potion":
                        playerhp + 60
                        if playerhp > 100:
                            playerhp = 100 
                            print(playerhp)
                        else:
                            print(playerhp)
                    elif input_3 == "great health potion":
                        playerhp + 90
                        if playerhp > 100:
                            playerhp = 100 
                            print(playerhp)
                        else:
                            print(playerhp)
                    elif input_3 == "soda":
                        print("The sweet flavor of the soda rejuvenates your weary body. You feel a new wave of power.")
                        ailments.append("soda")
                    else:
                        endingscenedie()
                    turn = False
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
        turn = True
        while turn == True:
                move = input("What will you do? Attack, Utility, or Heal? ")
                if move == "Attack":
                    print(weapons)
                    weapon = input("Which weapon will you use ")
                    if weapon == "iron_spear":
                        if "soda" in ailments.append:
                            enemyhp - 50
                            print(enemyhp)
                        else:
                            enemyhp - 25
                            print(enemyhp)
                            if enemyhp <= 0:
                                print("You have killed your enemy")
                    elif weapon == "flame_sword":
                        if "soda" in ailments.append:
                            enemyhp - 60
                            print(enemyhp)
                        else:
                            enemyhp - 30
                            print(enemyhp)
                            if enemyhp <= 0:
                                print("You killed the enemy")
                    elif weapon == "sand_magic":
                        if "soda" in ailments.append:
                            enemyhp - 80
                            print(enemyhp)
                        else:
                            enemyhp - 40
                            print(enemyhp)
                            if enemyhp <= 0:
                                print("You killed the enemy")
                    elif weapon == "throwable_bike":
                        if "soda" in ailments.append:
                            enemyhp - 140
                            print(enemyhp)
                        else:
                            enemyhp - 70
                            print(enemyhp)
                            if enemyhp <= 0:
                                print("You killed the enemy")
                    elif weapon == "throwable_motorcycle":
                        if "soda" in ailments.append:
                            enemyhp - 200
                            print(enemyhp)
                        else:
                            enemyhp - 100
                            print(enemyhp)
                            if enemyhp <= 0:
                                print("You killed the enemy")
                    turn = False
                elif move == "Heal":
                    playerhp = 100
                    if playerhp <= int(0):
                        endingscenedie()
                    elif playerhp >= int(1):
                        playerhp = playerhp + 20
                        if playerhp > 100:
                            playerhp = 100 
                            print(playerhp)
                        else:
                            print(playerhp)
                    turn = False
                else:
                    playerhp = 100
                    print(inventory)
                    input_3 = input("What would you like to use?")
                    if input_3 == "bandage":
                        playerhp + 30
                        if playerhp > 100:
                            playerhp = 100 
                            print(playerhp)
                        else:
                            print(playerhp)
                    elif input_3 == "health potion":
                        playerhp + 60
                        if playerhp > 100:
                            playerhp = 100 
                            print(playerhp)
                        else:
                            print(playerhp)
                    elif input_3 == "great health potion":
                        playerhp + 90
                        if playerhp > 100:
                            playerhp = 100 
                            print(playerhp)
                        else:
                            print(playerhp)
                    elif input_3 == "soda":
                        print("The sweet flavor of the soda rejuvenates your weary body. You feel a new wave of power.")
                        ailments.append("soda")
                    else:
                        endingscenedie()
                    turn = False
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
        turn = True
        while turn == True:
                move = input("What will you do? Attack, Utility, or Heal? ")
                if move == "Attack":
                    print(weapons)
                    weapon = input("Which weapon will you use ")
                    if weapon == "iron_spear":
                        if "soda" in ailments.append:
                            enemyhp - 50
                            print(enemyhp)
                        else:
                            enemyhp - 25
                            print(enemyhp)
                            if enemyhp <= 0:
                                print("You have killed your enemy")
                    elif weapon == "flame_sword":
                        if "soda" in ailments.append:
                             enemyhp - 60
                             print(enemyhp)
                        else:
                            enemyhp - 30
                            print(enemyhp)
                            if enemyhp <= 0:
                                print("You killed the enemy")
                    elif weapon == "sand_magic":
                        if "soda" in ailments.append:
                            enemyhp - 80
                            print(enemyhp)
                        else:
                            enemyhp - 40
                            print(enemyhp)
                            if enemyhp <= 0:
                                print("You killed the enemy")
                    elif weapon == "throwable_bike":
                        if "soda" in ailments.append:
                            enemyhp - 140
                            print(enemyhp)
                        else:
                            enemyhp - 70
                            print(enemyhp)
                            if enemyhp <= 0:
                                print("You killed the enemy")
                    elif weapon == "throwable_motorcycle":
                        if "soda" in ailments.append:
                            enemyhp - 200
                            print(enemyhp)
                        else:
                            enemyhp - 100
                            print(enemyhp)
                            if enemyhp <= 0:
                                print("You killed the enemy")
                    turn = False
                elif move == "Heal":
                    playerhp = 100
                    if playerhp <= int(0):
                        endingscenedie()
                    elif playerhp >= int(1):
                        eplayerhp = playerhp + 20
                        if eplayerhp > 100:
                            eplayerhp = 100 
                            print(eplayerhp)
                        else:
                            print(eplayerhp)
                    turn = False
                else:
                    print(inventory)
                    input_3 = input("What would you like to use?")
                    if input_3 == "bandage":
                        playerhp + 30
                        if playerhp > 100:
                            playerhp = 100 
                            print(playerhp)
                        else:
                            print(playerhp)
                    elif input_3 == "health potion":
                        playerhp + 60
                        if playerhp > 100:
                            playerhp = 100 
                            print(playerhp)
                        else:
                            print(playerhp)
                    elif input_3 == "great health potion":
                        playerhp + 90
                        if playerhp > 100:
                            playerhp = 100 
                            print(playerhp)
                        else:
                            print(playerhp)
                    elif input_3 == "soda":
                        print("The sweet flavor of the soda rejuvenates your weary body. You feel a new wave of power.")
                        ailments.append("soda")
                    else:
                        endingscenedie()
                    turn = False
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
        turn = True
        while turn == True:
                move = input("What will you do? Attack, Utility, or Heal? ")
                if move == "Attack":
                    print(weapons)
                    weapon = input("Which weapon will you use ")
                    if weapon == "iron_spear":
                        if "soda" in ailments.append:
                            enemyhp - 50
                            print(enemyhp)
                        else:
                            enemyhp - 25
                            print(enemyhp)
                            if enemyhp <= 0:
                                print("You have killed your enemy")
                    elif weapon == "flame_sword":
                        if "soda" in ailments.append:
                             enemyhp - 60
                             print(enemyhp)
                        else:
                            enemyhp - 30
                            print(enemyhp)
                            if enemyhp <= 0:
                                print("You killed the enemy")
                    elif weapon == "sand_magic":
                        if "soda" in ailments.append:
                            enemyhp - 80
                            print(enemyhp)
                        else:
                            enemyhp - 40
                            print(enemyhp)
                            if enemyhp <= 0:
                                print("You killed the enemy")
                    elif weapon == "throwable_bike":
                        if "soda" in ailments.append:
                            enemyhp - 140
                            print(enemyhp)
                        else:
                            enemyhp - 70
                            print(enemyhp)
                            if enemyhp <= 0:
                                print("You killed the enemy")
                    elif weapon == "throwable_motorcycle":
                        if "soda" in ailments.append:
                            enemyhp - 200
                            print(enemyhp)
                        else:
                            enemyhp - 100
                            print(enemyhp)
                            if enemyhp <= 0:
                                print("You killed the enemy")
                    turn = False
                elif move == "Heal":
                    playerhp = 100
                    if playerhp <= int(0):
                        endingscenedie()
                    elif playerhp >= int(1):
                        eplayerhp = playerhp + 20
                        if eplayerhp > 100:
                            eplayerhp = 100 
                            print(eplayerhp)
                        else:
                            print(eplayerhp)
                    turn = False
                else:
                    print(inventory)
                    input_3 = input("What would you like to use?")
                    if input_3 == "bandage":
                        playerhp + 30
                        if playerhp > 100:
                            playerhp = 100 
                            print(playerhp)
                        else:
                            print(playerhp)
                    elif input_3 == "health potion":
                        playerhp + 60
                        if playerhp > 100:
                            playerhp = 100 
                            print(playerhp)
                        else:
                            print(playerhp)
                    elif input_3 == "great health potion":
                        playerhp + 90
                        if playerhp > 100:
                            playerhp = 100 
                            print(playerhp)
                        else:
                            print(playerhp)
                    elif input_3 == "soda":
                        print("The sweet flavor of the soda rejuvenates your weary body. You feel a new wave of power.")
                        ailments.append("soda")
                    else:
                        endingscenedie()
                    turn = False
combat()