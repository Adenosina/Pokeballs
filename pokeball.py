# Class created so as to be avaible to represent different types of 
# pokeballs.
# There are 3 types of pokeballs, the normal one, the superball and 
# the ultraball 02-10-17.

from graphics import *

def pokeball(win,xcenter,ycenter,color):

	radius = 30
	circle = Circle(Point(xcenter,ycenter),radius)
	circle.setFill(color)
	circle.draw(win)
	p1, p2 = Point(xcenter-radius,ycenter), Point(xcenter+radius,ycenter+radius)
	tapar = Rectangle(p1,p2)
	tapar.setOutline("white")
	tapar.setFill("white")
	tapar.draw(win)
	line = Line(Point(xcenter-radius,ycenter),Point(xcenter+radius,ycenter))
	line.draw(win)
	circle2 = Circle(Point(xcenter,ycenter),radius)
	circle2.draw(win)
	circle3 = Circle(Point(xcenter,ycenter),8)
	circle3.setFill("white")
	circle3.draw(win)
	circle4 = Circle(Point(xcenter,ycenter),4)
	circle4.setFill("black")
	circle4.draw(win)
	
	plists = []
	drawlists = []
	if color == "blue": # Draws a superball 
		for i in [+1,-1]: # Gets the points to create the geometric figures
			p1 = Point(xcenter-i*radius,ycenter-radius+radius/1.5)
			p2 = Point(xcenter-i*radius/3,ycenter-radius+radius/2.5) 
			ptrin1 = Point(xcenter-i*radius,ycenter-radius+radius/2.5)
			ptrin2 = Point(xcenter-i*radius/1.2,ycenter-radius+radius/2.5)
			ptrin3 = Point(xcenter-i*radius,ycenter-radius+radius/1.5)
			for i in [p1,p2,ptrin1,ptrin2,ptrin3]:
				plists.append(i)
		for i in [0,5]: # Creates the figures and save them in a list
			superball1 = Rectangle(plists[0+i],plists[1+i])
			superball1.setFill("red")
			superball2 = Polygon(plists[2+i],plists[3+i],plists[4+i])
			superball2.setFill("white")
			superball2.setOutline("white")
			drawlists.append(superball1)
			drawlists.append(superball2)
		for i in drawlists: # Draw the figures saved in the list
			i.draw(win)
		circle5 = Circle(Point(xcenter,ycenter),radius)
		circle5.draw(win)
	
	plisth = []
	drawlisth = []
	if color == "black": # Draws a ultraball 
		for i in [+1,-1]: # Gets the points to create the geometric figures
			p1 = Point(xcenter-i*radius/1.5,ycenter) 
			p2 = Point(xcenter-i*radius/2.5,ycenter-radius) 
			ptrin1 = Point(xcenter-i*radius/1.5,ycenter-radius/1.3)
			ptrin2 = Point(xcenter-i*radius/1.5,ycenter-radius)
			ptrin3 = Point(xcenter-i*radius/2.5,ycenter-radius)
			for i in [p1,p2,ptrin1,ptrin2,ptrin3]:
				plisth.append(i)
		for i in [0,5]: # Creates the figures and save them in a list
			superball1 = Rectangle(plisth[0+i],plisth[1+i])
			superball1.setFill("yellow")
			superball2 = Polygon(plisth[2+i],plisth[3+i],plisth[4+i])
			superball2.setFill("white")
			superball2.setOutline("white")
			drawlisth.append(superball1)
			drawlisth.append(superball2)
		for i in drawlisth: # Draw the figures saved in the list
			i.draw(win)
		circle5 = Circle(Point(xcenter,ycenter),radius)
		circle5.draw(win)
		
		

		
