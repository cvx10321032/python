# week06_03.py
info = {}

info["n"] = "기미나"
info["a"] = 23
info["h"] = 163.2
print(info)

info["h"] = 173.2
print(info)

del info["h"]
print(info)

#print(f"키:{info['h']}cm")

if 'h' in info:
    print(f"키:{info['h']}cm")
else:
    print("키 없다.")

a = info.get('a')
if a:
    print(f"키:{info['a']}cm")
else:
    print("키 없다.")

print(f"키:{info.get('h', '-')}cm")

info.clear()
print(info) 
