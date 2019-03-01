def reverse(sen):
	a = sen.split(' ')
	b = ' '.join(a[::-1])
	return b

def getString():
	str = input("say something ")
	return str

print (reverse(getString()))