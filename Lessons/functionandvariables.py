"""
#print("What's your name? ") we don't ask user to input sth in print function.
name = input("What's your name? ")

"""
'''
print("hello,", name) #with "," we can use multiple arguements

#which is better? + or , ? concanetting*

#but what if I put my name Ram? it will still print prasun
#for this we need to learn about "return values" & "variables"

#read documentation of python from bookmark in brave
#print(*objects, sep=' ', end='\n', file=None, flush=False)
#everything between paranthesis is arguments of functions but this is paramaeter
name = input("What's your name? ")

print("hello,", end=" ")
print(name)'

'''

#bugs is a mistake in a program.

"""
name = name.strip() #strip is a function that removes the whitespace from the beginning and end of the string
name = name.capitalize() #capitalize is a function that capitalizes the first letter of the string
name = name.title() #title is a function that capitalizes the first letter of each word in the string
name= name.casefold() #casefold is a function that converts the string to lowercase
name= name.center(10) #center is a function that centers the string in the middle of the specified width
name = name.count("z") #count is a function that counts the number of occurrences of a substring in a string

"""
"""
first, last = name.split(" ") #split is a function that splits the string into a list of words

print(f"Hello, {first}") #f is format str 

print(f"Hello, {name}")

"""

