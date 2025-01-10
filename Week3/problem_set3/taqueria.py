
def get_menu():
    return {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }   


def main():

    menu:list = get_menu()
    total_price:float = 0
    item_price:float = 0

    while True:
        try:
            val = input("Item: ").title()
            item_price = menu[val]
            total_price = total_price + item_price
            formatted_total_price = "{:.2f}".format(total_price)
            print(f"Total: {formatted_total_price}")

        except KeyError:
            print("Menu item is not available, please try again")
        except KeyboardInterrupt:
            print("", end="\n")
            break

main()