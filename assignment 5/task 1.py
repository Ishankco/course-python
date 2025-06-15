n = int(input("enter the number of student"))
DICT = {}
for i in range(n):
    nane = input("enter the name of student")
    marks = int(input("enter the marks of student"))
    DICT.update({nane:marks})

a= input("enter the student name")
if a in DICT:
    print(a,"MARKS:",DICT[a])
else:
    print("student not found")
