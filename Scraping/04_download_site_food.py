from tqdm import tqdm
import os.path
import requests
import json

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
Chrome/96.0.4664.174 YaBrowser/22.1.2.834 Yowser/2.5 Safari/537.36"
            }

with open("json/all_food_dict.json", encoding="UTF-8") as file:
    all_food = json.load(file)

    for id_food, value in tqdm(all_food.items()):  #tqdm - progressbar
        url = value[0]
        id_food = id_food

        if os.path.exists(f"site_food/{id_food}.html") == False:  # check existing of file
            req = requests.get(url, headers=headers)
            src = req.text
            with open(f"site_food/{id_food}.html", "w", encoding="UTF-8") as file:
                file.write(src)




