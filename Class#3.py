#LIST
a = [23,'Anjan',35.7]
print(type(a))

#TUPLE AND INDEX POSITION
a = (23,'Anjan',35.7,"America")
print(type(a))
print(a[2])

#STRING AND INDEX POSITION
x="hello world"
print(x[-4])

#RANGE AND TYPE
#range(start,stop,step)
a= range(1,10,2)
print(type(a))
for i in range(1,10,2):
    print(i)

#mapping type with dictionary and key value pair
a = {'name':'Anjan','age':23,'country':'America'}
print(a['age'])

#set and type 
#note: it can vary each time you run the code because it is unordered
a = {23,'Anjan',35.7}
print(type(a))
print(a)

#boolean type
#note: boolean type are True and False
a = True
print(type(a))
print(a)

#none type
#note: None type is used to represent the absence of a value or a null value
a = None
print(type(a))
print(a)

#complex type
#note: complex numbers are represented in the form of a + bj, where a is the real part and b is the imaginary part
#note: conjugate of a complex number is obtained by changing the sign of the imaginary part
a = 3 + 4j
print(type(a))
print(a.real)
print(a.imag)
print(a.conjugate())

#frozenset type
#note: frozenset is an immutable version of set, which means that once a
a = frozenset([1, 2, 3])
print(type(a))
print(a)

#multiline string
#note: multiline string can be created using triple quotes (''' or """)
s = """Hello, 
my name is Anjan. 
I am 23 years old and I live in America."""
print(s)

#slicing
#note: slicing is used to extract a portion of a sequence (string, list, tuple
a = "Hello Python "
print(a[0:7])

#negative indexing
#note: negative indexing is used to access the elements of a sequence from the end
a = "Hello Python "
print(a[-7:-1])

#reverse slicing
a = "Hello Python "
print(a[::-1])
print(a[::1])

#concatenation
#note: concatenation is used to combine two or more strings
a = "Hello "
b = "Python"
print(a + b)

#repetition
#note: repetition is used to repeat a string a specified number of times
a = "Hello "
print(a * 3)

#membership operator
#note: membership operator is used to check if a value is present in a sequence
a = "Hello Python"
print('Python' in a)
print('Java' in a)

#Length
#note: to check length of varialbe or a string
a = "Hello Python"
print(len(a))

#uppercase
a = input("Enter a string: ")
python = a.upper()
print(python)

#lowercase
a = input("Enter a string: ")
python = a.lower()
print(python)

#swapcase
a = input("Enter a string: ")
python = a.swapcase()
print(python)