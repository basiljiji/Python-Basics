#!/bin/python3

#Functions

def mySelf(): #this is a function
	name = "Basil"
	age = 22
	print("My name is " + name + " and Iam " + str(age) + " years old")
	
mySelf()

#adding parameters
def addHundred(num):
	print(num + 100)
	
addHundred(10)

#multiple parameters
def add(x,y):
	print(x + y)
	
add(8,2)

def multiply(a,b):
	return a * b

print(multiply(12, 12))

def squareRoot(x):
	print(x ** .5)
	
squareRoot(64)

def nl():
	print('\n')
	
nl()
