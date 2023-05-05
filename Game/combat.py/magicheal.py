
def magicheal():
    def endingscenedie ():
        print("you died")
    playerhp = int(input("hp input "))
    if playerhp <= int(0):
        endingscenedie()
    elif playerhp >= int(1):
        playerhp
        eplayerhp = playerhp + 20
        if eplayerhp > 100:
            eplayerhp = 100 
            print(eplayerhp)
        else:
            print(eplayerhp)
magicheal()

