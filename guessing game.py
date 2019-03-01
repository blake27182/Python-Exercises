import time

def guess(rng):
	if rng[1]-rng[0] > 1:
		return (rng[0]+rng[1])//2
	else:
		return rng[0]

def correctRange(rng, gss, correction):
	if correction == 'higher':
		rng[0] = gss+1
	elif correction == 'lower':
		rng[1] = gss-1


if __name__ == '__main__':
	print("Think of a number between 1 and 100")
	time.sleep(3)
	answer = 'no'
	rng = [1,100]
	count = 0
	while answer == 'no':
		gss = guess(rng)
		answer = input('Is it %s? (yes or no) ' %(gss))
		if answer == 'no':
			correction = input('higher or lower? ')
			correctRange(rng, gss, correction)
		count += 1
	print('Took me %s tries' %(count))