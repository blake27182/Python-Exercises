import raword

answer = 'yes'
while answer == 'yes':
	word = raword.getWord()
	word = list(word)
	right = ['_' for i in word]
	wrong = 6

	while '_' in right and wrong>0:
		guess = input('Guess a letter ').upper()
		if guess in word:
			for i in range(len(word)):
				if word[i] == guess:
					right[i] = guess
			print(' '.join(right))
		else: 
			wrong -= 1
			if wrong>1:
				print('Nope. You have %s wrong guesses left' %(wrong))
			elif wrong>0:
				print('Nope. You have %s wrong guess left' %(wrong))
	if wrong > 0:
		print('You won!')
	else:
		print('you suck')
		print('It was ',''.join(word))
		answer = input("Do you want to play again? ")