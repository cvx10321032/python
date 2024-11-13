#week10_01.py
myfile = "C:\\s202444095\\kjm.txt"
# 1. 열기
#f = open(myfile, 'w')  # 기존 파일이 있을시 덮어씀 
f = open(myfile, 'a') # 추가모드
# 2. 작업
f.write("김재민\n")
#print(f.read())
# 3. 닫기
f.close()

f = open(myfile, 'r')
print(f.read())
f.close()
