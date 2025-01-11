
def get_fruit_calories(fruit:str):
    calories:str = ""
    fruit_list:list = [
        {"name": "apple", "calories": 130},
        {"name": "avocado", "calories": 50},
        {"name": "sweet cherries", "calories": 100},
        {"name": "kiwifruit", "calories": 90},
        {"name": "pear", "calories": 100}
   ]

    for item in fruit_list:
        if fruit.lower() == item["name"]:
            calories = item["calories"]
            break

    return calories if calories != "" else ""

def main():
    value = input("Item: ")
    result = get_fruit_calories(value)
    if result != "":
        print(f"Calories: {result}")
    else:
        print()

main()