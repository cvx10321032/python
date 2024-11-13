# week05_02.py
toeic = int(input("TOEIC:"))
age = int(input("AGE:"))
grade = int(input("GRADE:"))
temp = int(input("TEMPERATURE:"))
height = int(input("HEIGHT:"))

a = toeic >= 800 and age < 30
b = toeic >= 800 or age < 30
c = temp < 10 or temp > 28

d = not (age == 30) and toeic < 600
# d = age != 30 and toeic < 600

e = height >= 120 and height <= 160
# e = 120 <= height <= 160
print(a, b, c, d, e)

car = "KIA"
print(car == "Kia")
print(car.lower() == "kia")
#peint(car.lower() == "kia".lower())
print(car.lower() != "bmw")
print("*" * 30)

cars = ["audi", "tesla", "benz", "kia", "bmw", "hyundai"]
car = "KIA"
print(car in cars)
print(car not in cars)
print(car.lower() in cars)
print(car.lower() not in cars)
print("*" * 30)

t3 = 3 <= 2
t4 = 5 != 3
year = 2021
t5 = ((year % 4 == 0) and (year % 100 !=)) or (year % 400 == 0)
print(t3, t4, t5)
