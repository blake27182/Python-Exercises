from random import sample

def getList():
	l = int(input("how long? "))
	a = sample(range(1,(l+5)), l)
	return a

def getEnds(a):
	b = [a[0], a[-1]]
	return b

print (getEnds(getList()))