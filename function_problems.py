# #PART 1 — OPERATOR BASED PRACTICAL QUESTIONS
# #1. Employee Salary Bonus Checker
# salary = 45000 
# bonus = 5000 
# #1.1
# def total_salary(salary,bonus):
#     print(salary + bonus)
# total_salary(45000,5000)
# #1.2 & #1.3
# def employee_slary_limit(salary):
#     if salary > 50000:
#         print("Higher Salary")
#     else:
#         print("Lower Salary")
# employee_slary_limit(salary)

# #2.Online Shopping Bill
# price = 2500 
# quantity = 3 
# delivery_charge = 100
# #2.1
# def total(price,quantity,delivery_charge):
#     print((price * quantity) + delivery_charge)
# total(price = 2500, quantity = 3, delivery_charge = 100)
# #2.2
# def bill(total):
#     total_bill = 7600
#     for i in range(1,4):
#       print(total_bill)
#     return total_bill
# bill(7600)
# #2.3
# def final_bill(total):
#     if total > 7000:
#         print("Higher Bill")
#     else:
#         print("Lower Bill")
# final_bill(7600)

# #3.Student Marks Evaluation
# python_marks = 78 
# sql_marks = 65 
# powerbi_marks = 82
# #3.1
# def average(python_marks,sql_marks,powerbi_marks):
#     print((python_marks + sql_marks + powerbi_marks)/ 3)
# average(python_marks = 78 , sql_marks = 65 , powerbi_marks = 82)
# #3.2
# def check_average(average):
#     if average > 70:
#         print("Pass")
#     else:
#         print("Fail")
# check_average(75)
# #3.3
# def sub(marks):
#     Subjects = {"python_marks = 78", 
#                 "sql_marks = 65",
#                 "powerbi_marks = 82"}
#     for i in range(1,2):
#         print(Subjects)
#     return Subjects
# sub(0)

# #PART 2 — LIST PRACTICAL QUESTIONS
# #1. Ecommerce Product List
# products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
# #1.1
# for product in products:
#     print(product)
# #1.2
# products.append("Printer")
# print("Updated list:", products)
# #1.3
# if "Mouse" in products:
#     products.remove("Mouse")
# print(products)
# #1.4
# def count_products(Product_list):
#     return len(Product_list)
# total = count_products(products)
# print(f"Total products in list {total}")
# #1.5
# def check_exist(prodcut_list,item_name):
#     return item_name in prodcut_list
# exists = check_exist(products,"Laptop")
# if exists:
#     print("Yes Laptop is existed in list")
# else:
#     print("No Laptop is not existed in list")

# #2.Student Attendance System 
# students = ["Anu", "Rahul", "Megha", "Arjun"]
# #2.1
# for student in students:
#     print(student)
# #2.2
# def total_student(student_list):
#     return len(student_list)
# total = total_student(students)
# print(f"Total students is {total}")
# #2.3
# def check_exist(students,stud_name):
#     return stud_name in students
# exists = check_exist(students,"Megha")
# if exists:
#     print("Megha is present")
# else:
#     print("Megha is not present")
# #2.4
# students.append("Diya")
# print("Update list:",students)

# #3. Movie Collection App 
# movies = ["Leo", "Jailer", "Vikram", "Master"] 
# #3.1
# for movie in movies:
#     print(movie)
# #3.2
# def index_list(movie_list):
#     return movie[0]
# movie = movies[0]
# print(f"The first movie is {movie} ")
# #3.3
# if "Master" in movies:
#     movies.remove("Master")
# print(movies)
# #3.4
# def check_exist(movie_list,movie_name):
#     return movie_name in movie_list
# exists = check_exist(movies,"Leo")
# if exists:
#     print("It exists")
# else:
#     print("Not exists")

# #PART 3 — TUPLE PRACTICAL QUESTIONS 
# #1. Employee ID Management 
# employee_ids = (101, 102, 103, 104) 
# #1.1
# for employee_id in employee_ids:
#     print(employee_id)
# #1.2
# def total_ids(employee_id):
#     return len(employee_id)
# total = total_ids(employee_ids)
# print(f"Total ids are {total}")
# #1.3
# def check_exist(employee_list,employees):
#     return employees in employee_list
# exists = check_exist(employee_ids,103)
# if exists:
#     print("IT is existed")
# else:
#     print("It is not existed")
# #1.4
# def index_list(employee_list):
#     return employee_ids[0],employee_ids[-1]
# emp1 = employee_ids[0] 
# emp2 = employee_ids[-1]
# print(f"The first ids is {emp1} and the last id is {emp2}")

# #2. IPL Team Names 
# teams = ("CSK", "MI", "RCB", "KKR") 
# #2.1
# for team in teams:
#     print(team)
# #2.2
# def exist(team_list,item_name):
#     return item_name in team_list
# check = exist(teams,"RCB")
# if check:
#     print("RCB is existed")
# else:
#     print("RCB is not existed")
# #2.3
# def idex(team_list):
#     return teams[0:4]
# team = teams[0:4]
# print(f"The teams are {team}")
# #2.4
# def count(team_list):
#     return len(team_list)
# total = count(teams)
# print(f"the tuple length is {total}")

#PART 4 — SET PRACTICAL QUESTIONS
#1. Python and Data Analytics Students
python_students = {"Rahul", "Megha", "Anu", "Arjun"} 
analytics_students = {"Anu", "David", "Rahul", "Diya"}
#1.1
print(python_students & analytics_students)
#1.2
print(python_students - analytics_students)
#1.3
for python in python_students:
    print(python_students)
#1.4
def unique_students(student_list):
 dict1 : dict
 dict2 : dict
unique_students = set(dict1.keys()) | set(dict2.keys)
total_unique = len(unique_students)
print(f"total unique students are {unique_students}")