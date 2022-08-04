#!/bin/pyhton3

#Conditional Statements

def drink(money):
	if( money >= 2 ):
		return "You have got yourself a drink..!!"
	else:
		return "No drink for you"
		
print(drink(3))
print(drink(1))

def alcohol(age, money):
	if(age >= 21) and (money >= 5):
		return "You are getting a drink!"
	elif(age >= 21) and (money <= 5):
		return "Not sufficient money."
	elif(age < 21) and (money >= 5):
		return "You are underage kid."
	else:
		return "You are too young and have not enough money"
		
print(alcohol(22,2))
print(alcohol(20,1))


