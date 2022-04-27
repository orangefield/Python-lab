# for문 연습
for i in range(1, 10):  # 1~9
    print(i)

for i in range(1, 11, 2):  # 1~10, step=2
    print(i)

list = [1, 2, 3, 4]

for i in list:
    print(i)

tuple = (6, 7, 8)

for i in tuple:
    print(i)


# 2중 for문
for i in tuple:
    for j in list:
        print(i*j)
