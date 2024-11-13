# week09_01
data1 = [1, 2, 3, 4]

summary = sum(data1)
maximum = max(data1)
minimum = min(data1)
average = sum(data1) / len(data1)
print(summary)
print(maximum)
print(minimum)
print(average)

print("-"*30)
for i in data1:
    print(i)

print("-"*30)
for i in range(len(data1)):
    print(i)

print("-"*30)
for i in range(len(data1)):
    print(f"data1[{i}]:{data1[i]}")
print("-"*30)
for i in enumerate(data1):
    print(f"data1[{i[0]}]:{i[1]}")
print("-"*30)
for i, j in enumerate(data1):
    print(f"data1[{i}]:{j}")
data2 = [
            [1,2,3]
            ,[10, 20]
            ,[11, 12, 13, 14]
            ]
print("-"*30)
for i in data2:
    print(i)

print("-"*30)
for i in data2:
    print(f"sum: {sum(i)}")
    print(f"max: {max(i)}")
    print(f"min: {min(i)}")
    print(f"avg: {sum(i)/len(i)}")

print("-"*30)
for j, i in enumerate(data2):
    print(f"{j+1}번째: {i}")
    print(f"sum {sum(i)}")
    print(f"max {max(i)}")
    print(f"min {min(i)}")
    print(f"avg {sum(i)/len(i)}")
print("-"*30)
for j, i in enumerate(data2):
    print(f"{j+1}번째: ",end="")
    for a, b in enumerate(i):
        print(f"[{a+1}]{b}", end=" ")

    print()
    print(f"sum {sum(i)}")
    print(f"max {max(i)}")
    print(f"min {min(i)}")
    print(f"avg {sum(i)/len(i)}")

data3 = {
    "김인하": [1,2],
    "이인하": [10,20,30,40,50,60,70],
    "송인하": [11,12,13,14]
}
print("-"*30)
for i in data3:
    print(i)
print("-"*30)
for i in data3:
    print(f"{i}:{data3[i]}")

print("-"*30)

for i in data3:
    n = data3[i]
    print(f"{i} :",end="")
    for idx, data in enumerate(n):
        print(f"[{idx}]{data}", end=" ")
    print()
    print(f"sum {sum(n)}")
    print(f"max {max(n)}")
    print(f"min {min(n)}")
    print(f"avg {sum(n)/len(n)}")




    
