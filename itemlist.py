import random
random.randint

def hpcheck():
    playerhp = int(input("hp input "))
    if playerhp <= int(0):
        endingscenedie()
    if playerhp >= int(100):
        playerhp = 100
    print(playerhp)

Adventurer_name = "Slab"
retry = "Y"
def endingscenedie():
    print(f"{Adventurer_name} has unfortunatley died ")
    retry = input("Would you like to retry Y / N ")
    if retry == "N":
        exit()


def okending():
    print(f"{Adventurer_name} has escaped the mysterious cave with more than he had ")
    print(inventory)
    retry = input("Would you like to retry Y / N ")
    if retry == "N":
        exit()




hpcheck()

enemyhp = 100

while enemyhp > 0:
    i

""" """

inventory = []
def randomchest():
    N = "N"
    while N == "N":
        Random = random.randint(1,9)
        print(Random)
        if Random == "1":
            inventory.append("10* sword")
        if Random == "2":
            inventory.append("bow")
        if Random == "3":
            inventory.append("")            
        if Random == "4":
            inventory.append("")
        if Random == "5":
            inventory.append("")
        if Random == "6":
            inventory.append("")
        if Random == "7":
            inventory.append("")
        if Random == "8":
            inventory.append("")
        if Random == "9":
            inventory.append("")
        print(inventory)
randomchest()


def clothheal():
    playerhp +20 
    print(playerhp)