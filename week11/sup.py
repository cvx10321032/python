class Subject:
    def __init__(self, num, nm, t=None, g=None):
        self.number = num
        self.name = nm
        self.teacher = t
        self.grade = g
    # (숙제) 현재 과목의 grade를 비교하여 평가를 반환하는 메소드를 정의
    #        4.5 => "최우수"
    #        4.0 이상 => "우수"
    #        3.5 이상 => "준수"
    #        3.0 이상 => "보통"
    #        3.0 미만 => "노력 필요"
    #        None => "성적 부여전"
    def getReview(self):
        if not(self.grade):
            return "성적 부여전"
        elif(self.grade == 4.5):
            return "최우수"
        elif(self.grade >= 4.0):
            return "우수"
        elif(self.grade >= 3.5):
            return "준수"
        elif(self.grade >= 3.0):
            return "보통"
        else:
            return "노력필요"
    # (숙제) grade를 등록하는 메소드를 정의 (호출 형태는 아래 setGrade() 참고)
    #       단. grade가 0.0 미만이면 0.0으로 grade가 4.5를 초과하는 경우는 4.5로 강제 변환한다.
    def setGrade(self, g):
        self.grade = g
        if g>4.5:
            self.grade = 4.5
        elif g<0.0:
            self.grade = 0.0
        else:
            self.grade = g
    # (숙제) 현재 과목의 학수번호와 과목이름을 조합하여 같은 문자열로 반환하는 __str__() 메소드 재정의
    def __str__(self):
        return f"{self.number}, {self.name}"

# Subject()
Subject("001", "파이선")
Subject("001", "파이선", "이인하")
# Subject('001', '파이선', '이인하', 4.5)

subj = Subject("001", "파이선")
print(subj.getReview())
subj.setGrade(3.5)
print(subj.getReview())
print(subj)
