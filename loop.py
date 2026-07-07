#Problems
# #1.Print numbers from 1 to 10 using a for loop
# for i in range(1,11):
#  print(i)

# #2.Print the multiplication table of a given number.
# num = int(input("Enter a number: "))
# for i in range(1,11):
#     print(f"{num} x {i} = {num * i}")

# #3.Find the sum of all numbers from 1 to n
# num = int(input("Enter your last number :"))
# totalsum = 0
# for i in range(1, num+1):
#     totalsum += i
# print(f"The sum of 1 to {num} is {totalsum}")

# #4.Print the first n Fibonacci numbers.
# num = int(input("Enter a number: "))
# a,b = 0,1
# for i in range (num) :
#     print(a)
#     c = a + b
#     a = b
#     b = c

# #5. Print a * pattern like:   
# # *
# # **
# # *
# # **
# Level = 9
# for i in range(1,Level + 1):
#     if i % 2 != 0:
#         print("*")
#     else :
#         print("**")

# #6. Reverse a string using a loop.
# a = input("Enter a String: ")
# reverse = ""
# for i in a:
#     reverse = i + reverse
# print(f"the reversed string is : {reverse}")

# #7.Print all even numbers from 1 to 50
# for i in range(1,51):
#  if i % 2 == 0:
#   print(i)

# #8.Print numbers from n to 1 using a while loop
# n = int(input("Enter your Number: "))
# while n >= 1 :
#     print(n)
#     n -= 1

# #9.Find the factorial of a number using a while loop
# n = int(input("Enter a number: "))
# factorial = 1
# current = n
# while current > 1:
#     factorial *= current
#     current -= 1
# print (f"Factorial of {n} is : {factorial}")

# #10.Print all digits of a number separately using while loop
# n = int(input("Enter a number: "))
# a = n
# while a > 0:
#     digit = a % 10 #get the last digit
#     print(digit)
#     a //= 10      #remove the last digit

# #11.Count the number of digits in a given number
# n = int(input("Enter a number: "))
# count = 0
# if n == 0:
#     count = 1
# while n > 0:
#     n //= 10
#     count += 1
# print(f"The number of digits in the given number is: {count}")

# #12. Keep taking user input until they enter "exit".

# while True:
#     user = input("Enter a string : ")
#     if user == "exit":
#         break
#     print(f"You entered: {user}")

# #13.Use break to stop the loop when a number is found in a list
# num = int(input("Enter a number to search in the list: "))
# numbers = [1, 3, 5, 7, 9, 11]
# for i in numbers:
#     if i == num:
#         print(f"{num} found in the list.")
#         break

# #14 Use continue to skip printing even numbers from 1 to 20.
# for i in range(1, 21):
#     if i % 2 == 0:
#         continue
#     print(i)

# #15.Use pass inside a loop without affecting its flow
# n = int(input("Enter a number: "))
# for i in range(1, n + 1):
#     if i % 2 == 0:
#         pass  
#     else:
#         print(i)