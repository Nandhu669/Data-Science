# #list indexing reverse
# a = [2,3,5,6,7]
# print(a[::-1])
# print(type(a))

# #list indexing slicing
# a = [4,4,55,55,54,54,5,4,3,3,]
# print(a[3:6])

# #list index negative 
# a = ['hari',22,'kollam','kerela']
# print(a[-2])
# print(len(a)) #length of list

# #list reverse with looping
# a = [1,2,3,4,5]
# for i in range(len(a)-1,-1,-1):
#     print(a[i])

# #list adding 
# a = [1,2,3,4,5]
# a.append(6)       #used to add a single element to the end of the list
# print(a)
# a.extend([7,8,9]) #used to add multiple elements to the end of the list
# print(a)
# a.insert(2,63)    #used to add a single element at a specific index in the list
# print(a)
# a[3] = 100        #used to replace an element at a specific index in the list
# print(a)
# a.remove(2)       #used to remove the first occurrence of a specific element from the list
# print(a)


# #TODAY'S PROBLEM
# #1. List adding 
# x = [21,1,7,9,13,50]
# x.append(45)                         #add 45 at end
# print(x)
# x.extend([100,125,9])                #add 100,125,9 in end
# print(x)
# x.insert(-4,47)                      #add 47 at position -4
# print(x)
# x[3]=x[-1] = 0                       #to replace 9 with 0
# print(x) 
# print(x[:2] + x[-2:])                #new list using first and last 2 items
# #other way to replace 9 with for loop
# for i in x:
#     if i == 9:
#         a = x.index(9)
#         x[a] = 0 
# print(x)

# #list with poping , deleting and clearing
# a = [1,4,5,3,2,4,5,3]
# print(a.pop())        #removes last item
# print(a.pop(2))       #removes item at index 2
# print(a.index(4))     #returns index or positiom of first occurrence of 4
# print(a.count(4))     #returns count of 4 in the list
# print(5 in a)         #returns True if 5 is in the list, False otherwise
# del a[1]              #removes item at index 1
# print(a)
# a.clear()             #removes all items from the list
# print(a)

# #sorting using while loop
# a = [21,1,7,9,13,50]
# n = len(a)                                       #used to assing the length of the list to a variable n
# for i in range(n):                               #used to iterate through the list from index 0 to n
#     for j in range(0, n-1, 1):                   #used to iterate through the list from index 0 to n-1
#         if a[j] < a[j+1]:                        #here we use '>' for ascending and '<' for descending orders
#             a[j] , a[j+1] = a[j+1] , a[j]        #this will swap the numbers based on the above condition
# print("Sorted:",a)

