import requests
# 크롤링 연습 - 게시글 3개 스크랩

list = []

aid = ["0000000001", "0000000002", "1000000003"]  # 실전에서는 1 -> 10자리 포맷


for a in aid:
    try:
        print("나 3번 도나?")
        html = requests.get(
            f"https://n.news.naver.com/mnews/article/005/{a}?sid=100")
        print(html.status_code)  # 200 뜨는 것부터 보자
        if(html.status_code == 200):
            list.append(html.text)
    except Exception as e:
        pass

print(len(list))
print(list[0])
