from Room3 import fence
def menu4(list, question):
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