x = int(input("give me a prime motherfucker "))

def check(x):
	count = 0
	for i in range(x):
		if count > 2:
			break
		if x%(i+1) == 0:
			count += 1

	if count > 2:
		prime = False
	else:
		prime = True
	return prime


if check(x):
	print("thank you")
else:
	print("that is not a prime you bitch.")