overlap = []

with open('primes.txt', 'r') as p, open('happy.txt', 'r') as h:
	lp = p.readline()
	hfile = h.read()
	while lp:
		if lp in hfile:
			overlap.append(lp.strip())
		lp = p.readline()
print(overlap)