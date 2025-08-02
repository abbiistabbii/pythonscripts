import turtle
turtle.bgcolor("black")
turtle.speed(0)

colours = ["#5bcffa", "#f5abb9", "#ffffff", "#f5abb9", "#5bcffa"]

colx = 0
turtle.color(colours[colx])

posx = -200
posy = 200
sizex = 300
sizey = 40



turtle.teleport(posx, posy)


for x in range(5):
	turtle.color(colours[colx])
	for y in range(sizey):
		turtle.forward(sizex)
		posy -= 1
		turtle.teleport(posx, posy)
	colx += 1

turtle.done()
