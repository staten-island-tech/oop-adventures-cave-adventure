import random
n = random.randint(1,5)
if n == 5 :
        print("You stumbled upon a spider swarm, and they seem hungry")
        enemy = "spider"
if n == 4:
        print("You encounter a goblin, a green imp-like creature with fangs")
        enemy = "goblin"
if n == 3 :
        print("You have come across a bandit trying to steal your treasure")
        enemy = "bandit"
if n == 2:
        print("You have happened upon a mimic, a creature who disguises itself as a chest and kills any who tries to open it")
        enemy = "mimic"
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