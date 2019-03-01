def sequence(seed, l):
	a = []
	count = 0
	while count < 2:
		a.append(seed)
		count += 1
	while count < l:
		a.append(a[-1]+a[-2])
		count += 1
	return a

def seed():
	s = int(input("enter a seed "))
	return s

def length():
	l = int(input("enter length "))
	return l

print (sequence(seed(),length()))