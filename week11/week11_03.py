# week11_03.py

'''
클래스명 : Reactangle(2d좌표)
필요 속성: x 위치(실수), y (실수)
           길이(실수), 높이(실수)
'''
class Rectangle:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.width = 0.0
        self.height = 0.0
#struct Rectancle{
#    double x,y,width,height; (저거랑 같대)
#}
'''
클래스 명 : Subject (과목)
필요 속성 : 학수번호(문자열), 과목명(문자열),
            교수자(문자열), 학점(실수)
'''
class Subject:
    def __init__(self):
        self.number = ""
        self.name = ""
        self.teacher = ""
        self.grade = 0.0
'''
클래스 명 : Subject (과목)
필요 속성 : 이름(문자열), 학번(문자열),
            학과(문자열), 생년(실수)
'''
class Subject:
    def __init__(self):
        self.name = ""
        self.number = ""
        self.dept = ""
        self.birthyear = 0.0
'''
클래스 명 : Rectangle2 (사각형)
필요 속성 : 시작점(Point), 너비 (실수), 높이 (실수)
'''
class Rectangle2:
    def __init__(self):
        self.width = 0.0
        self.height = 0.0
        self.spoint = point()
'''
클래스 명 : Rectangle3 (사각형)
속성:       시작점(Point), 종료점(Point)
'''
class Rectangle3:
    def __init__(self):
        self.spoint = point()
        self.epoint = point()
r = Rectangle3()
r.spoint.x = 1
r.spoint.y = 1

r.epoint.x = 10
r.epoint.y = 21

