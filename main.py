import random
from Introduction import intro
from Room2 import room2
from saving import load, save, mainmenu
from Room2 import ladder, bucket, chair, mattress, carpet
from Room3 import room3
from Room3 import fence, gate, rock, bike, pot
from menu3 import menu3
from Room1 import room1
from menu import menu
from menu4 import menu4
from Room1 import Fridge, Counter, Microwave, Stove, Pantry, Window2, key
from menu2 import menu2
from searchItem import Door, Window, Backpack, Vase, Bucket, Painting, JewelryBox, Rug, Mirror, Bookshelf
codeSegment1 = random.randint(0,9)
codeSegment2 = random.randint(0,9)
codeSegment3 = random.randint(0,9)
code = int(str(codeSegment1) + str(codeSegment2) + str(codeSegment3))
items = ["Door","Window","Backpack","Vase","Bucket","Painting","Jewelry Box","Rug","Mirror","Bookshelf"]
locations = ["Fridge","Counter","Microwave", "Stove","Pantry","Window"]
menu3items = ["Ladder","Bucket","Chair","Mattress","Carpet"]
menu4items = ["Fence", "Gate", "Bike", "Rock", "Pot"]
code1Location = random.randint(1,3)
code2Location = random.randint(4,6)
code3Location = random.randint(7,9)
intro()
while True:
	choice = menu(items, "What do you want to inspect? ")

	if choice == 1:
		Window(choice, code1Location, codeSegment1)
	elif choice == 2:
		Backpack(choice, code1Location, codeSegment1)
	elif choice == 3:
		Vase(choice, code1Location, codeSegment1)
	elif choice == 4:
		Bucket(choice, code2Location, codeSegment2)
	elif choice == 5:
		Painting(choice, code2Location, codeSegment2)
	elif choice == 6:
		JewelryBox(choice, code2Location, codeSegment2)
	elif choice == 7:
		Rug(choice, code3Location, codeSegment3)
	elif choice == 8:
		Mirror(choice, code3Location, codeSegment3)
	elif choice == 9:
		Bookshelf(choice, code3Location, codeSegment3)
	else:
		result = Door(code)
		if result == 1:
			break

room1()
while True:
	choice = menu2(locations, "What do you want to inspect? ")

	if choice == 0:
		Fridge(choice)	
	elif choice == 1:
		key = Counter(choice)
	elif choice == 2:
		Microwave(choice)
	elif choice == 3: 
		Stove(choice)
	elif choice == 4:
		Pantry(choice, key)
		if key:
			break
	elif choice == 5:
		Window2(choice)
	else:
		print("Type a number from 0-5")

room2()
while True:
	choice = menu3(menu3items, "Where do you want to look? ")

	if choice == 0:
		ladder(choice)
	elif choice == 1:
		bucket(choice)
	elif choice == 2:
		chair(choice)
	elif choice == 3:
		mattress(choice)
		break
	elif choice == 4:
		carpet(choice)
	else:
		print("Type a number from 0-4")

room3()
while True:
	choice = menu4(menu4items, "Where do you want to look? ")

	if choice == 0:
		fence(choice)
	elif choice == 1:
		gate(choice, key)
		if key:
			break
	elif choice == 2:
		bike(choice)
	elif choice == 3:
		key = rock(choice)
	elif choice == 4:
		pot(choice)

	