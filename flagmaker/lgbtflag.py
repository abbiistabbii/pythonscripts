import turtle

turtle.seth(0)

colours = ["red", "orange", "yellow", "green", "blue", "purple"]

x = 0
posx = 0
posy = 0


for x in range(6):
	turtle.color(colours[x])
	for x in range(40):
		turtle.forward(400)
		posy -= 1
		turtle.teleport(posx, posy)

	x += 1

turtle.done()
