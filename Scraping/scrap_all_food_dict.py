from bs4 import BeautifulSoup
import json
import requests

# извлечение списка категорий
arr_all_categories = []
with open("json/all_categories_dict.json") as file:
    all_categories = json.load(file)
    for item in all_categories:
        arr_all_categories.append(item)


# извлечение названия еды и ссылки
all_food_dict = {}
id_food = 10938
for index in range(1, 55):
    with open(f"site_cat/index{index}.html", encoding="UTF-8") as file:
         src = file.read()
    soup = BeautifulSoup(src, "lxml")
    all_row = soup.find_all("tr")
    for item in all_row:
        food = item.find("a")
        if food:
            id_food += 1
            title = food.get("title")
            name = title.split(":")[-1]
            href = 'https://health-diet.ru' + food.get("href")
            all_food_dict[id_food] = href, name, arr_all_categories[index-1]
            print(id_food, name)

# сохр в json
with open("json/all_food_dict.json", "w", encoding="UTF-8") as file:
    json.dump(all_food_dict, file, indent=4, ensure_ascii=False)