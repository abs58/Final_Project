def load():
	name = input("Enter player's name\n")
	with shelve.open('game.bin') as file:
		return file.get(name, None)

def save(game): 
	with shelve.open("game.bin") as file: 
		file[game.name] = game
		

class SavedGames():
	def __init__(name):
		self.__name = name

	@property
	def name(self):
		return self.__name

def mainmenu(choice):
	print("")
	print("1 Load\n2 Save\n3 New Game")
	if input == 1:
		load()
	elif choice == 2:
		save(game)
	elif choice == 3:
		new()
	else:
		print("Please choose a number 1-3.")
		