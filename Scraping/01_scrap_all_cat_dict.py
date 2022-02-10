from bs4 import BeautifulSoup
import json
headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
Chrome/96.0.4664.174 YaBrowser/22.1.2.834 Yowser/2.5 Safari/537.36"
}

with open("site_cat/catalog.html", encoding="UTF-8") as file:
    src = file.read()


soup = BeautifulSoup(src, "lxml")

cat_dict = {}
cat_id = 1
all_products_hrefs = soup.find_all(class_="mzr-tc-group-item-href")
for item in all_products_hrefs:
    cat_dict[cat_id] = "https://health-diet.ru" + item.get("href"), item.text
    cat_id += 1

with open("json/all_categories_dict.json", "w") as file:
    json.dump(cat_dict, file, indent=4, ensure_ascii=False)

