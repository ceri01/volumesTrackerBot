from bs4 import BeautifulSoup
from manga import Manga
import requests
import re

URL = "https://www.starcomics.com/catalogo-fumetti"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser").find("tbody")


# This function format scraped elements
def format_text(element):
    element = element.text
    return element.strip().replace("  ", "").splitlines()


# This function adds manga to list
def create_list(name: str):
    lst = []
    name = str.upper(name)
    for el in soup.find_all("tr"):
        link = ""
        a = el.find("a", href=True)
        if a.getText().strip().find(name) != -1:
            link = a['href']
            data = list(filter(None, format_text(el)))
            manga = Manga(data[0], data[1], data[2], link)
            lst.append(manga)
    return lst
