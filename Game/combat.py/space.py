def space ():
    print(inventory)
    input_3 = ("What would you like to use?")
    if input_3.lower == "bandage":
        playerhp + 30
        print(playerhp)
    elif input_3.lower == "health potion":
        playerhp + 60
        print(playerhp)
    elif input_3.lower == "great health potion":
        playerhp + 90
        print(playerhp)
    elif input_3.lower == "soda":
        print("The sweet flavor of the soda rejuvenates your weary body. You feel a new wave of power.")
        ailments.append("soda")
    else:
        endingscenedie()
        def endingscenedie():
            print(f"{Adventurer_name} has unfortunatley died ")
            print(inventory)
        retry = input("Would you like to retry Y / N ")
        if retry == "N":
            exit()
