# #conversion from list to tuple
# x = [1,5,4,3,2,6]
# y = tuple(x)      #converting to tuple
# print(y)
# print(len(y))     #finding length
# print(y[1])       #indexing
# print(type(y))    #class type
# print(y[2:4])     #slicing
# print(y[-1])      #negative indexing
# print(3 in y)     #checking membership
# print(y.count(3)) #counting
# y += (7,8)        #concatination
# print(y)
# print(y * 3)      #repetition
# #way to set a single element to tuple using conversion
# x = [3]
# y = tuple(x)
# print(type(y))
# #way to set a single element to tuple by including ',' in paranthesis
# x = (3,)
# print(type(x))

# #tuple 
# t = (1,2.5,[5,7.6,'Hello'],10)
# t[2][2] = "Hai"
# print(t)
# t[2].append(45)
# t[2].pop(3)
# t[2].insert(1,6.5)
# print(t)
# a,b,c,d = t
# print(a)
# print(type(a))
# print(b)
# print(type(b))
# print(c)
# print(type(c))
# print(d)
# print(type(d))

#using list comprehension to check prime or not
a = int(input("enter the number:"))
div = [1 for i in range(2, a-1) if a % i == 0]
is_prime = a > 1 and sum(div) == 0
print(f"{a} is prime: {is_prime}")