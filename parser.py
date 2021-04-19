from bs4 import BeautifulSoup
from manga import Manga
import requests

URL = "https://www.starcomics.com/catalogo-fumetti"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser").find("tbody").find_all("tr")


# This function format scraped elements
def format_text(element):
    element = element.text
    return element.strip().replace("  ", "").splitlines()


# This function adds manga to a list
def create_manga(collection):
    for el in soup:
        link = el.find("a", href=True)
        data = list(filter(None, format_text(el)))
        manga = Manga(data[0], data[1], data[2], link)
        collection.append(manga)
