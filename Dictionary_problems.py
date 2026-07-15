# #PART 1 — OPERATOR BASED PRACTICAL QUESTIONS
# #1.Employee Salary Calculation
# e ={"basic_salary":35000,"bonus":5000,"tax" :2000}
# #1.1
# total_salary = e['basic_salary'] + e['bonus']
# print(total_salary) 
# #1.2
# final_salary = total_salary - e['tax']
# print(final_salary)
# #1.3
# yearly_salary = final_salary * 12
# print(yearly_salary)
# #1.4
# salary = yearly_salary // 12
# print(salary)

# #2.Mobile shop Discount System
# a = {"mobile_price":45000,"discount":5000,"gst":2000}
# #2.1
# discount_price = a['mobile_price'] - a["discount"]
# print(discount_price)
# #2.2
# final_amount = discount_price + a["gst"]
# print(final_amount)
# #2.3
# half = final_amount // 2
# print(half)
# #2.4
# reminder = final_amount % 3
# print(reminder)

# #3.Student Exam Marks Analysis 
# python_marks = 85 
# sql_marks = 78 
# powerbi_marks = 90 
# #3.1
# total_marks = python_marks + sql_marks + powerbi_marks
# print(total_marks)
# #3.2
# average_marks = total_marks / 3
# print(average_marks)
# #3.3
# if python_marks > sql_marks:
#     print("python_marks is greater")
# else:
#     print("sql_marks is greater")
# #3.4
# if powerbi_marks == python_marks:
#     print("Both are equal")
# else:
#     print("Not equal")

# #4.Ecommerce Order Billing 
# product_price = 1200 
# quantity = 4 
# delivery_charge = 150
# #4.1
# total = product_price * quantity
# print(total)
# #4.2
# total_bill = total + delivery_charge
# print(total_bill)
# #4.3
# if total_bill > 5000:
#     print("total_bill is greater")
# else:
#     print("Less than 5000")
# #4.4
# square = quantity ** 2
# print(square)

# #5.Data Usage Monitoring 
# daily_usage = 2.5 
# days = 30 
# #5.1
# monthly_usage = daily_usage * days
# print(monthly_usage)
# #5.2
# conversion = monthly_usage * 1024
# print(f"converted in Mb is {conversion}MB")
# gb_conversion = conversion // 1024
# print(f"Converted to GB : {gb_conversion}GB")
# #5.3
# if gb_conversion > 50:
#     print("It is Greater")
# else:
#     print("It is smaller")
# #5.4
# gb_conversion += 10
# print(gb_conversion)

# #6.Bank Account Transactions
# balance = 50000 
# deposit = 12000 
# withdraw = 7000 
# #6.1
# total = balance + deposit
# print(total)
# #6.2
# withdrawn = total - withdraw
# print(withdrawn)
# #6.3
# double = withdrawn * 2
# print(double)
# #6.4
# if double < 100000:
#     print("Total is less than 100000")
# else:
#     print("Total is greater than 100000")

# # 7.Laptop EMI Calculation 
# laptop_price = 80000 
# months = 10 
# #7.1
# emi = laptop_price / months
# print(emi)
# #7.2
# reminder = emi % 7
# print(reminder)
# #7.3
# if emi > 5000:
#     print("Emi is greater")
# else:
#     print("Emi is smaller")
# #7.4
# emi += 500
# print(emi)

# #8.Social Media Followers Analysis
# instagram = 25000 
# youtube = 18000 
# linkedin = 12000
# #8.1
# total_followers = instagram + youtube + linkedin
# print(total_followers)
# #8.2
# difference = instagram - linkedin
# print(difference)
# #8.3
# if youtube == linkedin:
#     print("Both are Equal")
# else:
#     print("Both are not Equal")
# #8.4
# total_followers *= 2
# print(total_followers)

# #PART 2 — DICTIONARY OPERATIONS PRACTICAL QUESTIONS
# #1.Student Profile Management 
# student = { 
# "name": "Rahul", 
# "course": "Data Science", 
# "marks": 88, 
# "city": "Bangalore" 
# } 
# #1.1
# print(student.get("name"))
# #1.2
# print(student.get("course"))
# #1.3
# student.update({"marks": 95})
# print(student)
# #1.4
# student["email"] = "1232@gmail.com"
# print(student)
# #1.5
# del student["city"]
# print(student)
# #1.6
# print(student.keys())

# #2.Employee Information System
# employee = { 
# "id": 101, 
# "name": "Anjali", 
# "department": "HR", 
# "salary": 45000 
# } 
# #1.1
# print(employee.get("salary"))
# #1.2
# employee.update({"salary": 45000 + 5000})
# print(employee)
# #1.3
# employee["location"] = "kochi"
# print(employee)
# #1.4
# del employee["department"]
# print(employee)
# #1.5
# print(employee.keys())

