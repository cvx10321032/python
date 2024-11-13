# week05_01.py
class Test: # user-defined type(Test)
    def __init__(self):
        self.a = 1
        self.b = 2


test1 = [1,2] #type:list
test2 = (1,2) #type:tuple
test3 = Test() #type:Test

print(test1[0])
print(test2[0])
print(test3.a)

print(test1[1])
print(test2[1])
print(test3.b)

test1[0]=3
test2[0]=3  #tuple아님
test3.a=3

#print(test1[0])
#print(test2[0])
#print(test3.a)

