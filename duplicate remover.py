import random

a = []
for i in range(15):
	a.append(random.randint(1,15))

b = set(a)

print (a)
print (b)