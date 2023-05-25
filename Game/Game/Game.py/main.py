"""import classes
from everything import Weapon"""

def introd():
    print(f"There was once a great adventurer of great renown by the name of {Adventure_name} who explored the whole world")
    print(f"One of many great stories told were of {Adventure_name} great adventures in the Dungeon of The Eldrich Flower god")
    print(f"After {Adventure_name} set off from a nearby village he stumbled apoun an ononimous cavern")
    print(f"After {Adventure_name} entered he found 3 pathways in a large lit room")
introd()
decision_1 = input("What route should they go down? Dark, Eerie, or Lit")
roomid == "0"
def Eerie():
  print("what")


def gamesplit():
  if decision_1 == "Dark":
    print("You reach a dimly lit room, and a chest can be seen on one side and a passage on the other.")
  elif decision_1 == "Eerie":
    number_generator()
    if n >= 9:
      print("You get lost and end up wandering into a room full of flames and die")
      endingscenedie()
    else:
      print("You navigate the cave end up in a dark room")
      roomid == 1
      Eerie()





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
    endingscenewater()

def endingscenewater():
  print("Reaching a large body of water underground you decide to leave")
  exit()


def endingrelic():
  print("In a large decorated room seems to be an artifact floating in the center")
  print("After retrieving the unknown artifact and escaping ")
  exit
def endinggolden():
  print("In a large decorated room seems to be an artifact floating in the center")
  print("After retrieving the unknow artifact and escaping ")
  
  