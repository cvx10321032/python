# week05_04.py
score = int(input("점수를 입력하세요"))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else: #중첩if
    print("이건 좀...")
    if score >= 70:
        print("C")
    elif score >= 70:
        print("D")
    else:
        print("F")
