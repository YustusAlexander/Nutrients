import requests
import json


headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
Chrome/96.0.4664.174 YaBrowser/22.1.2.834 Yowser/2.5 Safari/537.36"
}



with open("json/all_categories_dict.json") as file:
    all_categories = json.load(file)

    cat_id = 1
    for item in all_categories:
        url = all_categories[item][0]
        req = requests.get(url, headers=headers)
        src = req.text
        print(url)
        with open(f"site_cat/index{cat_id}.html", "w", encoding="UTF-8") as file:
            file.write(src)

        cat_id += 1



