
def add_or_update_grocery_list(item:str, grocery_list:dict):
    if item in grocery_list:
        grocery_list[item] += 1
    else:
        grocery_list[item] = 1

def grocery_list_sorted_capitalized(grocery_list:dict):
    for key in sorted(grocery_list):
        print(f"{grocery_list[key]} {key.upper()}")

def main():
    grocery_list:dict = {}

    while True:
        try:
            user_val:str = input(" ").lower()
            add_or_update_grocery_list(user_val, grocery_list)
                     
        except KeyboardInterrupt:
            print("", end="\n")
            grocery_list_sorted_capitalized(grocery_list)
            break
        except ValueError:
            print("Invalid list item, must be string")
main()