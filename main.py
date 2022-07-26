cook_book = {}
with open ('book.txt', encoding = 'utf-8') as book:
    for dish in book:
        dishes = dish.strip()
        ingredient = int(book.readline())
        ing_list = []
        for ing in range(ingredient):
            ingredient_name, quantity, measure = book.readline().split("|")
            quantity = int(quantity)
            ing_list.append({"ingredient_name": ingredient_name, "quantity": quantity, "measure": measure.strip()})
        cook_book[dishes] = ing_list
        book.readline()
    print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    ing = {}
    for key, values in cook_book.items():
        if key in dishes:
            for value in values:
                if value['ingredient_name'] in ing:
                    for a, b in ing.items():
                        b['quantity'] += value['quantity'] * person_count
                else:
                    ing[value['ingredient_name']] = {'measure': value['measure'], 'quantity': value['quantity'] * person_count}
    print(ing)

get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)
