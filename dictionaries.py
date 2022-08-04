#!/bin/python3

#Dictionaries {key:value pairs}

drinks = {"Jack Daniels" : 10, "Old monk" : 5, "MC" : 3 } #Drink is key, Price is value
print(drinks)

employees = {"Finance" : ["John", "Zgod","Neyo"], "IT" : ["Clutch", "Shadow", "Ninja"], "HR" : ["Aditya", "Evoo", "Goblin"]}
print(employees)

employees['Legal'] = ["Psycho","Akshat", "Hector"] #add new key:value pair
print(employees)

employees.update({"Sales":["Omega","Joker"]}) #add new key:value pair
print(employees)
drinks["Jack Daniels"] = ["12"]
print(drinks)

print(drinks.get("Jack Daniels")) #retrieve a particular value


