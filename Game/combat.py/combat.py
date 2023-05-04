""" #Random Encouter
import random
n = random.randint(1,10)
if n >= 9:
    enemy = "spider_swarm"
    print("You stumbled upon a spider swarm")
    combat()
elif n >= 7:
    enemy = "goblin"
    print("You encounter a goblin")
    combat()

#Fire Trap
import random
n = random.randint(1,10)
if n >= 10:
    print("You avoided a dangerous trap and continue deeper into the dungeon")
else:
    endingscenedie()

#Fighting
def combat():
    move = input("What will you do? Attack, Defend, or Heal?")
    if move == "Attack":
        print(weapons)
        weapon = input("Which weapon will you use")
        if weapon.lower == "iron_spear":
            spearattack
    if move == "Heal":

def enemyhp():
    if enemy == "spider_swarm":
        enemyhp = 100

def spearattack():
    enemyhurt = enemyhp - 25
    if enemyhp <= 0:
        print("You have killed your enemy")
spearattack() """


def magicheal():
    eplayerhp = playerhp + 20
    print(eplayerhp)
playerhp = 100
magicheal()


