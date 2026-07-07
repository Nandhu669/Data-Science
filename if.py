# # Problems
# #1. TO check (+,-,0)
# a = int(input('Enter your Number:'))
# if a > 0 :
#     print("a is a positive number")
# elif a < 0 :
#     print("a is negative number")
# else :
#     print("Your number is 0")

# #2. check number is even or odd
# a = int(input("enter your number:"))
# if a % 2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd")

# #3.Determin if user is elgible (Age>= 18)
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("Your are elgible to vote")
# else:
#     print("you are unelgible to vote")

# #4. program to say cold or warm
# temp = int(input("Enter your tenperature: "))
# if temp < 20:
#     print("It is Cold🥶")
# elif temp >= 20 and temp <= 30:
#     print("It is Warm😇")
# elif temp>30 :
#     print("It is Hot🥵")
# else:
#     print("Error")

# #5.check a year is leap year
# year =int(input("Enter a year: "))
# if(year % 4 ==0 and year % 100 != 0 or year % 400 == 0):
#     print("it is a leap year")
# else:
#     print("it is not a leap year")

# #6. GRADING
# mark = int(input("Enter your marks"))
# if mark >= 90
#  print("You are awarded A")
# elif mark >=80 and mark <= 89:
#    print("You are awarded B")
# elif mark >=70 and mark <= 79:
#    print("You are awarded C")
# elif mark >=60 and mark <= 69:
#    print("You are Awarded D")
# elif mark < 60:
#    print("You are awarded F")
# else:
#    print("You are Failed")

# #7.Checking even and positive
# num = int(input("Enter a number: "))

# if num > 0 and num % 2 == 0 :
#  print("Your number is positive and even")
# else:
#  print("Your number is not positive and not even")

# #8.Checking larger number

# num1 = int(input("Enter YOur First number: "))
# num2 = int(input("Enter your second number: "))
# num3 = int(input("Enter your Third number: "))

# if num1 > num2 and num1 > num3 :
#     print("The first number is Larger")
# elif num2 > num3 :                         #this function getting printed when the first one is true
#     print("The second number is large")
# else :
#     print("The third number is larger")

# #9.Bill Calculating

# Purchase_amount = float(input("Enter your purchase amount : "))

# if Purchase_amount > 5000 :
#     discount_percentage = 20
# elif Purchase_amount >= 2000 and Purchase_amount <= 5000 :
#     discount_percentage = 10
# else :
#     discount_percentage = 0

# discount_amount = (discount_percentage / 100 ) * Purchase_amount
# final_bill = Purchase_amount - discount_amount

# print(f"\n--- Bill Summary ---")
# #.2f used to match real-world standard currency formats
# print(f"Original Amount : ₹{Purchase_amount:.2f}")
# print(f"Discount Rate   : {discount_percentage}%")
# print(f"Discount Saved  : ₹{discount_amount:.2f}")
# print(f"Final Bill Paid : ₹{final_bill:.2f}")

# #10.Day and it dates of (1-7)

# day = int(input("Enter a day number (1-7): "))

# if day == 1:
#     print("It is MonDay baby!!! ")
# elif day == 2:
#     print("It's Tuesday bro!!")
# elif day == 3:
#     print("It is Wednesday Yay!!!")
# elif day == 4:
#     print("It is Thursday Suiiii")
# elif day == 5:
#     print("It is Friday frooo!!!")
# elif day == 6:
#     print("it is Saturday wow !!!")
# elif day == 7:
#     print("It is Sunday burn (-_-)")
# else :
#     print("Yo bro put it your freaking number -__- ")