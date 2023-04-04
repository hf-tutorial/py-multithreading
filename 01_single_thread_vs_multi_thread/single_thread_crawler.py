import requests
from model import UrlList


def craw(url: str):
    r = requests.get(url)
    print(url, len(r.text))
