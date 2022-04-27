import json
# 데이터 다루기에 파이썬이 참 좋다!

# JSON 처럼 생긴 문자열
json_str = '''
{"id": 1,"username":"ares", "password":"1234"}
'''

# JSON -> dict
dic1 = json.loads(json_str)
print(dic1) # dict은 DB에 그대로 들어간다
print(dic1["password"])

# dict -> JSON
dict_to_json = json.dumps(dic1)
print(dict_to_json)