# Hewo der! :3
#
# This is a colour cycler! It makes a multi-colour circle!
# I made it so I could test out how to switch colours through RGB codes and code!

# Import turtle and Turtle settings
import turtle
turtle.colormode(255)
turtle.speed(0)
turtle.pensize(2)

# This is where we keep the colour codes!
r = 255
g = 0
b = 0

y = 0 # "y" is for the y postition of the Turtle!
cr = 1 # "cr" is the  cirle radius. It increases by 1 for every loop
inc = 5 # this is how much the rgb codes increase by! If you wanna slow the colour cycle, you can  set it to 1.
max = 255 # The max number an RGB Code can be!

# this is the colour changer loop!

for x in range(1528):
	if r == max and g != max and b == 0:
		g += inc
	elif r != 0  and g == max and b == 0:
		r -= inc
	elif r == 0 and g == max and b != max:
		b += inc
	elif r == 0 and g != 0 and b == max:
		g -= inc
	elif r != max and g == 0 and b == max:
		r += inc
	elif r == max and g == 0 and b != 0:
		b -= inc

	print(str(r)) # I print this in the term to make sure the RGB codes are working correctly.
	print(str(g)) # You can comment them out if you don't want them.
	print(str(b))
	print(" ")
	turtle.color(r, g, b)
	turtle.circle(cr)
	y -= 1
	cr += 1
	turtle.teleport(0, y)

turtle.done()
