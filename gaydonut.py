import turtle

wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Turtle")
curs = turtle.Turtle()
curs.speed(100)

hue = ["red", "orange", "yellow", "green", "blue", "purple"]

c = 0

for x in range(360):
	curs.color(hue[c])
	curs.circle(100)
	curs.forward(1)
	curs.right(1)
	if c < 5:
		c += 1
	else:
		c = 0

turtle.done()
