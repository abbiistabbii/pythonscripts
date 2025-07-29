import turtle
import random

wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Turtle")
curs = turtle.Turtle()
curs.speed(1)

for x in range(100):
	r = random.randint(10, 100)
	curs.forward(r)
	r = random.randint(45, 180)
	curs.right(r)

turtle.done()
