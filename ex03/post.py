# 생성자를 만들어보자

# 타입 : Class
class Post:
    def __init__(self, username, password):
        self.username = username
        self.password = password


p = Post("ssar", "1234")

print(p.username)
print(p)  # 주소
print(p.__dict__)  # 클래스를 dict으로 바꾸는 방법
