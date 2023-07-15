import requests
from bs4 import BeautifulSoup


# url = "https://www.culture.ru/literature/poems/tag-o-lyubvi"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}
# req = requests.get(url=url, headers=headers)
# src = req.text
#
# with open("index.html", "w", encoding="utf-8") as file:
#     file.write(src)

# with open("index.html", encoding="utf-8") as file:
#     src = file.read()


pages_list = list()
for page_number in range(1, 109):
    url = "https://www.culture.ru/literature/poems/tag-o-lyubvi?page=" + str(page_number)
    pages_list.append(url)

for page_url in pages_list:
    req = requests.get(page_url, headers)
    src = req.text
    print(src)
    soup = BeautifulSoup(src, "lxml")
    find_all_hrefs = soup.find(class_="A5Si4").find_all(class_="bMNap")
    for item in find_all_hrefs:
        item_text = item.find(class_="_1ERrb").find(class_="_9OVEn").find(class_="L5VcY").text
        item_text_string = " ".join(item_text.split())
        item_url = "https://www.culture.ru" + item.find(class_="_1ERrb").find(class_="_9OVEn").get("href")
        print(f"{item_text_string}: {item_url}")
