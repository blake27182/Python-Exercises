import random, time


a = random.sample(range(1,5000000), 4900000)
# a = [1,2,3,5,6,8,9,10,11,15,20,23,24,25,27,28]
a.sort()

def search(num, lst):
	idx = [0,len(lst)-1]
	# print(idx)
	rslt = False
	# count = 0
	while idx[1]-idx[0]>1:
		mdpt = (idx[0]+idx[1])//2

		if num == lst[idx[0]]:
			rslt = True
			break
		elif num == lst[idx[1]]:
			rslt = True
			break

		elif num < lst[mdpt]:
			idx[1] = mdpt
		elif num > lst[mdpt]:
			idx[0] = mdpt
		elif num == lst[mdpt]:
			rslt = True
			break
		# print(idx,mdpt)
		# count += 1
	# print(count)
	return rslt
	
if __name__=="__main__":
	x = int(input("Are you a stupid-ass bitch? Enter a number to find out "))
	start = time.time()
	print(search(x, a))
	end = time.time()
	print(end-start)
	start = time.time()
	print(x in a)
	end = time.time()
	print(end-start)