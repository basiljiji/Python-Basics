#!/bin/python3

#Lists - Have brackets []

movies = ["Vikram", "Master", "KGF", "Kaithi"]

print(movies[0]) #list starts from 0

print(movies[1:3]) #end value is exclusive

print(movies[1:]) #print everything after 1

print(movies[:1]) #print everything before 1

print(movies[-1]) #to grab last item

print(len(movies)) #to find length

movies.append("Thallumala") #to append at the end of the list
print(movies)

movies.pop() #deletes the last item
print(movies)

movies.pop(0) #deletes the first item
print(movies)
