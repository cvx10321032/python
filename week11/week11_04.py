# week11_04.py
class Student:
    def __init__(self):
        self.name = ""
        self.number = ""
        self.dept = ""
        self.birthyear = 0.0
students = []
for i in range(3):
    a = Student()
    a.name = input("이름:")
    a.number = input("학번:")
    a.dept = input("학과:")
    a.birthyear = int(input("생년:"))
    students.append(a)
for i in students: # type(i) ==> __init__Student
    print(i.name)
# (1) 동일한 학번이 들어오면?
# (2) list가 아닌 ditc로 구성해보기.
#     key => ?
# (3) while 무한반복
