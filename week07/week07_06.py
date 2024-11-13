# week07_06.py

def findname(target, cmplist):
    if target in cmplist:
        return True
    else:
        return False
#def findname(target, cmplist):
#    return target in cmplist
names = ['김인하', '이미영', '박태영']
result1 = findname('이미영', names)
result2 = findname('김미영', names)
print(result1, result2)
result3 = findname(cmplist=names, target='이미영')
#result4 = findname(names, '이미영')
print(result3)#, result4)


def findname(target, cmplist):
	if isinstance(cmplist, list) or isinstance(cmplist, tuple) and isinstance(target, str):
		return target in cmplist

result5 = findname(cmplist=names, target='이미영')
result6 = findname(names, '이미영')
result7 = findname(cmplist=tuple(names), target='이미영')
result8 = findname(cmplist=tuple(names), target=12)
print(result5, result6, result7, result8)
