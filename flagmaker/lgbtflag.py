import turtle

turtle.seth(0)

colours = ["red", "orange", "yellow", "green", "blue", "purple"]

x = 0

def stripe():
	for x in range(10):
		turtle.forward(200)
		turtle.right(90)
		turtle.forward(1)
		turtle.right(90)
		turtle.forward(200)
		turtle.left(90)
		turtle.forward(1)
		turtle.left(90)

for x in range (6):
	turtle.color(colours[x])
	stripe()
	x += 1

turtle.done()
