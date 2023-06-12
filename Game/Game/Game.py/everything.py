inventory = ["bandage","health_potion"]
weapons = ["iron_spear","flame_sword", "sand_magic"]

def endingscenedie():
        retry = input("You have died. Would you like to retry? Y / N ")
        if retry.upper == "N":
            exit()
        else:
            add_more_adventurers = True




class attacking():
    def combat():
        import random
        n = random.randint(1,5)
        if n == 5 :
            print("You stumbled upon a spider swarm, and they seem hungry")
            enemy = "spider"
            if enemy == "spider swarm":
                enemyhp = 75
            elif enemy == "goblin":
                enemyhp = 25
            elif enemy == "bandit":
                enemyhp = 75
            elif enemy == "mimic":
                enemyhp = 50
            elif enemy == "wanderer":
                enemyhp = 75
        if n == 4:
            print("You encounter a goblin, a green imp-like creature with fangs")
            enemy = "goblin"
            if enemy == "spider swarm":
                enemyhp = 75
            elif enemy == "goblin":
                enemyhp = 25
            elif enemy == "bandit":
                enemyhp = 75
            elif enemy == "mimic":
                enemyhp = 50
            elif enemy == "wanderer":
                enemyhp = 75
        if n == 3 :
            print("You have come across a bandit trying to steal your treasure")
            enemy = "bandit"
            if enemy == "spider swarm":
                enemyhp = 75
            elif enemy == "goblin":
                enemyhp = 25
            elif enemy == "bandit":
                enemyhp = 75
            elif enemy == "mimic":
                enemyhp = 50
            elif enemy == "wanderer":
                enemyhp = 75
        if n == 2:
            print("You have happened upon a mimic, a creature who disguises itself as a chest and kills any who tries to open it")
            enemy = "mimic"
            if enemy == "spider swarm":
                enemyhp = 75
            elif enemy == "goblin":
                enemyhp = 25
            elif enemy == "bandit":
                enemyhp = 75
            elif enemy == "mimic":
                enemyhp = 50
            elif enemy == "wanderer":
                enemyhp = 75
        if n == 1 :
            print("You come across a mysterious wanderer with malicious intent")
            enemy = "wanderer"
            if enemy == "spider swarm":
                enemyhp = 75
            elif enemy == "goblin":
                enemyhp = 25
            elif enemy == "bandit":
                enemyhp = 75
            elif enemy == "mimic":
                enemyhp = 50
            elif enemy == "wanderer":
                enemyhp = 75
        playerhp = 100
        hits = []
        bhits = []
        turn = True
        while turn == True:
                move = input("What will you do? Attack, Utility, or Heal (please respond with the format in the question)? ")
                if move == "Attack":
                    print(weapons)
                    weapon = input("Which weapon will you use ")
                    if weapon == "iron_spear":
                                if enemy == "spider swarm":
                                    bhits.append("i")
                                    for i in bhits:
                                        lenemyhp = enemyhp - (25*len(bhits))
                                    print (lenemyhp)
                                    print("You have been hit.")
                                    hits.append("i")
                                    for i in hits:
                                        lplayerhp = playerhp - (30*len(hits))
                                    print(lplayerhp)
                                    if lplayerhp < 0:
                                        endingscenedie()
                                    else:
                                        turn = True
                                    if lenemyhp <= 0:
                                           print("You killed the enemy")
                                           turn = False
                                elif enemy == "goblin":
                                    bhits.append("i")
                                    for i in bhits:
                                        lenemyhp = enemyhp - (25*len(bhits))
                                    print (lenemyhp)
                                    print("You have been hit.")
                                    hits.append("i")
                                    for i in hits:
                                        lplayerhp = playerhp - (30*len(hits))
                                    print(lplayerhp)
                                    if lplayerhp < 0:
                                        endingscenedie()
                                    else:
                                        turn = True
                                    if lenemyhp <= 0:
                                           print("You killed the enemy")
                                           turn = False
                                elif enemy == "bandit":
                                    bhits.append("i")
                                    for i in bhits:
                                        lenemyhp = enemyhp - (25*len(bhits))
                                    print (lenemyhp)
                                    print("You have been hit.")
                                    hits.append("i")
                                    for i in hits:
                                        lplayerhp = playerhp - (30*len(hits))
                                    print(lplayerhp)
                                    if lplayerhp < 0:
                                        endingscenedie()
                                    else:
                                        turn = True
                                    if lenemyhp <= 0:
                                           print("You killed the enemy")
                                           turn = False
                                elif enemy == "mimic":
                                    bhits.append("i")
                                    for i in bhits:
                                        lenemyhp = enemyhp - (25*len(bhits))
                                    print (lenemyhp)
                                    print("You have been hit.")
                                    hits.append("i")
                                    for i in hits:
                                        lplayerhp = playerhp - (30*len(hits))
                                    print(lplayerhp)
                                    if lplayerhp < 0:
                                        endingscenedie()
                                    else:
                                        turn = True
                                    if lenemyhp <= 0:
                                           print("You killed the enemy")
                                           turn = False
                                elif enemy == "wanderer":
                                    bhits.append("i")
                                    for i in bhits:
                                        lenemyhp = enemyhp - (25*len(bhits))
                                    print (lenemyhp)
                                    print("You have been hit.")
                                    hits.append("i")
                                    for i in hits:
                                        lplayerhp = playerhp - (30*len(hits))
                                    print(lplayerhp)
                                    if lplayerhp < 0:
                                        endingscenedie()
                                    else:
                                        turn = True
                                    if lenemyhp <= 0:
                                           print("You killed the enemy")
                                           turn = False
                    elif weapon == "flame_sword":
                                if enemy == "spider swarm":
                                    bhits.append("i")
                                    for i in bhits:
                                        lenemyhp = enemyhp - (25*len(bhits))
                                    print (lenemyhp)
                                    print("You have been hit.")
                                    hits.append("i")
                                    for i in hits:
                                        lplayerhp = playerhp - (30*len(hits))
                                    print(lplayerhp)
                                    if lplayerhp < 0:
                                        endingscenedie()
                                    else:
                                        turn = True
                                    if lenemyhp <= 0:
                                           print("You killed the enemy")
                                           turn = False
                                elif enemy == "goblin":
                                    bhits.append("i")
                                    for i in bhits:
                                        lenemyhp = enemyhp - (25*len(bhits))
                                    print (lenemyhp)
                                    print("You have been hit.")
                                    hits.append("i")
                                    for i in hits:
                                        lplayerhp = playerhp - (30*len(hits))
                                    print(lplayerhp)
                                    if lplayerhp < 0:
                                        endingscenedie()
                                    else:
                                        turn = True
                                    if lenemyhp <= 0:
                                           print("You killed the enemy")
                                           turn = False
                                elif enemy == "bandit":
                                    bhits.append("i")
                                    for i in bhits:
                                        lenemyhp = enemyhp - (25*len(bhits))
                                    print (lenemyhp)
                                    print("You have been hit.")
                                    hits.append("i")
                                    for i in hits:
                                        lplayerhp = playerhp - (30*len(hits))
                                    print(lplayerhp)
                                    if lplayerhp < 0:
                                        endingscenedie()
                                    else:
                                        turn = True
                                    if lenemyhp <= 0:
                                           print("You killed the enemy")
                                           turn = False
                                elif enemy == "mimic":
                                    bhits.append("i")
                                    for i in bhits:
                                        lenemyhp = enemyhp - (25*len(bhits))
                                    print (lenemyhp)
                                    print("You have been hit.")
                                    hits.append("i")
                                    for i in hits:
                                        lplayerhp = playerhp - (30*len(hits))
                                    print(lplayerhp)
                                    if lplayerhp < 0:
                                        endingscenedie()
                                    else:
                                        turn = True
                                    if lenemyhp <= 0:
                                           print("You killed the enemy")
                                           turn = False
                                elif enemy == "wanderer":
                                    bhits.append("i")
                                    for i in bhits:
                                        lenemyhp = enemyhp - (25*len(bhits))
                                    print (lenemyhp)
                                    print("You have been hit.")
                                    hits.append("i")
                                    for i in hits:
                                        lplayerhp = playerhp - (30*len(hits))
                                    print(lplayerhp)
                                    if lplayerhp < 0:
                                        endingscenedie()
                                    else:
                                        turn = True
                                    if lenemyhp <= 0:
                                           print("You killed the enemy")
                                           turn = False
                    elif weapon == "sand_magic":
                                if enemy == "spider swarm":
                                    bhits.append("i")
                                    for i in bhits:
                                        lenemyhp = enemyhp - (25*len(bhits))
                                    print (lenemyhp)
                                    print("You have been hit.")
                                    hits.append("i")
                                    for i in hits:
                                        lplayerhp = playerhp - (30*len(hits))
                                    print(lplayerhp)
                                    if lplayerhp < 0:
                                        endingscenedie()
                                    else:
                                        turn = True
                                    if lenemyhp <= 0:
                                           print("You killed the enemy")
                                           turn = False
                                elif enemy == "goblin":
                                    bhits.append("i")
                                    for i in bhits:
                                        lenemyhp = enemyhp - (25*len(bhits))
                                    print (lenemyhp)
                                    print("You have been hit.")
                                    hits.append("i")
                                    for i in hits:
                                        lplayerhp = playerhp - (30*len(hits))
                                    print(lplayerhp)
                                    if lplayerhp < 0:
                                        endingscenedie()
                                    else:
                                        turn = True
                                    if lenemyhp <= 0:
                                           print("You killed the enemy")
                                           turn = False
                                elif enemy == "bandit":
                                    bhits.append("i")
                                    for i in bhits:
                                        lenemyhp = enemyhp - (25*len(bhits))
                                    print (lenemyhp)
                                    print("You have been hit.")
                                    hits.append("i")
                                    for i in hits:
                                        lplayerhp = playerhp - (30*len(hits))
                                    print(lplayerhp)
                                    if lplayerhp < 0:
                                        endingscenedie()
                                    else:
                                        turn = True
                                    if lenemyhp <= 0:
                                           print("You killed the enemy")
                                           turn = False
                                elif enemy == "mimic":
                                    bhits.append("i")
                                    for i in bhits:
                                        lenemyhp = enemyhp - (25*len(bhits))
                                    print (lenemyhp)
                                    print("You have been hit.")
                                    hits.append("i")
                                    for i in hits:
                                        lplayerhp = playerhp - (30*len(hits))
                                    print(lplayerhp)
                                    if lplayerhp < 0:
                                        endingscenedie()
                                    else:
                                        turn = True
                                    if lenemyhp <= 0:
                                           print("You killed the enemy")
                                           turn = False
                                elif enemy == "wanderer":
                                    bhits.append("i")
                                    for i in bhits:
                                        lenemyhp = enemyhp - (25*len(bhits))
                                    print (lenemyhp)
                                    print("You have been hit.")
                                    hits.append("i")
                                    for i in hits:
                                        lplayerhp = playerhp - (30*len(hits))
                                    print(lplayerhp)
                                    if lplayerhp < 0:
                                        endingscenedie()
                                    else:
                                        turn = True
                                    if lenemyhp <= 0:
                                           print("You killed the enemy")
                                           turn = False
                    elif weapon == "throwable_bike":
                                if enemy == "spider swarm":
                                    bhits.append("i")
                                    for i in bhits:
                                        lenemyhp = enemyhp - (25*len(bhits))
                                    print (lenemyhp)
                                    print("You have been hit.")
                                    hits.append("i")
                                    for i in hits:
                                        lplayerhp = playerhp - (30*len(hits))
                                    print(lplayerhp)
                                    if lplayerhp < 0:
                                        endingscenedie()
                                    else:
                                        turn = True
                                    if lenemyhp <= 0:
                                           print("You killed the enemy")
                                           turn = False
                                elif enemy == "goblin":
                                    bhits.append("i")
                                    for i in bhits:
                                        lenemyhp = enemyhp - (25*len(bhits))
                                    print (lenemyhp)
                                    print("You have been hit.")
                                    hits.append("i")
                                    for i in hits:
                                        lplayerhp = playerhp - (30*len(hits))
                                    print(lplayerhp)
                                    if lplayerhp < 0:
                                        endingscenedie()
                                    else:
                                        turn = True
                                    if lenemyhp <= 0:
                                           print("You killed the enemy")
                                           turn = False
                                elif enemy == "bandit":
                                    bhits.append("i")
                                    for i in bhits:
                                        lenemyhp = enemyhp - (25*len(bhits))
                                    print (lenemyhp)
                                    print("You have been hit.")
                                    hits.append("i")
                                    for i in hits:
                                        lplayerhp = playerhp - (30*len(hits))
                                    print(lplayerhp)
                                    if lplayerhp < 0:
                                        endingscenedie()
                                    else:
                                        turn = True
                                    if lenemyhp <= 0:
                                           print("You killed the enemy")
                                           turn = False
                                elif enemy == "mimic":
                                    bhits.append("i")
                                    for i in bhits:
                                        lenemyhp = enemyhp - (25*len(bhits))
                                    print (lenemyhp)
                                    print("You have been hit.")
                                    hits.append("i")
                                    for i in hits:
                                        lplayerhp = playerhp - (30*len(hits))
                                    print(lplayerhp)
                                    if lplayerhp < 0:
                                        endingscenedie()
                                    else:
                                        turn = True
                                    if lenemyhp <= 0:
                                           print("You killed the enemy")
                                           turn = False
                                elif enemy == "wanderer":
                                    bhits.append("i")
                                    for i in bhits:
                                        lenemyhp = enemyhp - (25*len(bhits))
                                    print (lenemyhp)
                                    print("You have been hit.")
                                    hits.append("i")
                                    for i in hits:
                                        lplayerhp = playerhp - (30*len(hits))
                                    print(lplayerhp)
                                    if lplayerhp < 0:
                                        endingscenedie()
                                    else:
                                        turn = True
                                    if lenemyhp <= 0:
                                           print("You killed the enemy")
                                           turn = False
                    else:
                        print("You decided not to attack")

                elif move == "Heal":
                    for i in hits:
                        lplayerhp = playerhp - (30*len(hits))
                    if playerhp <= int(0):
                        endingscenedie()
                    elif playerhp >= int(1):
                        hits = []
                        splayerhp = lplayerhp + 20
                        if splayerhp > 100:
                            splayerhp = 100 
                            print(splayerhp)
                        else:
                            print(splayerhp)
                    turn = True
                    
                    
                elif move == "Utility":
                    print(inventory)
                    input_3 = input("What would you like to use? ")
                    if input_3 == "bandage":
                        eplayerhp = lplayerhp + 30
                        hits = []
                        if eplayerhp > 100:
                            eplayerhp = 100 
                            print(eplayerhp)
                        else:
                            print(playerhp)
                    elif input_3 == "health_potion":
                        eplayerhp = lplayerhp + 60
                        hits = []
                        if eplayerhp > 100:
                            eplayerhp = 100 
                            print(eplayerhp)
                        else:
                            print(eplayerhp)
                    elif input_3 == "great_health_potion":
                        eplayerhp = lplayerhp + 90
                        hits = []
                        if eplayerhp > 100:
                            eplayerhp = 100 
                            print(eplayerhp)
                        else:
                            print(eplayerhp)
                    else:
                        endingscenedie()
                    turn = True
                else:
                     turn = True
    




        