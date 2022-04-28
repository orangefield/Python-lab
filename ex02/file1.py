f = open("C:/upload/hello.txt", 'r')

for line in f.readlines():
    print(line)

while(True):
    line = f.readline()
    print(line)

    if line == "":
        break
