from pprint import pprint

with open('recipes.txt', encoding='utf-8') as f:
    cook_book = {}

    for line in f:
        dish_name = line.strip()
        ingredients_count = f.readline().strip()
        ingredients = []

        for ingredient in range(int(ingredients_count)):
            items = f.readline().split(' | ')
            ingredients.append({
                'ingredient_name': items[0],
                'quantity': items[1],
                'measure': items[2].strip()
            })

        cook_book[dish_name] = ingredients
        f.readline()

pprint(cook_book)





def get_shop_list_by_dishes(dishes, person_count):
    for cook_book_keys, cook_book_val in cook_book.items():
        for dish in dishes:
            if dish == cook_book_keys:

                for ingredient_keys in cook_book_val:
                    ingredients_dict = {}
                    ingredient_k = ingredient_keys['ingredient_name']
                    ingredient_keys.pop('ingredient_name')
                    ingredients_dict[ingredient_k] = ingredient_keys

                    if person_count == len(dishes):
                        pprint(ingredients_dict)

                    else:
                        num_persons = int(ingredient_keys['quantity'])
                        num_persons *= person_count
                        ingredient_keys['quantity'] = num_persons
                        pprint(ingredients_dict)
    return

get_shop_list_by_dishes(['Омлет', 'Фахитос'], 3)





files = ["1.txt", "2.txt", "3.txt"]
dict_ = {}
sorted_dict = {}
for file in files:
    with open(file, "r", encoding="utf-8") as f:
        lines = f.readlines()
        dict_[file] = len(lines)

sorted_keys = sorted(dict_, key=dict_.get)
for i in sorted_keys:
    sorted_dict[i] = dict_[i]

for new_file_sort in sorted_dict.keys():
    with open(new_file_sort, 'r', encoding='utf-8') as sf, open('new_file.txt', 'a', encoding='utf-8') as nf:
        count = 0
        nf.write(f'{new_file_sort}\n{sorted_dict[new_file_sort]}\n')
        for line_sorted in sf:
            count += 1
            nf.write(f'Строка номер {count} файла номер {new_file_sort[0]}\n')











