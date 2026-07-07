#matching statement

# point = (15, 25, 43)
# match point:
#     case (0, 0 , 0):
#         print("orgin")
#     case (x, 0, 0):
#         print(f"x={x} on x-axis")
#     case (0, y, 0):
#         print(f"y={y} on y-axis")
#     case (0, 0, z):
#         print(f"z={z} on z-axis")
#     case (x, y, z):
#         print(f"x={x}, y={y}, z={z} on 3D")

# #1. Day classifier
# day = int(input("Enter a day number (1-7): "))
# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday") 
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
#     case _:
#         print("Invalid day number. Please enter a number between 1 and 7.")

# #2.Simple calculator using match case
# a = int(input("Enter your first number: "))
# b = int(input("Enter your second number: "))
# operator = input("Enter your operator (+,-,*,/): ")
# match operator:
#     case "+":
#         print(f"{a} + {b} = {a + b}")
#     case "-":
#         print(f"{a} - {b} = {a - b}")
#     case "*":
#         print(f"{a} * {b} = {a * b}")
#     case "/":
#         if b != 0:
#             print(f"{a} / {b} = {a / b}")
#         else:
#             print("Error: Division by zero is not allowed.")
#     case _:
#         print("Incorrect operator.")

# #3. Grade checker
# x = int(input("Enter your marks: "))
# match x:
#     case x if x >= 90:
#         print("A Grade")
#     case x if x >= 80:
#         print("B Grade")
#     case x if x >= 70:
#         print("C Grade")
#     case x if x >= 60:
#         print("D Grade")
#     case _:
#         print("You need to work hard to get a better grade")

# #4. HTTP status error
# x = int(input("ENTER CODE: "))
# match x:
#     case 200:
#         print("OK")
#     case 404:
#         print("Not Found")
#     case x if x >= 500 and x < 600:
#         print("Server Error")
 
# #5. Chess Board
# row = int(input("Enter the row:"))
# col = int(input("Enter the column:"))
# match (row, col):
#     case (row, col) if (row + col) % 2 == 0:
#         print("The square is black")
#     case (row, col) if (row + col) % 2 != 0:
#         print("The square is white")

# #6.Command parser input and checking
# cmd = ["add" , 5, 3]
# match cmd:
#     case ["add", int(a) | float(a) , int(b) | float(b)]:
#         result = a + b
#         print(f"Result: {result}")
#     case ["quit"]:
#         print("Exiting Program....")
#         pass
#     case _:
#         print("Invalid command...")

# #7.File Type checker
# file = input('Enter your file name: ')
# file_parts = file.split('.')
# match file_parts:
#     case [name , "jpg" | "png"]:
#         print("It is an image file")
#     case [name , "py"]:
#         print("It is python file")
#     case _:
#         print("Invalid File..")

# #8.Shape area calculator
# calc = input("Enter your shape and dimensions ('rectangle, 5, 4') or ('circle, 7') like this : ")
# parts = [item.strip() for item in calc.split(',')]
# match parts:
#     case ["rectangle" , w_str, h_str]:
#         w = float(w_str)
#         h = float(h_str)
#         area = w * h
#         print(f"Your area of rectangle is {area}")
#     case ["circle" , r_str]:
#         r = float(r_str)
#         area = 3.14159 * (r**2)
#         print(f"Your area of circle is {area:.2f}")
#     case _:
#         print("Invalid shape and dimension")

