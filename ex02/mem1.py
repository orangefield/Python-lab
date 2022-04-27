# 함수 (: 클래스 내부에 있는 것이 아닌 것들)
def add():
    print("더하기")


def minus():
    return 1


add()

n = minus()
print(n)


# 오버로딩이 없다 (+ 디폴트값이 있는 것은 앞에 둘 수 없다)
def multi(n1, n2):
    print(f"곱하기 {n1}*{n2}")


multi(3, 2)


def multi(n1, n2=3):
    print(f"곱하기 {n1}*{n2}")


multi(2)
