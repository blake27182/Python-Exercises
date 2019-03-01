h = int(input("How high: "))
w = int(input("how wide: "))
def row(rv, rh):
	print('    '.join(rv))
	print(' '.join(rh))


def printyPrint(h, w):
	rh = [' ---']*w
	rv = ['|']*(w+1)
	print(' '.join(rh))
	for i in range(h):
		row(rv, rh)


printyPrint(h, w)