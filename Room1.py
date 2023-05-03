from Room2 import room2
key = False
def room1():
	print("")
	
def Fridge(choice):
	print("")
	print("You open the fridge to find moldy food. At the back you see a broken light bulb. You shut the door.")

def Counter(choice):
	print("")
	print("You see a key laying on the counter. You pick it up.")
	key = True
	return key

def Microwave(choice):
	print("")
	print("You open up the microwave door and a rat is staring back at you. You quickly shut it.")

def Stove(choice):
	print("")
	print("You notice there are some matches lying ontop of one of the burners. You pick them up.")

def Pantry(choice, key):
	print("")
	if key:
		print("You insert the key and the door opens! You realize it's not a pantry, but instead a set of stairs leading down. You start to descend.")
		room2()
	else:
		print("")
		print("You try to open the door, but it's locked. Try finding a key.")

def Window2(choice):
	print("")
	print("You look out the window but can't see anything except dead grass.")
