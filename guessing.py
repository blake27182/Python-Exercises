from random import randint

x = randint(1,9)
y = input("Guess what I'm thinking, motherfucker ")

while y != "uncle":
	if int(y)<x:
		print()
		print ("Higher, bitch ")
		y = input("Guess again ")

	elif int(y)>x:
		print()
		print ("Lower ")
		y = input("Guess again ")

	else:
		print()
		print ("wow, good job")
		x = randint(1,10)
		y = input("Guess what I'm thinking, motherfucker ")
		
print ("Pussy")