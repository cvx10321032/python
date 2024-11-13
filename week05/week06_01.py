#week06_01.py
values = [1,2,3,4]
values_1 = [ ]
for v in values:
    values_1.append(v * 3)
values_1_1 = [v for v in values]
print(values_1_1)
values_1_2 = [v * 3 for v in values]
print(values_1_2)
values_2 = [ ]
for v in values:
    if v % 2 == 0:
        values_2.append(v * 3)
values_2_1 = [v * 3 for v in values if v % 2 == 0]#리스트 딕셔너리 차이
print(values_2_1)
print(values)
print(values_1)
print(values_2)
values = ['1','2','3']
# 위 values의 데이터를 모두 정수로 변환한
# 새로운 리스트를 만들어보세요.
# 리스트 내포를 이용하세요.
values_1 = [ int(v) for v in values ]
print(values_1)

mx = int(input("최대수:"))
# 최대수를 받아서 1~mx까지의 숫자를
# 리스트로 만들어보세요
# 단 리스트 내포를 이용하셔야 합니다.
#[ B' for B in A(seq)]
results = [v for v in range(1,mx + 1)]
print(results)
