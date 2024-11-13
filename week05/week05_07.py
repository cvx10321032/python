# 아래는 n명의 점수를 받는다.
# 나중에 5명의 점수를 받도록
# for으로 바꿔본다.

i = 0
scores = []

while i < 5:
    i += 1
    score = input(f"{i} 번째 점수: ")
    if not score.strip():
        break
    scores.append(float(score))

if 0 < len(scores):
    number = 0
    summary = 0
    for score in scores:
        number += 1
        summary += score
        print(f"{number} : {score}")
    print(f"avg:{summary/len(scores)}")
else: 
    print("점수가 존재하지 않습니다.")
