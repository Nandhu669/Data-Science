#1.to print company name in upper,lower and title
company_name = "TechNova Solutions"
print(company_name.upper())
print(company_name.lower())
print(company_name.title())

#2.Find the total number of characters in employee name.
employee_name = "Arjun Menon"
total_char = len(employee_name)
print("Total Characters:",total_char)

#3.Replace "Analytics" with "Science" in department. 
department = "Data Analytics" 
new_department = department.replace("Analytics", "Science")
print(new_department)

#4.Extract:  first name  last name using slicing.
employee_name = "Arjun Menon" 
print("First_name:",employee_name[0:5])
print("Second_name:",employee_name[6:11])

#5.Print first 5 characters from employee ID. 
employee_id = "TNX2026"
print(employee_id[0:5])

#6.Check whether "Nova" exists in company name using membership operator. 
company_name = "TechNova Solutions" 
print('Nova' in company_name)

#7.Create a professional message: "Employee Arjun Menon works in Data Analytics department." using concatenation. 
a = 'Employee Arjun Menon works'
b = ' in Data Analytics department'
print(a+b)

#8.Print email without domain name. Expected: arjun.menon 
email = "arjun.menon@technova.com"
print(email[0:11])

#9. Print: first skill,last skill 
skills = ["Python", "SQL", "Excel", "Power BI", "Tableau"] 
print(skills[0],skills[-1])
#10. Add "Machine Learning" to skills list.
skills.append('Machine Learning')
print(skills)
#11. Insert "Statistics" at 2nd position.
skills.insert(2,'Statistics')
print(skills)
#12. Remove "Excel" from list.
skills.remove('Excel')
print(skills)
#13.Sort skills alphabetically.
skills.sort()
print(skills)
#14.Reverse the skills list.
skills.reverse()
print("Reverse:",skills)
#15.Find total number of skills. 
print(len(skills))
#16.Create another list: tools = ["Git", "Jupyter Notebook"] Merge it with skills list.
tools = ["Git", "Jupyter Notebook"]
print(skills + tools)
#17. Check whether "SQL" exists in skills list.
print("SQL" in skills)
#18.Print skills from index 1 to 4 using slicing.
print(skills[1:5])

#19. Print all project details. 
project_details = ("Customer Churn Analysis", "Completed", "Power BI Dashboard")
print(project_details)
#20.Print project status only.
print("project status:",project_details[1])
#21.Find total number of elements in project_details tuple.
print(len(project_details))
#22.Check whether "Completed" exists in tuple.
print("Completed" in project_details)
#23.Create another tuple: project_manager = ("Rahul",) Combine both tuples.
project_manager = ("Rahul",)
b = project_details + project_manager
print(b)
#24.Calculate: total_salary = monthly_salary + bonus 
monthly_salary = 45000 
bonus = 5000
working_days = 26
absent_days = 2
total_salary = monthly_salary + bonus
print(total_salary)
#25.Calculate salary per working day
salary = monthly_salary / 30
print("Salary per day is: ",salary)
#26.Calculate salary deduction for absent days. Formula: (monthly_salary / working_days) * absent_days 
Deduction = (monthly_salary / working_days) * absent_days
print("Salary deduction for absent days is: ",Deduction)
#27. Use assignment operator: Increase salary by 3000. 
monthly_salary += 3000
total_salary += 3000
print(monthly_salary)
#28.Check: monthly_salary > bonus 
if monthly_salary > bonus:
    print('True')
else:
    print('False')
#29.Check identity operator: skills is tools
print(skills is tools)
#30.Check logical operator: monthly_salary > 40000 and bonus > 3000
if monthly_salary > 40000 and bonus > 3000:
    print('True')
else:
    print('False')
#Final Task
print("Employee Summary")
print("----------------")
print(f'Company: ',company_name)
print(f'Employees Name: ',employee_name)
print(f'Department: ',department)
print(f'Skills: ',skills)
print(f'Project: ',project_details)
print(f'Total Slary: ',total_salary)