import lab10

def main():
	#Creates two obstacles with different specified positions and the dinosaur, which is at the origin.
	print("Obstacle and dino model Test")
	cactusguy = lab10.Obstacle(200,0) 
	cloudguy = lab10.Obstacle(250,50)
	dinoguy = lab10.Dino()
	#Uses the functions in each of the classes with randomly inputted numbers for move, forward, and backwards.
	print("standard input")
	print(cactusguy.cactus())
	print(cactusguy.move(20)) 
	print(cloudguy.cloud())
	print(cloudguy.move(25))
	print(dinoguy.forward(50))
	print(dinoguy.backward(60))
	print(dinoguy.jump())
	#Does the same thing with large numbers for just the functions that you can input things into 
	print("Out of bounds input test")
	print(cactusguy.move(100000000))
	print(cloudguy.move(100000000)) 
	print(dinoguy.forward(10000000))
	print(dinoguy.backward(10000000))
	#Does the same thing but with zero
	print("Zero input")
	print(dinoguy.forward(0))
	print(dinoguy.backward(0))
	print(cactusguy.move(0))
	print(cloudguy.move(0)) 
	#Does the same with negative numbers
	print("Negative input test")
	print(dinoguy.forward(-1))
	print(dinoguy.backward(-1))
	print(cactusguy.move(-1))
	print(cloudguy.move(-1)) 
main()
