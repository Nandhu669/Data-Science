# #function last problem
# #2. Social Media Analytics 
# followers = { 
# "instagram": 25000, 
# "youtube": 18000, 
# "linkedin": 12000 
# } 
# #2.1
# for follower in followers:
#     print(followers.keys())
# #2.2
# def counts(followers_list):
#     return len(followers_list)
# total = counts(followers)
# print(f"Total followers count is {total}")
# #2.3
# def counts(instagram,youtube,linkedin):
#     print(instagram + youtube + linkedin)
# counts(instagram = 25000, youtube = 18000, linkedin = 12000)
# #2.4
# def check_followers(follower_count):
#     return follower_count > 20000
# current_int = 25000
# print(check_followers(current_int))

# #factorial using funstion
# def factorial(num):
#     s = 1
#     for i in range(1,num+1):
#         s *= i
#     return s
# x = factorial(5)
# print("factorial:",x)

# #fibinocci using function
# def fibinocci(num):
#     a,b = 0,1
#     for i in range(num):
#         print(a,end =' ')
#         c = a + b
#         a = b
#         b = c
# x = fibinocci(6)

#armstrong or not using function
def armstrong(num):
    digits = str(num) #here we choose num as string
    num_digits = len(digits) #we check the length of digits
    total = sum(int(digit) ** num_digits for digit in digits) 
    #here we add each digit with the power of it total length , using for loop to get the each number
    return total == num #here we return check the total with the number
num = 153
if armstrong(num):
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
    