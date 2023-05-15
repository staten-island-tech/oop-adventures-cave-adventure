""" turn = True


while turn == True:
    move = input("What will you do? Attack, Utility, or Heal? ")
    if move == "Attack":
        print("HI")
        turn = False
    elif move == "Heal":
        print("HI")
        turn = False
    else:
        print("HI")
        turn = False """
""" 
#Random Encouter
def enemy_check():
    import random
    n = random.randint(1,10)
    if n == 9 or 10:
        print("You stumbled upon a spider swarm")
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
    if n == 7 or 8:
        print("You encounter a goblin")
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
    if n == 6 or 5:
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
    if n == 4 or 3:
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
    if n == 2 or 1:
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
            enemyhp = 4820  """



""" import random
n = random.randint(1,10)
if n == 9:
    print("hi")
if n == 8:
    print("bye")
if n == 7:
    print("j")
if n == 6:
    print("g")
if n == 5:
    print("y")
if n == 4:
    print("d")
if n == 3:
    print("a")
if n == 2:
    print("k")
if n == 1:
    print("p")  """

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
    else: 
        enemyhp = 4820 
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