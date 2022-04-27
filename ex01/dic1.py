import json

dic1 = {
    "id":1,
    "username":"ares"
}

print(dic1)

dic2 = '''{"id":1, "username":"ares"}'''

print(dic2)

print(dic1["username"])

# print(type(dic1))
# print(type(dic2))

# dic3 = json.loads(dic2)
# print(dic3["id"])