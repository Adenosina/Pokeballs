# Creates a random pokeball mosaic

from graphics import *
from random import *
from pokeball import *

def codchallenge76(color1,color2, probcolor1):

	width, lenght = 1200, 800
	win = GraphWin("CodChallenge76",width,lenght)
	win.setBackground("white")

	spacing = 100

	x, y = 50, 40

	redleaf = pokeball(win,x,y,color1)
	blueleaf = pokeball(win,x,y,color2)
	genlist = []
	
	while True:
			
		if random() < probcolor1:
			x += spacing
			redleaf = pokeball(win,x,y,color1)
			genlist.append(redleaf)

		else:
			x += spacing
			blueleaf = pokeball(win,x,y,color2)
			genlist.append(blueleaf)

		if x > width:
			x = -50
			y += spacing
		
		if y > 800:
			break

	for i in genlist:
		i.draw(win)


