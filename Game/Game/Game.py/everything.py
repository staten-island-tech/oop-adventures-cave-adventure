inventory = ["bandage"]
weapons = ["iron_spear"]

def endingscenedie():
        retry = input("You have died. Would you like to retry? Y / N ")
        if retry.upper == "N":
            exit()

class attacking():
    def combat():
        import random
        from attack import player_attack
        damage = player_attack
        inventory = ["bandage"]
        weapons = ["iron_spear"]
        turn = True
        while turn == True:
                move = input("What will you do? Attack, Utility, or Heal? ")
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
                    input_3 = input("What would you like to use? ")
                    if input_3 == "bandage":
                        eplayerhp = playerhp + 30
                        if eplayerhp > 100:
                            eplayerhp = 100 
                            print(eplayerhp)
                        else:
                            print(playerhp)
                    elif input_3 == "health potion":
                        eplayerhp = playerhp + 60
                        if eplayerhp > 100:
                            eplayerhp = 100 
                            print(eplayerhp)
                        else:
                            print(playerhp)
                    elif input_3 == "great health potion":
                        eplayerhp = playerhp + 90
                        if eplayerhp > 100:
                            eplayerhp = 100 
                            print(eplayerhp)
                        else:
                            print(eplayerhp)
                    else:
                        endingscenedie()
                    turn = False

        