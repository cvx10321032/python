# week09_02.py

data2 = [
            [1,2,3]
            ,[10, 20]
            ,[11, 12, 13, 14]
            ]
data3 = {
    "김인하": [1,2],
    "이인하": [10,20,30,40,50,60,70],
    "송인하": [11,12,13,14]
}


def print_info(datas):
    for idx, data in enumerate(datas):
        print(f"[{idx}]{data}", end=" ")
    print()
    print(f"sum {sum(datas)}")
    print(f"max {max(datas)}")
    print(f"min {min(datas)}")
    print(f"avg {sum(datas)/len(datas)}")


def analyze_list(datas):
    for j, i in enumerate(datas):
        print(f"{j+1}번째: ",end="")
        print_info(i)

        
def analyze_dict(datas):
    for i in datas:
        print(f"{i} :",end="")
        print_info(datas[i])


def analyze_score(datas):
    if isinstance(datas, list):
        analyze_list(datas)
    elif isinstance(datas, dict):
        analyze_dict(datas)
    else:
        print("분석 불가")

        
analyze_score(data2)
print("-"*30)
analyze_score(data3)
analyze_score(12)

    
