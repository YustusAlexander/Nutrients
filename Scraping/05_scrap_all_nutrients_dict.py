from bs4 import BeautifulSoup
import json
from tqdm import tqdm

with open("json/all_food_dict.json", encoding="UTF-8") as file:
    all_food_nutrients_dict = json.load(file)

# извлечение нутриентов
all_nutrients_dict = {}
rep = [",", " ", "-", "'"]
for id_food in tqdm(range(10939, 11050)):  #10939-23354 tqdm - прогресс выполнения

    try:
        with open(f"site_food/{id_food}.html", encoding="UTF-8") as file:
             src = file.read()
        soup = BeautifulSoup(src, "lxml")
        all_row = soup.find_all('tr')
        for item in all_row:   # поиск строк с названиями нутриентов на сайте
            nutrient_name = item.find('td', class_="mzr-tc-chemical-level-1")
            if nutrient_name:
                nutrient_val = nutrient_name.find_next().text
                nutrient_name = nutrient_name.text

                for item_rep in rep:   # замена названий нутриентов
                    if item_rep in nutrient_name:
                        nutrient_name = nutrient_name.replace(item_rep, "_")

                all_nutrients_dict[nutrient_name] = nutrient_val   # temp dict for nutrients

        # поместить словарь all_nutrients_dict внутрь словаря all_food_dict по совпадению id_food
        all_food_nutrients_dict[str(id_food)].append(all_nutrients_dict)
        all_nutrients_dict = {}
    except:
        print(f'отсутствует файл {id_food}')


with open("json/all_food_nutrients_dict.json", "w", encoding="UTF-8") as file:
    json.dump(all_food_nutrients_dict, file, indent=4, ensure_ascii=False)
# сохр в csv отдельно