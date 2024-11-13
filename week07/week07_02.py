# week07_02.py
def test(a, b, c=2, d=1):
    print(a, b, c, d)

for i in range(1,6):
    if i % 3 == 0:
        test(i, i+1, i+2, i+3)
    else:
        test(i, b=i+3)
        print("abc" + str(i), end="_", sep="/")
