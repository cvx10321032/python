# week06_04.py
fruites = {'kim':'딸기', 'lee':'귤'}

for f in fruites:
    print(f, fruites[f])

for f in fruites.keys():
    print(f, fruites[f])

#for f in fruites.key():
    #print(f, fruites['f'])
    #pass
for f in fruites.values():
    print(f)

for f in fruites.items():
    print(f)
    print(f[0],f[1])
for f1, f2 in fruites.items():
    print(f1, f1)

a = {'h':127.0, 'w':30, 'e':2.0}
b = {'h':160, 'w':40}
c = [a, b]

for idx, ele in enumerate(c):
    print(f"{idx+1}번 키:{ele['h']}")
    print(f"{idx+1}번 키:{c[idx]['h']}")
    #시력은?
a = {
    'source': '고추장',
    'topping': ['버섯','계란']
}

topping = '/'.join(a['topping'])
print(f"양념:{a['source']}")
print(f"고명:{topping}")

a = {
    "kim": {1: "귤", 2: "사과"},
    "lee": {1: "귤", 2: '딸기'},
}

for k, v in a.items():
    print(f"{k}씨가 좋아하는 과일")
    print(f"{v[1]}, {v[2]}")
