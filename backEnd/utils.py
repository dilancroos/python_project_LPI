from .constants import calories, combos, meals, combos2, meal_dist_by_id, meal_dist_by_name, combo_dist_by_id, combo_dist_by_name


def calories_counter(*args):

    total_calories = 0

    for item in args:
        try:
            item = item.capitalize()
            if item in calories:
                total_calories += calories[item]
            else:
                for combo_item in combos[item.capitalize()]:
                    total_calories += calories[combo_item]

        except KeyError:
            print(f"Item '{item}' not found")

    return total_calories


def comp_cal_counter(*args):

    total_calories = 0

    for item in args:
        try:
            for meal in meals:
                if item == meal['id']:
                    total_calories += meal['calories']
                elif item == meal['name']:
                    total_calories += meal['calories']

            for combo in combos2:
                if item == combo['id']:
                    for mealInCombo in combo['meals']:
                        for meal in meals:
                            if mealInCombo == meal['id']:
                                total_calories += meal['calories']
                elif item == combo['name']:
                    for mealInCombo in combo['meals']:
                        for meal in meals:
                            if mealInCombo == meal['id']:
                                total_calories += meal['calories']
        except KeyError:
            print(f"Item '{item}' not found")
    return total_calories


def comp_cal_counter2(*list_of_items):

    total_calories = 0
    for item in list_of_items:
        try:
            if item in meal_dist_by_id:
                total_calories += meal_dist_by_id[item]['calories']
            elif item in meal_dist_by_name:
                total_calories += meal_dist_by_name[item]['calories']
            elif item in combo_dist_by_id:
                for combo_item in combo_dist_by_id[item]['meals']:
                    total_calories += meal_dist_by_id[combo_item]['calories']
            else:
                for combo_item in combo_dist_by_name[item]['meals']:
                    total_calories += meal_dist_by_id[combo_item]['calories']

        except KeyError:
            print(f"Item '{item}' not found 2")

    # for item in list_of_items:
    #     try:
    #         for meal in meal_dist:
    #             if item in meal:
    #                 total_calories += meal_dist[item]['calories']
    #     except KeyError:
    #         print(f"Item {item} not found")
    return total_calories
