import math
student_count = 1000
rating = 4.4
is_publisted = True
course_name = "python programming"
message = """ hi sohel this is rana from sohel """

# find length
len(message)  # 34

course_name[0]  # p
course_name[-1]  # g
course_name[0:3]  # pyt
course_name[0:]  # python programming
course_name[:]  # python programming

# escape sequence

course = "mosh \"programming"

# formatter string

first = 'sohel'
last = 'rana'

full = first + last
full2 = f"{first} {last}"

# string methods
course = 'python programming '
course.upper()
course.lower()
course.title()
course.strip()  # trim
course.find("Pro")  # find index # 7, -1 if not found
course.replace("p", "j")
"pro" in course  # boolean
"swift" not in course  # boolean
course.split(" ")

# Numbers
value = 2.9
round(value)  # 3
abs(-2.5)  # 2.5

print(math.ceil(3.4))  # 4


# typeconversion
int()
float()
str()
bool()
x = input("x: ")
type(x)  # str
y = int(x) + 1
