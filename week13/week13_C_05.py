# week13_C_05~8.py
# id:202444095
# name:kim jaemin
import datetime
import os
myfile = "E:\py\week13\C\book1.txt"
def dae_ban_second(dae, ban):
    if not ban:
        ban = datetime.now()
    return (ban - dae).total_seconds()
li = []
fmt = "%Y-%m-%d %H:%M:%S"
while True:
    num = input("도서번호:").strip()
    if not num:
        break
    while True:
        try:
            dae = input("대출시간:").strip()
            if dae:
                dae = datetime.datetime.strptime(dae, fmt)  # 수정: datetime 모듈을 사용할 때는 'datetime.'을 추가
                break
        except:
            pass
    while True:
        try:
            ban = input("반납시간:").strip()# strptime으로 변환
            if not ban:
                ban = None
            else:
                ban = datetime.datetime.strptime(ban, fmt)
            break
        except:
            pass
    dic = {}
    dic['num'] = num
    dic['dae'] = dae
    dic['ban'] = ban
    li.append(dic)

for item in li:
    print(item['num'], item['dae'], item['ban'])
    print(dae_ban_second(item['dae'], item['ban']))
