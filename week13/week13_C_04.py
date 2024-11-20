# week13_C_04.py
# id:202444095
# name:kim jaemin
import datetime
li = []
fmt = "%Y-%m-%d %H:%M:%S"
while True:
    num = input("도서번호:").strip()
    if not num:
        break
    dae = input("대출시간:")
    dae = datetime.datetime.strptime(dae, fmt)  # 수정: datetime 모듈을 사용할 때는 'datetime.'을 추가
    ban = input("반납시간:")# strptime으로 변환
    ban = datetime.datetime.strptime(ban, fmt)
    dic = {}
    dic['num'] = num
    dic['dae'] = dae
    dic['ban'] = ban
    li.append(dic)

for item in li:
    print(item['num'], item['dae'], item['ban'])
