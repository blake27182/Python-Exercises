word = input("Enter a word or phrase: ")
a = list(word)

def despace(a):
	x = len(a)
	i = 0
	while i < x:
		if a[i] == ' ':
			a.pop(i)
			i -= 1
			x -= 1
		i += 1

def check(a):
	i = 0
	j = len(a)-1
	while i < j:
		if a[i] != a[j]:
			return False
			break
		else:
			return True
		i += 1
		j -= 1
		
despace(a)
if check(a) is True:
	print ('This is a palindrome!')
else:
	print ('This is not a palindrome')