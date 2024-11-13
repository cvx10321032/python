# week11_05.py
class Test:
    def __init__(self):
        self.name = None
        self.age = None
    def func(self, name, age):
        self.name = name
        print(age)
t = Test()
print(t.name)
print(t.age)
t = Test()
t.func("김인하", 20)
print(t.name)
print(t.age)

print("-"*30)
class In:
    def func(self):
        print("In.func()")
class Out:
    def method(self):
        print("Out.method()")

# 안되면 주석.
i = In()
o = Out()
# 정식표현인데 (잘 안씀)
Out.method(o)
In.func(i)
str.upper("a")
#약식표현 ( 많이 씀)
o.method()
i.func()
"a".upper()
#되지만 정상적으로 동작하지
#않을 가능성이 큼.
In.func(o)
Out.method(i)
#아예 실행되지 않음.
#o.func()
#i.method()
