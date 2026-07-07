#find
#note: in find if the value is not on the string it will give -1
a = "Hyndal"
print(a.find("y"))

#index
#note: in index if the value is not on the string it will give value error
a = "Hyndal"
print(a.index("y"))

#reverse find
#note: in rfind it will return the highest index of the substring if found in the string. If not found, it will return -1.
a = "Hylndal"
print(a.rfind("l"))

#reverse index
#note: in rindex it will return the highest index of the substring if found in the string. If not found, it will return value error.
a = "Hylndal"
print(a.rindex("l"))

#count
#note: count is used to count the number of occurrences of a substring in a string
a = "Hyllndal"
print(a.count("l"))

#startswith
#note: startswith is used to check if a string starts with a specified substring. It returns True if the string starts with the substring, otherwise it returns False.
a = "Hylndal"
print(a.startswith("y"))

#endswith
#note: endswith is used to check if a string ends with a specified substring. It returns True if the string ends with the substring, otherwise it returns False.
a = "Hylndal"
print(a.endswith("a"))

#replace
#note: replace is used to replace a specified substring with another substring in a string. It returns a new string with the specified substring replaced.
a = "Hylndal"
print(a.replace("y", "i"))

#strip
#note: strip is used to delete the spacing between both sides of the string. It returns a new string with the specified substring replaced.
a = " Hylndalmy "
print(a.strip())

#rstrip
#note: rstrip is used to delete the spacing on the right side of the string. It returns a new string with the specified substring replaced.
a = " Hylndalmy "
print(a.rstrip())

#lstrip
#note: lstrip is used to delete the spacing on the left side of the string. It returns a new string with the specified substring replaced.
a = " Hylndalmy "
print(a.lstrip())

#split
#note: spllit is used to split a string with it own charcater
a = "Hylndalmy"
print(a.split("l"))

#join
#note: join is used to join the elements of a sequence (string, list, tuple) into a single string. It returns a new string with the specified separator between each element.
a = "Hy""ln""dal""my"
print("-".join(a))

#isalpha
a = "Hylndalmy"
print(a.isalpha())

#isdigit
a = "23313313"
print(a.isdigit())

#isalnum
a = "23andfb"
print(a.isalnum())

#islower
a = "hylndalmy"
print(a.islower())

#isupper
a = "HYLNDAALMY"
print(a.isupper())

#f-string
a = "Manu"
print(f"You {a} has money")

#format
a = "Monday"
print("we have {} holiday".format(a))
