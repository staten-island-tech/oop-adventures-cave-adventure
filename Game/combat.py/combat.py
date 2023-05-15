""" #Combat
from attack import attack
from magicheal import magicheal
from space import space

turn = True
while turn == True:
    move = input("What will you do? Attack, Utility, or Heal? ")
    if move == "Attack":
        attack()
        turn = False
    elif move == "Heal":
        magicheal()
        turn = False
    else:
        space()
        turn = False """



#Random Encouter
def enemy_check():
    import random
    n = random.randint(1,10)
    if n >= 9:
        enemy = "spider swarm"
        print("You stumbled upon a spider swarm")
        enemy_hp()
        combat()
    elif n == 7 or 8:
        enemy = "goblin"
        print("You encounter a goblin")
        enemy_hp()
        combat()
    elif n == 6 or 5:
        enemy = "bandit"
        print("You have come across a bandit trying to steal your treasure")
        enemy_hp()
        combat()
    elif n == 4 or 3:
        enemy = "mimic"
        print("You have happened upon a mimic, a creature who disguises itself as a chest and kills any who tries to open it")
        enemy_hp()
        combat()
    elif n == 2 or 1:
        enemy = "wanderer"
        print("You come across a mysterious wanderer with malicious intent")
        enemy_hp()
        combat()
enemy_check


def enemy_hp():
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

enemies = []
defeated_enemies = []  

""" def spiderattack():
    if turn == False:
        playerhp - 40
        print("You got hit for 40 hp. You have this much hp left:")
        print(playerhp)
        turn = True

def goblinattack():
    if turn == False:
        playerhp - 20
        print("You got hit for 20 hp. You have this much hp left:")
        print(playerhp)
        turn = True

def banditattack():
    if turn == False:
        playerhp - 30
        print("You got hit for 30 hp. You have this much hp left:")
        print(playerhp)
        turn = True

def mimicattack():
    if turn == False:
        playerhp - 80 
        print("You got hit for 80 hp. You have this much hp left:")
        print(playerhp)
        turn = True

def wandererattack():
    if turn == False:
        playerhp - 45
        print("You got hit for 45 hp. You have this much hp left:")

def gardenattack():
    while curse in ailments:
        for encounter in encounters:
            playerhp - 5
        print("You have taken 5 dmg from the God's curse")


 """