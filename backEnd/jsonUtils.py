import json
from .exceptions import InvalidMealException, BigMealException

with open("data/meals.json") as file:
	mealsJson = json.load(file)['meals']

with open("data/combos.json") as file:
	combosJson = json.load(file)['combos']
	
meal_dist_by_id_json = {
    meal["id"]: meal 
    for meal in mealsJson
}

meal_dist_by_name_json = {
    meal["name"]: meal
    for meal in mealsJson
}

combo_dist_by_id_json = {
    combo["id"]: combo
    for combo in combosJson
}

combo_dist_by_name_json = {
    combo["name"]: combo
    for combo in combosJson
}

def comp_cal_counter_json(*list_of_items):

    total_calories = 0
    for item in list_of_items:
        try:
            if item in meal_dist_by_id_json:
                total_calories += meal_dist_by_id_json[item]['calories']
            elif item in meal_dist_by_name_json:
                total_calories += meal_dist_by_name_json[item]['calories']
            elif item in combo_dist_by_id_json:
                for combo_item in combo_dist_by_id_json[item]['meals']:
                    total_calories += meal_dist_by_id_json[combo_item]['calories']
            else:
                for combo_item in combo_dist_by_name_json[item]['meals']:
                    total_calories += meal_dist_by_id_json[combo_item]['calories']

        except KeyError:
            raise InvalidMealException(item)

    if total_calories > 2000:
        raise BigMealException(total_calories)
    
    return total_calories


def price_counter_json(*list_of_items):

    sum_price = 0
    combo_price = 0
    for item in list_of_items:
        try:
            if item in meal_dist_by_id_json:
                sum_price += meal_dist_by_id_json[item]['price']
            elif item in meal_dist_by_name_json:
                sum_price += meal_dist_by_name_json[item]['price']
            elif item in combo_dist_by_id_json:
                combo_price += combo_dist_by_id_json[item]['price']
                for combo_item in combo_dist_by_id_json[item]['meals']:
                    sum_price += meal_dist_by_id_json[combo_item]['price']
            else:
                combo_price += combo_dist_by_name_json[item]['price']
                for combo_item in combo_dist_by_name_json[item]['meals']:
                    sum_price += meal_dist_by_id_json[combo_item]['price']

        except KeyError:
            raise InvalidMealException(item)
    
    # unit-test doesnt work with print

    # if combo_price == 0:
    #     return print(f"Total price: {sum_price} €")
    # else:
    #     return print(f"Combo price: {combo_price} €, Total if you buy individualy: {sum_price} €, You're savings: {sum_price - combo_price} €")

    if combo_price == 0:
        return sum_price
    else:
        return combo_price