import random

class Obstacle:
#Made a class for my obstacles with an x and y value.
	def __init__ (self,x,y):
		self.x = x
		self.y = y
#Made a function that makes it into a cactus, with a random width and random height based on the width. Returns these values.
	def cactus(self):	
		self.width = random.randrange(20,30)
		self.height = self.width * 2
		return(self.width, self.height)
#Made a function that makes it into a cloud, with a random width and random height based on the width. Returns these values.
	def cloud(self):
		self. width = random.randrange(40,60)
		self.height = self.width // 3
		return(self.width, self.height)
#Made a function that moves the thing, going back at a certain dist in the x direction towards the player, who has to jump over or duck under them.
	def move(self,dist):
		self.x -=dist
		return(self.x)

class Dino:
#Made a class for my dinosaur player with an x and y position
	def __init__(self,xpos = 0,ypos = 0):
		self.xpos = xpos
		self.ypos = ypos
#Gave it a function of jump that lets it go up in the y direction a constant 70 pixels.
	def jump(self):
		self.ypos += 70
		return self.ypos
#Gave it a function of forward that lets it go forward in the x direction a specified distance
	def forward(self,dist):
		self.xpos +=dist
		return self.xpos



