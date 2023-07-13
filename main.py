from bs4 import BeautifulSoup
import requests

year = input("Which year do you want to travel to? type the date in this format YYYY-MM-DD:  ")

URL = f"https://www.billboard.com/charts/hot-100/{year}"

response = requests.get(URL)

data = response.text

soup = BeautifulSoup(data, "html.parser")
songs = soup.select("li.o-chart-results-list__item > h3.c-title")

playlist = [song.get_text().strip() for song in songs]

# print(playlist)
