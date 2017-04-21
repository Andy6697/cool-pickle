class char:

	def __init__(self,initX, initY, name, char_type):
		self.xpos = initX
		self.ypos = initY
		self.name = name
		self.char_type = char_type
	
	def __str__(self):
		return str(self.char_type) + str(self.name)
	def running(self):
		game_start = input("Start the game by pressing your spacebar.")
		if  game_start == " "
			self.forward()
		return (self.xpos, self.ypos)
	


	def __int__(self):
   	def jump(self):
        self.ypos += 15
        return self.ypos
    def forward(self):
        self.xpos +=10
        return self.xpos
    def backward(self):
        self.xpos -= 10
        return self.xpos
class cactus:
    def __init(self,width,height):
        
                    
def main():
    print("Start")
    p = char(3,3)
    print(p.jump())
    print(p.forward())
    print(p.backward())
main()
