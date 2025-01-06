


def get_fruit_calories(fruit:str):
    calories:str = ""
    fruit_list:list = [
        {"name": "apple", "calories": 130},
        {"name": "avocado", "calories": 50},
        {"name": "sweet cherries", "calories": 100}
   ]

    for item in fruit_list:
        if fruit.lower() == item["name"]:
            calories = item["calories"]
            break

    return calories if calories != "" else ""

def main():
    value = input("Item: ")
    calories = get_fruit_calories(value)
    print(f"Calories: {calories}")

main()