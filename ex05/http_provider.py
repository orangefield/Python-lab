# Repository가 아니라 provider
import requests as api


def get(url):
    response = api.get(url)
    if response.status_code == 200:
        # header, body
        datas = response.json()["response"]["body"]["items"]["item"]
        return datas
