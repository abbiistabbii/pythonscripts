import random

list = []

def iteminput():
	item = input("Insert choice ")
	list.append(item)
	arewedone()

def arewedone():
	yesorno = input("Is that all? y/n ")
	if yesorno == "y":
		spin()
	elif yesorno == "n":
		iteminput()
	else:
		print("Sorry, type y or n")
		arewedone()

def spin():
	listlength = len(list)
	choice = random.randint(0, listlength)
	print("The winner is " + list[choice])

iteminput()

