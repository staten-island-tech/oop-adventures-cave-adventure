
def magicheal():
    def endingscenedie():
        print("has unfortunatley died ")
        print(inventory)
    retry = input("Would you like to retry Y / N ")
    if retry == "N":
        exit()
    playerhp = 100
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


