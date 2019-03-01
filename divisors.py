num = int(input("Enter a number: "))
a = []
for i in range(num):
	if num%(i+1) == 0:
		a.append(i+1)
print ("The divisors are: %s" %(a))
if len(a) == 2:
	print ("This number is prime!")