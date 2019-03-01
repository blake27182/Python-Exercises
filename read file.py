name_count = {}
with open('names.txt', 'r') as f:
	line = f.readline().strip('\n')
	while line:
		if line in name_count:
			name_count[line] +=1
		else:
			name_count[line] = 0
		line = f.readline().strip('\n')

with open('names.txt', 'a') as f:
	f.write('\n' + str(name_count))

print('done')