# #Sorting & Reversing
# a = [21,1,7,9,13,50]
# a.sort()                         #sorts the list in ascending order
# print("Sorted:",a)
# a.sort(reverse=True)             #sorts the list in descending order
# print("Sorted in Reverse:",a)
# a.reverse()                      #sorts the list in reverse order
# print("reversed:",a)
# sorted(a)                        #returns a new sorted list without modifying the original list
# print("Sorted:",sorted(a))

# #copy & other 
# a = [21,1,7,9,13,50]
# b = a.copy()                       #creates a copy of the list
# print("Copied:",b)
# #list 
# list=("Hello","World")             #creates a list from a tuple
# print("List:",list)
# #repetition
# b = a * 2
# print("Repetition:",b)

# #list comprehension
# copy = [a**2 for a in range(5)]        #creates a new list with the square of each number in the range of 0 to 4
# print("Comprehension:",copy)
# #dictionary comprehension
# dict = {a:a**2 for a in range(5)}       #creates a new dictionary with the square of each number in the range of 0 to 4
# print("Dictionary Comprehension:",dict)
# #set comprehension
# set = {a**2 for a in range(5)}          #creates a new set with the square of each number in the range of 0 to 4
# print("Set Comprehension:",set)
# #factorial in comprehension version 1
# a = [1,2,3,4,5]
# factorial = [1]
# for i in a:
#     factorial.append(factorial[-1]*i)      #creates a new list with the factorial of each number in the list a
#     print("Factorial:",factorial[1:])

# #factorial in comprehension version 2
# a = int(input("Enter a number: "))
# b = 1
# fact = [b:=b*i for i in range(1,a+1)][-1] #:= -- Walrus operator, assigns the value of b*i to b and returns the value of b for getting the last item we use -1
# print(fact)

# #fibinocci in comprehension
# n = int(input("Enter a number: "))
# a,b = 0,1
# fib = [a] + [a:= (b:=a+b)-a for i in range(n-1)]
# print(fib)

# #filtering in comprehension
# x = [21,9,7,47,51]
# mult = [i for i in x if i % 3 == 0]
# print(mult)

# #To find first character and last character of the items in the list eg: 'ae,oe,ge'
# x = ['appple','orange','grape']
# box = [f"{item[0]},{item[-1]}" for item in x]
# print(box)

#Task - change number into string->Above 10:Big Below 10:samll
x = [34,42,12,6,86,6,3,5,3]
result = ["Big" if num > 10 else "small" for num in x]
print(result)
