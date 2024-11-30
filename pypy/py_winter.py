import user
import os
users = []
def add_user():
    print("[회원 정보 등록]")
    id = input("아이디:")
    for use in users:
        if use.id== id:
            print("중복된 아이디입니다.")
            return False
    gender = input("성별 (M:남자 F:여자):").upper()
    if gender not in ['M','F']:
        print("성별이 잘못 입력되었습니다.")
        return False
    try:
        height = float(input("신장(m):"))
    except:
        print("신장 입력이 잘못되었습니다.")
        return False
    try: 
        weight = float(input("체중(kg):"))
    except:
        print("체중 입력이 잘못되었습니다.")
        return False
    use = user.User(id, gender, height, weight)
    print(f"bmi:{use.bmi_calc():.2f}")
    users.append(use)
    
def update_user():
    if not users:
        print("수정할 회원이 없습니다.")
        return False
    print("[회원 정보 수정]")
    id = input("아이디:")
    for use in users:
        if use.id == id:
            print(f"현재 신장 :{use.height}m")
            try:
                height = float(input("수정 신장(m):"))
            except:
                print("수정 신장 잘못 입력")
                return False
            print(f"현재 체중 :{use.weight:.1f}kg")
            try:
                weight = float(input("수정 체중(kg):"))
            except:
                print("체중 입력이 잘못되었습니다.")
                return False
            use.height = height
            use.weight = weight
            return False
        else:
            print("회원정보가 없습니다.")
            break

def check_user():
    if not users:
        print("상태를 보여줄 회원이 없습니다.")
        return False
    print("[전체 상태 조회]")
    print('='*30)
    males = [use for use in users if use.gender == "M"]
    females = [use for use in users if use.gender == "F"]
    male_num = 0
    female_num = 0
    print("[남성]")
    for use in males:
        male_num += 1
        print(f"[{male_num}] 아이디:{use.id}  신장:{use.height}  체중:{use.weight:.2f}  BMI:{use.bmi_calc():.2f}")
        print("도표:"+'*'*int(use.bmi_calc()))
        print("")
    print("")
    print("[여성]")
    for use in females:
        female_num += 1
        print(f"[{female_num}] 아이디:{use.id}  신장:{use.height}  체중:{use.weight:.2f}  BMI:{use.bmi_calc():.2f}")
        print("도표:"+'*'*int(use.bmi_calc()))
        print("")
    print('='*30)
    print(f"총 {male_num+female_num}명의 정보입니다.")

def path_file():
    mypath = "e:\\pypy\\winter_txt"
    myfile = "bmilist.txt"
    fullfile = os.path.join(mypath, myfile)

    if not os.path.isdir(mypath):
        os.mkdir(mypath)
        
    return fullfile

def save_user():
    if not users:
        print("저장할 자료가 없습니다.")
        print("프로그램을 종료합니다.")
        return False
    with open(fullfile,'w') as f:
        for use in users:
            f.write(use.file_record())
        print(f"{len(users)}건의 데이터를 저장했습니다.")
    print("프로그램을 종료합니다.")

def load_user():
    fullfile = path_file()
    if not os.path.isfile(fullfile):
        print("복원할 데이터가 없습니다.")
        return False
    if users:
        print("원래 자료가 있음")
        return False
    else:
        with open(fullfile, 'r') as f:
            for datas in f:
                split_datas = datas.strip().split("|")
                us = user.User(split_datas[0], split_datas[1], float(split_datas[2]), float(split_datas[3]))
                users.append(us)
        print(f"{len(users)}건의 데이터를 복원했습니다.")
                
print('#'*30)
print("A. 기존자료복원")
print("B. 회원등록")
print("C. 정보수정")
print("D. 전체조회")
print("Q. 종료 및 회원정보 저장")
print('#'*30)
if __name__ == '__main__':
    fullfile = path_file()
    while True:
        answer = input("").lower().strip()
        if answer == "a":
            load_user()
        elif answer == "b":
            add_user()
        elif answer == "c":
            update_user()
        elif answer == "d":
            check_user()
        elif answer == "q":
            save_user()
            break
        else:
            continue
