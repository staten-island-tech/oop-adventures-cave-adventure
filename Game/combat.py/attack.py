""" def attack():
    print(weapons)
    weapon = input("Which weapon will you use")
    if playerhp <= int(0):
        endingscenedie()
    if weapon.lower == "iron spear":
        spearattack()
    elif weapon.lower == "flame sword":
        swordattack()
    elif weapon.lower == "sand magic":
        magicattack()
    elif weapon.lower == "throwable bike":
        bikeattack()
    elif weapon.lower == "throwable motorcycle":
        motorcycleattack()
    else:
        print("YOU DON'T HAVE THAT")
        still_turn = True
        still_turn = turn """

class player_attack():
    def spear_attack(): 
        lenemyhp = enemyhp - 25
        print(lenemyhp)
        if lenemyhp <= 0:
            print("You have killed your enemy")
    def sword_attack():
        lenemyhp = enemyhp - 30
        print(lenemyhp)
        if lenemyhp <= 0:
            print("You killed the enemy")
    def magic_attack():
        lenemyhp = enemyhp - 40
        print(lenemyhp)
        if lenemyhp <= 0:
            print("You killed the enemy")
    def bike_attack():
        lenemyhp = enemyhp - 70
        print(lenemyhp)
        if lenemyhp <= 0:
            print("You killed the enemy")
    def motor_attack():
        lenemyhp = enemyhp - 100
        print(lenemyhp)
        if lenemyhp <= 0:
            print("You killed the enemy")
        
""" class monster_attack():
    def spider_attack():
 """
