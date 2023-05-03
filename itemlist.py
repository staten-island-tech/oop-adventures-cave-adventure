def hpcheck():
    playerhp = int(input("hp input "))
    if playerhp <= int(0):
        endingscenedie()
    if playerhp >= int(100):
        playerhp = 100
    print(playerhp)

"""def mad_lib():
    adjective = input("please enter a adjective ")
    verb = input("please enter a verb ")
    celeb = input("please enter a celebrity ")
    number = input("please enter a number ")
    verb2 = input("please enter a verb ")
    print(f"It was normal {adjective} day as I watched someone {verb} with {celeb} for {number} days and then {verb2}")"""
Adventurer_name = "Slab"
retry = "Y"
def endingscenedie():
    print(f"{Adventurer_name} has finally died ")
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