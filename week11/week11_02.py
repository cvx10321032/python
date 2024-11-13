# week11_02.py
import datetime
class Test:
    def __init__(self): #매개변수, parameter, local
        name = "a"      #local
        self.name = "b" #attr. member/instance var
        self.age = 20   #상동.
        print(datetime.datetime.now())
t = Test()              
print(t.name)
#1st : Test() 생성자 호
#2nd : __new__() 메소드 자동 호출
#      Test의 인스턴스를 생성.
#3rd : __init__() 메소드 자동 호축
#      Test의 인스턴스를 초기화
#4th : 생성한 인스턴스의 참조를 반환
t = Test()
print(t.name)

t2 = Test()
print(t.name)

#t3 = t2
t.name = "김인하"
t2.name = "이인하"

print(id(t), id(t2))
print(type(t) == type(t2))
print(t == t2)
print(t.name == t2.name)
print(t.age == t2.age)
