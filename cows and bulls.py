import random

def printresults(num, guess):
	cows = 0
	bulls = 0
	num = list(str(num))
	guess = list(str(guess))

	for i in range(len(guess)):
		# count cows, change guess list and num list
		if guess[i] == num[i]:
			cows += 1
			guess[i] = 'cow'
			num[i] = 'none'
		# print(num,guess)
	for i in range(len(guess)):
		# count bulls, change both lists for that index
		if guess[i] in num:
			bulls += 1
			guess[i] = 'bull'
		# print(num,guess)
	print('cows: %s bulls: %s' %(cows,bulls))

def getGuess(tries):
	if tries > 0:
		print()
	g = int(input("Guess a four digit number: "))
	return g

def newNumber():
	return random.randint(1000,9999)

def game():
	count = 0
	x = newNumber()
	# print (x)
	y = 1
	while x != y:
		y = getGuess(count)
		if y == 0:
			break
		elif len(str(y)) == len(str(x)):
			printresults(x, y)
			count += 1
		else:
			print('read the instructions you bitch')
			continue
	if x == y:
		print('good job, it only took you %s tries' %(count))
	return y


while quit != 0:
	quit = game()

print("Fuck you")