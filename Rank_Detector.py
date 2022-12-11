#writing and practicing code of python
students = {}
n = int(input("Enter the number of students "))
for i in range(n):
    name = input("Enter the name of the student ")
    marks = int(input("Enter the marks of the student "))
    students[name] = marks
students = dict(sorted(students.items(), key= lambda x:x[1],reverse = True))
for i in students:
    print(i,":",students[i])#it gives the students and marks in the key value pairs
s = input("Do you want to change the marks of the student press(Y/N)")
if s == "Y" or s == "y":
    a = input("Enter the name of the student you want to change marks ")
    newmarks = int(input("Enter the new marks of the student "))
    b = (list(students).index(a))+1
    for i in students:
        if i==a:
            students[i]=newmarks
    students = dict(sorted(students.items(),key = lambda x: x[1],reverse = True))

