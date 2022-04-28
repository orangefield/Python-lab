import requests

# python -m pip install requests

r = requests.get("http://openapi.tago.go.kr/openapi/service/DmstcFlightNvgInfoService/getFlightOpratInfoList?serviceKey=wJmmW29e3AEUjwLioQR22CpmqS645ep4S8TSlqtSbEsxvnkZFoNe7YG1weEWQHYZ229eNLidnI2Yt5EZ3Stv7g%3D%3D&numOfRows=10&pageNo=1&depAirportId=NAARKPK&arrAirportId=NAARKPC&depPlandTime=20220125&airlineId=ABL&_type=json")
responseDict = r.json()

print(responseDict)
print("="*60)
print(responseDict["response"]["body"]["items"]["item"][0])
