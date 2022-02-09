from random import randrange
from time import sleep

import requests
import json


headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
Chrome/96.0.4664.174 YaBrowser/22.1.2.834 Yowser/2.5 Safari/537.36"
}


count = 3
with open("json/all_categories_dict.json", encoding="UTF-8") as file:
    all_categories = json.load(file)


    for item in all_categories:
        url = all_categories[item]
        req = requests.get(url, headers=headers)
        src = req.text
        count += 1

        print(url)

        with open(f"site_cat/index{count}.html", "w", encoding="UTF-8") as file:
            file.write(src)

        # sleep(randrange(2, 4))


