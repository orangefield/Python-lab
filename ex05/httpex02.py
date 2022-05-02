from weather import Weather
import http_provider as hp

datas = hp.get("http://apis.data.go.kr/1360000/TourStnInfoService/getCityTourClmIdx?serviceKey=dSHJNipMJz%2BPWTt9UN2qgExW7ql36lF%2BXp81YL%2FD42muatm7QP9jYJQSfIPMJ79C6NLitgJqd%2FGhRmY6U6YWwg%3D%3D&pageNo=1&numOfRows=10&dataType=JSON&CURRENT_DATE=2018123110&DAY=3&CITY_AREA_ID=5013000000")

print(datas)
print(datas[0]["cityAreaId"])
# 키값을 잘못 쓰는 실수를 방지하기 위해 클래스화 - weather.py

weathers = []  # 빈 리스트를 만들어서 클래스를 옮긴다

# dict으로 다 되면 이 부분을 굳이 만들 필요는 없다
for data in datas:
    weather = Weather.dictToEntity(data)
    weathers.append(weather)

print(weathers[0].tm)
