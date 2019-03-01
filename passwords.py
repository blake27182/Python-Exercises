import random as ra
l = 1

def main(l):
	a = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVQXYZ1234567890!@#$%^&*'
	print(''.join(ra.sample(a,l)))

while l != 0:
	l = int(input("How long do you want it you perv? "))
	main(l)