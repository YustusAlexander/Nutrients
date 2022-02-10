import csv
import json
from tqdm import tqdm


with open("json/all_food_nutrients_dict.json", encoding="UTF-8") as file:
    all_food_nutrients_dict = json.load(file)


with open('json/Nutrients_DB.csv', newline='', mode='w', encoding="UTF-8") as csvfile:
    fieldnames = [
            "Имя",
            "Кат",
            "Калорийность",
            "Белки",
            "Жиры",
            "Вода",
            "Зола",
            "Витамин_А__РЭ",
            "Ретинол",
            "бета_Каротин",
            "Витамин_В1__тиамин",
            "Витамин_В2__рибофлавин",
            "Ниацин",
            "Витамин_В9__фолаты",
            "Витамин_В4__холин",
            "Витамин_В5__пантотеновая",
            "Витамин_В6__пиридоксин",
            "Витамин_В12__кобаламин",
            "Витамин_Е__альфа_токоферол__ТЭ",
            "Витамин_Н__биотин",
            "Витамин_РР__НЭ",
            "Витамин_C__аскорбиновая",
            "Крахмал_и_декстрины",
            "Витамин_D__кальциферол",
            "Витамин_D3__холекальциферол",
            "Витамин_К__филлохинон",
            "Бетаин",
            "Калий__K",
            "Кальций__Ca",
            "Магний__Mg",
            "Натрий__Na",
            "Сера__S",
            "Фосфор__P",
            "Железо__Fe",
            "Марганец__Mn",
            "Медь__Cu",
            "Селен__Se",
            "Цинк__Zn",
            "Хлор__Cl",
            "Йод__I",
            "Кобальт__Co",
            "Молибден__Mo",
            "Никель__Ni",
            "Фтор__F",
            "Хром__Cr",
            "Олово__Sn",
            "Жирные_кислоты",
            "Углеводы",
            "Пищевые_волокна",
            "Моно__и_дисахариды_(сахара)",
            "гамма_Токоферол",
            "Органические_кислоты"
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, restval=0, extrasaction='ignore')
    writer.writeheader()

    for id_food, lst in tqdm(all_food_nutrients_dict.items()):
        dict_for_write = {"Имя": lst[1], "Кат": lst[2]}

        if len(lst) == 4:
                for nutrient_name, nutrient_value in lst[3].items():
                        dict_for_write[nutrient_name] = nutrient_value
                writer.writerow(dict_for_write)
                dict_for_write.clear()
        else:
                print(f'Отсутствуют нутриенты {id_food}')