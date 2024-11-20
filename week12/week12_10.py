# week12_10.py
def test():
    raise NotImplementedError("test함수 미작성")
while True:
    try:
        dvd = int(input("피제수:"))
        dvs = int(input("제수:"))
        result = dvd / dvs
        print(result)
    except ValueError:
        print("올바른 정수를 넣어라 허접")
    except ZeroDivisionError:
        print("제수는 0을 넣으면 다매!")
    except Exception: # ValueError, ZeroDivisionError 조상님
        print("지금이야! 뛰어내려")
    except Exception as e:
        print(e)
    else:
        print("try문이 완벽히 실행하면 할 것")
    finally:
        print("안녕히 계세요 여러분")
