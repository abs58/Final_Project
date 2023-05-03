from Room4 import room4
key = False

def room3():
	print("")

def fence(choice):
	print("")
	print("You go near the fence but it seems too high to climb. Maybe look for another way out?")

def gate(choice, key):
	print("")
	if key:
		print("You put the key in the lock and the gate shakes open. You step out and see a sidewalk. You start running.")
		room4()
	else:
		print("You see that there's a lock on the gate keeping it shut. Let's try finding a key.")

def bike(choice):
	print("")
	print("You notice a bike laying in the middle of the field. That's not too useful though.")

def rock(choice):
	print("")
	print("As you're walking around the field, you stumble over a rock. You look down and see there's a key next to it! You pick it up.")
	key = True
	return key

def pot(choice):
	print("")
	print("You see a pot that has a dead flower in it. A spider is crawling around in the dirt.")