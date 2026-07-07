Mark = 24.6
mark= 12
favfruit="apple"
print(type(favfruit))
print(type(mark))
print(type(Mark))

#boolean type output
a= True
print(a)
print(type(a))

# string type output
a = input("Enter your Name: ")
print(a)
print(type(a))

# int type output
a =int(input("Enter your Mark: "))
print(type(a))

# float type output
a =float(input("Enter your Mark: "))
print(type(a))

# multipile Assignment
a,b,c = 1,2.5,"hello"
print(a,b,c)

# same value to multiple variables
a=b=c=10
print(a,b,c)

# operation
# 1 Addition
print("Addition")
a = int(input("Enter your Num1: "))
b = int(input("Enter your Num2: "))
print(a+b)

#2 subtraction
print("subtraction")
a = int(input("Enter your Num1: "))
b = int(input("Enter your Num2: "))
print(a-b)

#3 division
print("division")
a = float(input("Enter your Num1: "))
b = float(input("Enter your Num2: "))
print(a/b)

#4 multiplication
print("multiplication")
a = int(input("Enter your Num1: "))
b = int(input("Enter your Num2: "))
print(a*b)

#5 Exponention
print("Exponention")
a = int(input("Enter your Num1: "))
b = int(input("Enter your Num2: "))
print(a**b)

#6 floor division
print("Floor Division")
a = int(input("Enter your Num1: "))
b = int(input("Enter your Num2: "))
print(a//b)

#7 modulus remainder
print("Modulus Remainder")
a = int(input("Enter your Num1: "))
b = int(input("Enter your Num2: "))
print(a%b)

#print variable with sep and end
print("MY","name","is","nandhu",sep="/",end="END\n")
print("Stack flow")

#deleting variable
a = "mani"
del a
print(a)

#swaping of two numbers
a = int(input("Enter your Num1: "))
b = int(input("Enter your Num2: "))
a,b = b,a
print("After swaping: ",a,b)

