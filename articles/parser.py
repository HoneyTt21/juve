import requests
from bs4 import BeautifulSoup

URL = "https://www.gazzetta.it/calcio/squadre/"
URL_NOT = "/notizie/"
URL_MER = "/calciomercato/"


def get_notizie(team):
    result = requests.get(URL + team + URL_NOT)

    soup = BeautifulSoup(result.text, "html.parser")

    pagination = soup.find("div", {"class": "pagination"})

    links = pagination.find_all("div", {"class": "media"})
    pages = []

    for link in links[:-1]:
        pages.append(int(link.find("span").string))
    max_page = pages[-1]

    return max_page
