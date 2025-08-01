import turtle
import random


turtle.pensize(5)


colour = ["red", "orange", "yellow", "green", "blue", "purple", "black"]
stationnames = ["Princes Street", "Bankhead", "Saughton", "Balgreen", "Murrayfield", "Haymarket", "West End", "Ocean Terminal"]
circ = 360
stanumb = 0

def stationname():

	stationnamechosen = stationnames[stanumb]
	offsetx = 11
	offsety = 11
	turtle.teleport(turtle.xcor() + offsetx, turtle.ycor() + offsety)
	turtle.write(stationnamechosen, align="left")
	turtle.teleport(turtle.xcor() - offsetx, turtle.ycor() - offsety)

def mainstation():
	turtle.seth(90)
	turtle.teleport(0,0)
	turtle.pencolor(colour[6])
	turtle.circle(10, circ)
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
	turtle.pencolor("black")
	turtle.circle(10)
	stationname()

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


turtle.teleport(0, 0)
turtle.seth(90)
stationname()
for x in range(0, 4):
	stanumb += 1
	linemaker()
	circ += 90

turtle.teleport(0,0)
turtle.seth(90)
turtle.circle(10)


turtle.done()

