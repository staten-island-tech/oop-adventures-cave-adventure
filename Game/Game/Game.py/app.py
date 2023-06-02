import random

class random_1:
  def randomchest():
    inventory = []
    Random = random.randint(1,10)
    if Random == "1":
            if "flame_sword" in inventory:
                return
            else:
                inventory.append("flame_sword")
    if Random == "2":
            print("nothing")
    if Random == "3":
            if "sand_magic" in inventory:
                return
            else:
                inventory.append("sand_magic")            
    if Random == "4":
            if "throwable_bike" in inventory:
                return
            else:            
                inventory.append("throwable_bike")
    if Random == "5":
            if "throwable_motorcycle" in inventory:
                return
            else:            
                inventory.append("throwable_motorcycle")
    if Random == "6":
            if "bandage" in inventory:
                return
            else:            
                inventory.append("bandage")
    if Random == "7":
            if "health_potion" in inventory:
                return
            else:            
                inventory.append("health_potion")
    if Random == "8":
            if "great_health_potion" in inventory:
                return
            else:            
                inventory.append("great_health_potion")
    if Random == "9":
            if "coke" in inventory:
                return
            else:            
                inventory.append("coke")
    if Random == "10":
            if inventory in "unknown":
                return
            else:            
                inventory.append("unknown")
            print(inventory)
  def random():
    def endingscenedie():
        retry = input("You have died. Would you like to retry? Y / N ")
        if retry.upper == "N":
            exit()
    n = random.randint(1,10)
    if n <= 9:
      endingscenedie()
    else:
      print("You enter a room with a huge wall with random symbols.")






""" def gamesplit():
  if decision_1 == "Dark":
    print("You reach a dimly lit room, and a chest can be seen on one side and a passage on the other.")
  elif decision_1 == "Lit":
    print("You step into a giant garden filled with flora.")
    number_generator()
    if n >= 6:
      Garden_God()
      while x == "Y":
        Garden_God()
    else: 
       print("You carefully make your way through the garden and find a chest.")
       randomchest()
  elif decision_1 == "Eerie":
    number_generator()
    if n >= 9:
      print("You get lost and end up wandering into a room full of flames and die")
      endingscenedie()
    else:
      print("You navigate the cave end up in a dark room")
      roomid == 1
      Eerie()

gamesplit()




def puzzlemath():
  print("You enter a room with the a question engraved into the ground")
  print("6 x 7 = ")
  mathanswer = input("a. 420 b.42 c.69")
  if mathanswer == "42":
    roomid = 20
    print("You obatin a flower crown")
    flowercrown == "Yes"
    inventory.append("flowercrown")
  else:
    endingscenedie()

def stumble():
  number_generator()
  if n >=5:
    print("you suffer head damage")
    concus = "YEs"
  else:
    print("continue on smoothly")

def shrine():
  print("You discover a room with a shrine with a pedestal")
  question1 = input("Whould you like to place an item on the pedestal? Y/N ")
  if question1 == "Y":
    print(inventory)
    while shrinechoice not in inventory:
      shrinechoice = input("What item do you choose to go on the pedestal? ")
    if shrinechoice == "flower crown":
      print("You reveive a blessing.")
      soda == "Yes"
    else:
      endingscenedie()

def underwatercave():
  print("you reach a cavern with a deep pool of water ")
  ucavedecison = input("dive into the pool of water Y/N or leave")
  if ucavedecison == "Y":
    print("You dive under the surface of the water and swim into another cave.")
  elif ucavedecison == "N":
    endingscenewater() """


