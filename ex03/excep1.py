
try:
    f = open("c:/hello.txt", "r")
    print(2/0)
except Exception as e:
    print(e)
finally:
    print("finally : try, except 어디를 타든 무조건 실행됨")
