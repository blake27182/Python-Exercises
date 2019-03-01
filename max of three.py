def maxi(x,y,z):
	m = x
	if y > m:
		m = y
	if z > m:
		m = z
	return m

print(maxi(56,21,83))