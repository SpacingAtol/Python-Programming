# part A 
print("Hello") #1

user = input("Enter your name: ") #2
print("Welcome", user)

in1 = input("Enter the animal name:") #3
in2 = input("Enter another animal name:")
print(in1, in2)

# part B 

#This is the comment 

#1
num = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
print(f"Addition: {num + num2}")
#2
sub = num - num2
mult = num * num2
div = num / num2
rem = num / num2
print(f"Subtraction: {sub} \n Multiplication: {mult} \n Division: {div} \n Remainder: {rem} \n")

#3
temp = num
num = num2
num2 = temp
print(f"First number: {num}  \n Second number: {num2}")

#4
sub1 = int(input("Enter the marks of Science:"))
sub2 = int(input("Enter the marks of Maths:"))
sub3 = int(input("Enter the marks of Computer:"))
sub4 = int(input("Enter the marks of Social:"))
sub5 = int(input("Enter the marks of English:"))
total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (total)/500 * 100
print("Total Marks:", total)
print("Percentage:", percentage, "/b%")

#5 
basic = float(input("Enter the Basic Salary: "))
grade_pay = 2 * basic
da = 0.70 * basic
ta = 200 
hra = 0.20 * basic
salary = grade_pay + da + ta + hra
print("Grade Pay:", grade_pay)
print("DA:", da)
print("TA:", ta)
print("HRA:", hra)
print("Total Salary:", salary)



# a = a + b
# b = a - b
# a = a - b

