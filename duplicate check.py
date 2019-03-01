import random
import math
a = []
b = []
c = []


rand = math.floor(random.random() * 5 + 5)
for i in range(rand):
	ran = math.floor(random.random() * 20)
	a.append(ran)

rand = math.floor(random.random() * 5 + 5)
for i in range(rand):
	ran = math.floor(random.random() * 20)
	b.append(ran)


print (a)
print (b)

for i in a:
	for n in b:
		if i == n:
			c.append(i)

print ("")
print (c)