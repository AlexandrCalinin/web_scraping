import requests
from bs4 import BeautifulSoup


url = "https://www.culture.ru/literature/poems/tag-o-lyubvi"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/114.0.0.0 Safari/537.36"
}
req = requests.get(url=url, headers=headers)
src = req.text

with open("index.html", "w", encoding="utf-8") as file:
    file.write(src)
