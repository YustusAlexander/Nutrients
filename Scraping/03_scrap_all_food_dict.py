from bs4 import BeautifulSoup
import json
import requests

# извлечение списка категорий
with open("json/all_categories_dict.json") as file:
    all_categories = json.load(file)

# print(all_categories.get(str(cat_id))[1])

# извлечение названия еды и ссылки
all_food_dict = {}
id_food = 10939
for cat_id in range(1, 55):
    with open(f"site_cat/index{cat_id}.html", encoding="UTF-8") as file:
         src = file.read()
    soup = BeautifulSoup(src, "lxml")
    all_row = soup.find_all("tr")
    for item in all_row:
        food = item.find("a")
        if food:
            title = food.get("title")
            name = title.split(":")[-1]
            href = 'https://health-diet.ru' + food.get("href")
            all_food_dict[id_food] = href, name, all_categories.get(str(cat_id))[1]
            print(id_food, name)
            id_food += 1

# сохр в json
with open("json/all_food_dict.json", "w", encoding="UTF-8") as file:
    json.dump(all_food_dict, file, indent=4, ensure_ascii=False)