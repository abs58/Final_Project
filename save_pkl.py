import pickle

name = []

def save(game): 
	with open('save_pkl.py', 'wb') as f:
		pickle.dump(name, f)
		print("Saved!")
def load():
	with open('save_pkl.py', 'wb') as f:
		name = pickle.load(f)
	print(name)

def new():
	name = input("Enter player's name:\n")
	return game