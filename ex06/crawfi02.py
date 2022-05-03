import requests

list = []

for a in range(1, 1000000000):
    aid = str(a).zfill(10)

    try:
        html = requests.get(
            f"https://n.news.naver.com/mnews/article/005/{aid}?sid=100")
        print(html.status_code)  # 200 뜨는 것부터 보자
        if(html.status_code == 200):
            list.append(html.text)
    except Exception as e:
        pass


print(len(list))
print("="*60)
print(list[0])
