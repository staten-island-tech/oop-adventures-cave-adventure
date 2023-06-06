inventory = ["bandage","health_potion"]
weapons = ["iron_spear","flame_sword", "sand_magic"]

def endingscenedie():
        retry = input("You have died. Would you like to retry? Y / N ")
        if retry.upper == "N":
            exit()

class attacking():
    def combat():
        playerhp = 100
        hits = []
        from attack import player_attack
        damage = player_attack
        turn = True
        while turn == True:
                move = input("What will you do? Attack, Utility, or Heal (please respond with the format in the question)? ")
                if move == "Attack":
                    print(weapons)
                    weapon = input("Which weapon will you use ")
                    if weapon == "iron_spear":
                            damage.spear_attack()
                    elif weapon == "flame_sword":
                            damage.sword_attack()
                    elif weapon == "sand_magic":
                            damage.magic_attack()
                    elif weapon == "throwable_bike":
                            damage.bike_attack()
                    elif weapon == "throwable_motorcycle":
                            damage.motor_attack()
                    turn = False
                    print("You have been hit.")
                    hits.append("i")
                    for i in hits:
                        lplayerhp = playerhp - (30*len(hits))
                    print(lplayerhp)
                    turn = True

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
                    turn = False
                    print("You have been hit.")
                    hits.append("i")
                    for i in hits:
                        lplayerhp = playerhp - (30*len(hits))
                    print(lplayerhp)
                    turn = True
                    
                else:
                    print(inventory)
                    input_3 = input("What would you like to use? ")
                    if input_3 == "bandage":
                        eplayerhp = playerhp + 30
                        if eplayerhp > 100:
                            eplayerhp = 100 
                            print(eplayerhp)
                        else:
                            print(playerhp)
                    elif input_3 == "health_potion":
                        eplayerhp = playerhp + 60
                        if eplayerhp > 100:
                            eplayerhp = 100 
                            print(eplayerhp)
                        else:
                            print(playerhp)
                    elif input_3 == "great_health_potion":
                        eplayerhp = playerhp + 90
                        if eplayerhp > 100:
                            eplayerhp = 100 
                            print(eplayerhp)
                        else:
                            print(eplayerhp)
                    else:
                        endingscenedie()
                    turn = False
                    print("You have been hit.")
                    hits.append("i")
                    for i in hits:
                        lplayerhp = playerhp - (30*len(hits))
                    print(lplayerhp)
                    turn = True
    




        