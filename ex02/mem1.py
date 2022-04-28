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


# ** dict으로 변환하는 문법

def my_dict(**data):
    print(data)
    pass


my_dict(id=1, username="ssar")  # 키값 있어야 한다!


# global 전역변수를 호출하는 방법
n1 = 1


def vartest():
    global n1
    n1 = 2


print(n1)

vartest()
print(n1)
