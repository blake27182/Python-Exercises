import json

def new():
	name = input("What is the person's name? ")
	day = input("What is the person's birthday? ")
	birthdays[name] = day
	with open('dics.json', 'w') as file:
		json.dump(birthdays, file)

with open('dics.json', 'r') as file:
	birthdays = json.load(file)


names = [i for i in birthdays.keys()]
print('welcome to birthday land. We know the birthdays of %s' %(', '.join(names)))
search = input("Who's birthday would you like to know? or say new to log a new birthday ")

if search in birthdays:
	print("%s's birthday is %s." %(search,birthdays[search]))
elif search == 'new':
	new()
else:
	print('We dont have him/her')

