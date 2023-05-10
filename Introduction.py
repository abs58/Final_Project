def play():
	print("To play the game enter 1!")
	print("To exit enter 2!")
	print("To see preexisting games enter 3!")


def intro():
	print("Last night, you went to sleep in your own home.")
	print("Now, you wake up to an unfamiliar environement.")
	print("As your eyes flutter open, darkness greets you. Your surroundings are unfamiliar to you.")
	print("You are sitting on a bed, and a wall hugs your back. Beside you is a table, whose outline you can barely see.")
	print("1 - to check under the bed")
	print("2 - to check the table")
	while True:
		bedOrWall = input()
		try:
			if int(bedOrWall) == 1:
				print("Under the bed, you feel a note. But you cannot see to examine it.")
				print("You check the table and find a lamp. With a loud click, your surroundings are illuminated.")
				break
			elif int(bedOrWall) == 2:
				print("You check the table and find a lamp. With a loud click, your surroundings are illuminated.")
				print("You also check under the bed and find a note.")
				break
			else:
				print("Enter either 1 or 2:")
		except:
			print("Value must be whole number 1 or 2:")
			
	print("")
	print("The note reads:")
	print("My dearest participant,")
	print(" If you notice, the door contains a padlock with a three digit code.")
	print(" You will find this code hidden within the room, and must solve it. You shall find three numbers, and must order them correctly.")
	print(" I wish you the best of luck.")
	print("Sincerely, your gracious host.")
	print("")
	print("You examine the room and see:")