# #3.Mobile Product Details 
# mobile = { 
# "brand": "Samsung", 
# "model": "S24", 
# "price": 75000, 
# "storage": "256GB" 
# }
# #3.1
# print(mobile.get("model"))
# #3.2
# mobile.update({"price": 70000})
# print(mobile)
# #3.3
# mobile["color"] = "Black"
# print(mobile)
# #3.4
# del mobile["storage"]
# print(mobile)
# #3.5
# print(mobile)

# #4.Movie Information Database
# movie = { 
# "title": "Leo", 
# "hero": "Vijay", 
# "rating": 8.5, 
# "language": "Tamil" 
# } 
# #4.1
# print(movie.get("title"))
# #4.2
# movie.update({"rating":9.1})
# print(movie)
# #4.3
# movie["director"] = "Lokesh"
# print(movie)
# #4.4
# del movie["language"]
# print(movie)
# #4.5
# print(movie.items())

# #5.Online Food Order Details
# order = { 
# "item": "Burger", 
# "quantity": 2, 
# "price": 250, 
# "status": "Preparing" 
# }
# #5.1
# print(order.get("item"))
# #5.2
# total = order.get("quantity") * order.get("price")
# print(total)
# #5.3
# order.update({"status":"Delivered"})
# print(order)
# #5.4
# order["payment"] = "Online"
# print(order)
# #5.5
# del order["quantity"]
# print(order)

# #6.Laptop Store Inventory
# laptop = { 
# "brand": "Dell", 
# "ram": "16GB", 
# "price": 65000, 
# "processor": "i7" 
# } 
# #6.1
# print(laptop.get("ram"))
# #6.2
# laptop.update({"processor":"i9"})
# print(laptop)
# #6.3
# laptop["warranty"] = "2 years"
# print(laptop)
# #6.4
# del laptop["price"]
# print(laptop)
# #6.5
# print(laptop.keys(),laptop.items())

# #7.Hospital Patient Record
# patient = { 
# "name": "Arjun", 
# "age": 32, 
# "blood_group": "O+", 
# "room": 205 
# }
# #7.1
# print(patient.get("name"))
# #7.2
# patient.update({"room":206})
# print(patient)
# #7.3
# patient["docotor"] = "Dr.Meera"
# print(patient)
# #7.4
# del patient["age"]
# print(patient)
# #7.5
# print(patient)

# #8.Amazon Product Tracking 
# product = { 
# "product_name": "Headphones", 
# "price": 2999, 
# "rating": 4.4, 
# "stock": 50 
# } 
# #8.1
# print(product.get("price"))
# #8.2
# product.update({"stock": 40})
# print(product)
# #8.3
# product["brand"] = "Sony"
# print(product)
# #8.4
# del product["rating"]
# print(product)
# #8.5
# print(product.keys(),product.items())

# #PART 3 — MIXED OPERATORS + DICTIONARY PRACTICE
# #1.Employee Bonus System
# employee = { 
# "name": "Akhil", 
# "salary": 50000, 
# "bonus": 10000 
# } 
# #1.1
# total = employee.get("salary") + employee.get("bonus")
# print(f"total salary after bonus {total}")
# #1.2
# employee["department"] = "AI Team"
# print(employee)
# #1.3
# employee.update({"salary": 50000 + 5000})
# print(employee)
# total = employee.get("salary") + employee.get("bonus")
# #1.4
# if total > 60000:
#     print("salary is greater")
# else:
#     print("salry is lower or equal")

# #2.Shopping Cart System
# cart = { 
# "item": "Keyboard", 
# "price": 1500, 
# "quantity": 3 
# } 
# #2.1
# total = cart.get("price") * cart.get("quantity")
# print(total)
# #2.2
# cart["delivery"] = 100
# print(cart)
# #2.3
# final_bill = total + cart.get("delivery")
# print(final_bill)
# #2.4
# if final_bill > 5000:
#     print("it is greater")
# else:
#     print("it is lower")

# #3. Student Course Fee Management
# student = { 
# "name": "Diya", 
# "course_fee": 45000, 
# "paid": 20000 
# } 
# #3.1
# remaining = student.get("course_fee") - student.get("paid")
# print(remaining)
# #3.2
# student["course"] = "Python Full Stack"
# print(student)
# #3.3
# student.update({"paid": 30000})
# print(student)
# #3.4
# if student.get("paid") == student.get("course_fee"):
#     print("PAID")
# else:
#     print("not fully paid")