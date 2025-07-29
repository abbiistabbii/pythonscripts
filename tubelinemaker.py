# Let's import some modules!
# Turtle for drawing, random for random numbers.
import turtle
import random


# This sets the line colour :3
linecolor = ["red", "blue", "green", "yellow"]
# These are the Random Numbr generators
# linenumb sets the line colour
# stop numb sets the number of stops
# turngen decides if we have a turn in our line and if so, which way!
linenumb = random.randint(0,3)
stopnumb = random.randint(4,10)
turngen = random.randint(0,2)

# This offsets the starting point of the line depending if it is heading
# north (up) or south (down)
if turngen == 1:
	turtle.teleport(-200, 100)
elif turngen == 2:
	turtle.teleport(-200, -100)
else:
	turtle.teleport(-200, 0)
# pensize sset to 5
turtle.pensize(5)
# This creates the end stations
def mainstation():
	turtle.pencolor("black")
	turtle.circle(10, 450)
	turtle.right(90)
# This creates the intermediate stops
def lineandstop():
	turtle.pencolor(linecolor[linenumb])
	turtle.forward(20)
	turtle.left(90)
	turtle.forward(5)
	turtle.left(180)
	turtle.forward(5)
	turtle.left(90)
# This creates the station at the end of the line
def endofline():
	turtle.forward(20)
	turtle.right(90)
	mainstation()
# this decides the number of stations on the line between the main stations
def linegenerator():
	for x in range(stopnumb):
		lineandstop()

mainstation()

linegenerator()

if turngen == 1:
	turtle.right(45)
	turtle.forward(20)
	turtle.right(45)
	linegenerator()
elif turngen == 2:
	turtle.left(45)
	turtle.forward(20)
	turtle.left(45)
else:
	pass

linegenerator()

endofline()

turtle.done()
# it done :3
