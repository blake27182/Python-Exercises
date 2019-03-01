import random

def getWord():
	with open('sowpods.txt', 'r') as file:
		return random.choice(file.readlines()).strip()
