import random
random.randint


    inventory = []

def randomchest():
    inventory = []
    N = "N"
    while N == "N":
        Random = random.randint(1,10)
        if Random == "1":
            if inventory in "10* sword":
                return
            else:
                inventory.append("10* sword")
        if Random == "2":
            print("nothing")
        if Random == "3":
            if inventory in "sand magic":
                return
            else:
                inventory.append("sand magic")            
        if Random == "4":
            if inventory in "throwable bike":
                return
            else:            
                inventory.append("throwable bike")
        if Random == "5":
            if inventory in "throwable motorcycle":
                return
            else:            
                inventory.append("throwable motorcycle")
        if Random == "6":
            if inventory in "cloth":
                return
            else:            
                inventory.append("cloth")
        if Random == "7":
            if inventory in "health potion":
                return
            else:            
                inventory.append("health potion")
        if Random == "8":
            if inventory in "greathealth":
                return
            else:            
                inventory.append("greathealth")
        if Random == "9":
            if inventory in "coke":
                return
            else:            
                inventory.append("coke")
        if Random == "10":
            if inventory in "unknown":
                return
            else:            
                inventory.append("unknown")
        print(inventory)
        N = "U"
    print(inventory)
randomchest()


