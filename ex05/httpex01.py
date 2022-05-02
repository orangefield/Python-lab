# 데이터 다운로드
# python -m pip install requests

import requests

response = requests.get("http://apis.data.go.kr/1360000/TourStnInfoService/getCityTourClmIdx?serviceKey=dSHJNipMJz%2BPWTt9UN2qgExW7ql36lF%2BXp81YL%2FD42muatm7QP9jYJQSfIPMJ79C6NLitgJqd%2FGhRmY6U6YWwg%3D%3D&pageNo=1&numOfRows=10&dataType=JSON&CURRENT_DATE=2018123110&DAY=3&CITY_AREA_ID=5013000000")

# dict response["키값"]
print(response)  # Header의 상태 코드만 볼 수 있다
print(type(response))  # 클래스 : response.~
print(type(response.json()))  # JSON을 파이썬 오브젝트로 바꿔주겠다
print(type(response.text))
print(response.status_code)


# print(response.json())
# item이 배열이라서 item까지 받으면 된다
# dict으로 받지만 마지막 데이터는 클래스에 담아놓는 게 오류도 안나고 좋다
datas = response.json()["response"]["body"]["items"]["item"]

for data in datas:
    print(data["doName"])
