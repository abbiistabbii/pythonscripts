import turtle
import random


turtle.pensize(5)


turnamount = [0, 450, 540, 630]

colour = ["red", "orange", "yellow", "green", "blue", "purple", "black"]

def mainstation():
	turtle.teleport(0,0)
	turtle.seth(90)
	turtle.pencolor(colour[6])
	turtle.circle(10, turnamount[random.randint(0, 3)])
	turtle.right(90)

def lineandstations():
	turtle.forward(15)
	turtle.left(90)
	turtle.forward(5)
	turtle.left(180)
	turtle.forward(5)
	turtle.left(90)

def endstation():
	turtle.forward(10)
	turtle.right(90)
	turtle.pencolor(colour[6])
	turtle.circle(10)

def bendmaker():
	benddirection = random.randint(0, 2)
	if benddirection == 1:
		turtle.right(45)
		turtle.forward(20)
		turtle.right(45)
		for x in range(5, 10):
			lineandstations()
	elif benddirection == 2:
		turtle.left(45)
		turtle.forward(20)
		turtle.left(45)
		for x in range(5, 10):
			lineandstations()
	else:
		for x in range(5, 8):
			lineandstations()



def linemaker():
	mainstation()

	turtle.pencolor(colour[random.randint(0, 5)])

	for x in range(10, 30):
		lineandstations()

	bendmaker()

	endstation()

for x in range(0, 6):
	linemaker()
	mainstation

turtle.done()
