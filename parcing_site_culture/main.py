import json
import requests
from bs4 import BeautifulSoup


headers = {
    "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

# for page_number in range(1, 109):
#     url = "https://www.culture.ru/literature/poems/tag-o-lyubvi?page=" + str(page_number)
#     req = requests.get(url=url, headers=headers)
#     src = req.text
#     with open(f"html/{page_number}.html", "w", encoding="utf-8") as file:
#         file.write(src)
#     print(f"{page_number} страница скопирована")

result = dict()
for index in range(1, 109):
    with open(f"html/{index}.html", "r", encoding="utf-8") as file:
        src = file.read()
    soup = BeautifulSoup(src, "lxml")
    find_all_hrefs = soup.find(class_="A5Si4").find_all(class_="bMNap")

    for item in find_all_hrefs:
        item_text = item.find(class_="_1ERrb").find(class_="_9OVEn").find(class_="L5VcY").text
        item_text_string = " ".join(item_text.split())
        item_url = "https://www.culture.ru" + item.find(class_="_1ERrb").find(class_="_9OVEn").get("href")
        result[item_text_string] = item_url

with open("result.json", "w") as file:
    json.dump(result, file, indent=4, ensure_ascii=False)
