def Door(code):
	print("You walk to the door. The rotary padlock contains three digits. You enter a code")
	while True:
		try:
			option1 = int(input("Digit one: "))
			break
		except:
			print("Digit one must be a whole number between 0-9:")

	while True:
		try:
			option2 = int(input("Digit two: "))
			break
		except:
			print("Digit two must be a whole number between 0-9:")

	while True:
		try:
			option3 = int(input("Digit three: "))
			break
		except:
			print("Digit three must be a whole number between 0-9:")
	chosenCode = int(str(option1) + str(option2) + str(option3))
	print("")
	if chosenCode == code:
		print("You hear a click, and the padlock shifts. As you press open the door you are greeted to a kitchen. You step inside.")
		return (1)
	else:
		print("You jiggle the padlock, but to no avail. The code is incorrect.")
		return(0)

def Window(choice, codeLocation, codeValue):
	print("")
	print("You look at the window. It's dark, and damp. Mold grows along the edges and you cannot see through its musty panes.")
	if choice == codeLocation:
		print("Carved into the edging, you see the number " + str(codeValue) + ".")
		print("")
	else:
		print("You find no code.")
		print("")

def Backpack(choice, codeLocation, codeValue):
	print("")
	print("The backpack is your personal bag. Strange. You thought you lost it weeks ago.")
	if choice == codeLocation:
		print("Within the front pocket, you see the number " + str(codeValue) + " written on a crumpled note.")
		print("")
	else:
		print("You find no code.")
		print("")

def Vase(choice, codeLocation, codeValue):
	print("")
	print("A dark blue vase holds roses that seem to have died long ago.")
	if choice == codeLocation:
		print("On the base, you see the number " + str(codeValue) + ".")
		print("")
	else:
		print("You find no code.")
		print("")

def Bucket(choice, codeLocation, codeValue):
	print("")
	print("The bucket sits in the middle of the floor. It catches a gentle leak from the dank ceiling.")
	if choice == codeLocation:
		print("Within, you see exactly " + str(codeValue) + " stones.")
		print("")
	else:
		print("You find no code.")
		print("")

def Painting(choice, codeLocation, codeValue):
	print("")
	print("Has Mona Lisa always been this creepy? Her eyes peer into you, her smile gleams as if she knows the fate that awaits you unless you find the code.")
	if choice == codeLocation:
		print("Painted in the corner, you see the number " + str(codeValue) + ".")
		print("")
	else:
		print("You find no code.")
		print("")

def JewelryBox(choice, codeLocation, codeValue):
	print("")
	print("The oak Jewelry Box creeks open and gentle music fills the room. The music may have once been soothing, but years of age has ruined this once peaceful melody.")
	if choice == codeLocation:
		print("Etched inside the lid, you see the number " + str(codeValue) + ".")
		print("")
	else:
		print("You find no code.")
		print("")

def Rug(choice, codeLocation, codeValue):
	print("")
	print("A dusty woven rug adorns the otherwise ragged wooden floor, adding a hint of color to the eery room.")
	if choice == codeLocation:
		print("Carved onto the floor beneath, you see the number " + str(codeValue) + ".")
		print("")
	else:
		print("You find no code.")
		print("")

def Mirror(choice, codeLocation, codeValue):
	print("")
	print("The mirror is grimey and unpleseant. The unnatural reflection leers back at you. The circles under your eyes are dark and full. It offers little comfort.")
	if choice == codeLocation:
		print("As you study your reflection, you notice the number " + str(codeValue) + " painted onto your shirt.")
		print("")
	else:
		print("You find no code.")
		print("")

def Bookshelf(choice, codeLocation, codeValue):
	print("")
	print("A bookshelf filled with old, unkempt books. It is sad to see them so run down.")
	if choice == codeLocation:
		print("You notice the books are all the same volume. The volume number is " + str(codeValue) + ".")
		print("")
	else:
		print("You find no code.")
		print("")