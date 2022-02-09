from random import randrange
from time import sleep

import requests
import json


headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
Chrome/96.0.4664.174 YaBrowser/22.1.2.834 Yowser/2.5 Safari/537.36"
}



with open("json/all_food_dict.json", encoding="UTF-8") as file:
    all_food = json.load(file)

    for item in all_food:
        url = all_food[item][0]
        id_food = all_food[item][2]
        req = requests.get(url, headers=headers)
        src = req.text


        print(id_food)

        with open(f"site_food/{id_food}.html", "w", encoding="UTF-8") as file:
            file.write(src)




