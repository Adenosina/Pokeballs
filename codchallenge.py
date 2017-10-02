# Creates a random mosaic of pokeballs.

from graphics import *
from random import *
from pokeball import *

def codchallenge76(color1,color2,color3):
	width, lenght = 1200, 800
	win = GraphWin("CodChallenge76",width,lenght)
	win.setBackground("white")
	spacing, x, y = 100, 50, 40
	Pokeball = pokeball(win,x,y,color1)
	Superball = pokeball(win,x,y,color2)
	Ultraball = pokeball(win,x,y,color3)
	
	genlist = []
	while True:
		if random() < 0.3:
			x += spacing
			Pokeball = pokeball(win,x,y,color1)
			genlist.append(Pokeball)
		elif 0.3 <= random() < 0.6:
			x += spacing
			Superball = pokeball(win,x,y,color2)
			genlist.append(Superball)
		else:
			x += spacing
			Ultraball = pokeball(win,x,y,color3)
			genlist.append(Ultraball)
		if x > width:
			x = -50
			y += spacing
		if y > 800:
			break
		
	for i in genlist:
		i.draw(win)

