from Room1 import Fridge
def menu2(list, question):
	for item in list:
		print(list.index(item), item)

	while True:
		result = input(question)
		try:
			result = int(result)
			break
		except: 
			print("Please type a number.")

	return result

	