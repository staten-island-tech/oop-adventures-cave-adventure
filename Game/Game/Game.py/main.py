import classes

""" def character_creation():
    Adventurer_name = input("What is the name of your adventurer?")
    print(f"One upon a time, "+ Adventurer_name +" stumbled upon a cave and goes in to explore it.")
    print(f"Then, " + Adventurer_name + " came across 3 routes leading further down into the cave, but doesn't know which one to go down") """
decision_1 = input("What routew should they go down? Dark, Eerie, or Lit")
roomid == "0"
def Eerie():
  print("")


def gamesplit():
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

def secondsences():
  if roomid == 1:



def puzzlemath():
  print("You enter a room with the a question engraved into the ground")
  print("6 x 7 = ")
  mathanswer = input("a. 420 b.42 c.69")
  if mathanswer == "42":
    roomid = 20
  else:
    endingscenedie()

def stumble():
  number_generator()
  if n >=5:
    print("you suffer head damage")
    concus = "YEs"
  else:
    print("continue on smoothly")


\