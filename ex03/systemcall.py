import os
import time

# os.system에서 system call 사용 가능
# 파이썬으로 OS의 Script를 많이들 짠다
# Shell 언어, Pearl 언어 공부 안하고 py파일 실행!
os.system("dir")

workDir = os.path.abspath("./")
print(workDir)


# while True:
#     time.sleep(1000)
#     workDir = os.path.abspath("./")
#     workDir += "a.txt"

#     f = open(workDir, "r")
