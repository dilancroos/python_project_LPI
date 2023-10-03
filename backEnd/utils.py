from .constants import calories, combos

def calories_counter(*args):

    total_calories = 0

    for item in args:
        try: 
            if item in calories:
                total_calories += calories[item]
            else:
                for combo_item in combos[item]:
                    total_calories += calories[combo_item]

        except:
            raise Exception("Item not found")
    # print([calories[item] for item in items])
    return total_calories