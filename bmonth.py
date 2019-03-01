from bokeh.plotting import figure, show, output_file
import json

with open('dics.json', 'r') as file:
	birthdays = json.load(file)

months = {}

for i in birthdays.values():
	date = i.split('/')
	mo = date[0]
	if mo in months:
		months[mo] += 1
	else:
		months[mo] = 1
		
print(months)

output_file('plot.html')
x = [int(i) for i in months]
y = [i for i in months.values()]
p = figure()
p.vbar(x=x, top=y, width=.5)
show(p)