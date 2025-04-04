#str.capitalize() - Returns a copy of the string with its first character capitalized and the rest lowercased.
a = "hello atol"
b = a.capitalize()
print(f"Original: '{a}', Capitalized: '{b}'") #f=formatted string literal and instead of using str.format() or % you can place vairables or expression inside curly braces {} within the string.

#str.casefold() - Returns a copy of the string with its first character capitalized and the rest lowercased.
c = input("Enter your name in block letters: ")
d = " ".join(c.split()).casefold() # Updated line: removes all extra spaces and casefolds
print(f"Original: '{c}', Casefolded: '{d}'") #f=formatted
