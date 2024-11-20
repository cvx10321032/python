# week13_C_03.py
# id:202444095
# name:kim jaemin
import datetime
li = []
parsingFormat = "%Y-%m-%d %H:%M:%S"
while True:
    num = input("도서번호:").strip()
    if not num:
        break
    dae = input("대출시간:")
    ban = input("반납시간:")
    dic = {}
    dic['num'] = num
    dic['dae'] = dae
    dic['ban'] = ban
    #li.append({'num':num, 'dae':dae, 'ban':ban}) 한 번에 가능
    dic['dae'] = datetime.datetime.strftime(dic['dae'] , parsingFormat)
    dic['ban'] = datetime.datetime.strftime(dic['ban'] , parsingFormat)
    li.append(dic)
for li in li:
    print(li['num'], li['dae'], li['ban'])
    
