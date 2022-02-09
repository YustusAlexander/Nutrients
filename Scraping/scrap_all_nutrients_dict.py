from bs4 import BeautifulSoup
import json
import requests




# извлечение нутриентов
all_nutrients_dict = {}
rep = [",", " ", "-", "'"]
for index in range(10939, 10940):
    with open(f"site_food/{index}.html", encoding="UTF-8") as file:
         src = file.read()
    soup = BeautifulSoup(src, "lxml")
    all_row = soup.find_all('tr')
    # print(all_row)
    for item in all_row:
        food = item.find('td', class_="mzr-tc-chemical-level-1")
        if food:
            nutrient = food.find_next()
            nutrient_val = nutrient.text
            food = food.text
            # замена названий еды
            for item in rep:
                if item in food:
                    food = food.replace(item, "_")

            all_nutrients_dict[food] = nutrient_val
            print(food, nutrient_val)

    # поместить словарь all_nutrients_dict внутрь словаря all_nutrients_dict по совпадению index
    with open("json/all_nutrients_dict.json", encoding="UTF-8") as file:
        all_food_dict = json.load(file)


        all_food_dict[index] =






with open("json/all_nutrients_dict.json", "w", encoding="UTF-8") as file:
    json.dump(all_nutrients_dict, file, indent=4, ensure_ascii=False)

# сохр в csv отдельно