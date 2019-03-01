import datetime


name = input("Please enter your name: ")
age = int(input("Please enter your current age: "))

now = datetime.datetime.now().year
year100 = (100 - age) + now

print ("Thank you %s. You will turn 100 in the year %s" %(name,year100))