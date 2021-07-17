import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/"
response = requests.get(url)

hmtl_icerigi = response.content

soup = BeautifulSoup(hmtl_icerigi, "html.parser")

basliklar = soup.find_all("td", {"class": "titleColumn"})
imdb = soup.find_all("td", {"class": "ratingColumn imdbRating"})

a = float(input("istediğiniz imdb puanını yazınız:"))

for baslik, rating in zip(basliklar, imdb):
    baslik = baslik.text
    rating = rating.text

    baslik = baslik.strip()
    baslik = baslik.replace("\n", "")

    rating = rating.strip()
    rating = rating.replace("\n", "")
    if float(rating) >= a:
        print("başlık:", baslik, "imdb:", rating)
