import random

yes = ["Yes, however, there is a steep cost", "Indeed, the Consortium has been notifed", "The Old Gods state yes, the Sacrifice will be made"]
no = ["It is not to be, a dire fate awaits you", "Alas no, for you have been chosen as a sacrifice.", "The Old Gods have decided your fate, and it is a grim one."]
unclear = ["The void is as silent as the grave", "The government holds many secrets, this may be one of them", "Yes, no, it matters not to An Dubhnachd."]

def thechooser():
	choosernumb = random.randint(0, 2)
	optionnumb = random.randint(0, 2)
	if choosernumb == 0:
		print(yes[optionnumb])
	elif choosernumb == 1:
		print(no[optionnumb])
	else:
		print(unclear[optionnumb])

print("I am Egdar, the Ominous 8-Ball.")
print("I see everything, I see all.")
print("Give me a question, yes or no")
print("and the answer, I shall show.")

question = input("What is your question, mortal? ")

print(question + "?")

thechooser()
