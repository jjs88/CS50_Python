def main():
    value = input("Plate: ")
    # print(starts_with_two_letters(value))
    # print(no_special_characters(value))
    # print(max_six_characters(value))
    # print(numbers_at_end(value))
    # print(first_number_not_zero(value))
    # print(no_numbers(value))
    # print(number_not_in_middle(value))
    if(is_valid(value)):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate:str):
    if no_special_characters(plate) and starts_with_two_letters(plate) and max_six_characters(plate) and no_numbers(plate):
        return True
    elif no_special_characters(plate) and starts_with_two_letters(plate) and max_six_characters(plate) and numbers_at_end(plate) and first_number_not_zero(plate) and number_not_in_middle(plate):
        return True
    else:
        return False

def number_not_in_middle(plate:str):
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    result:bool = True
    rest_of_plate:str = ""

    for p in range(len(plate)):
        if p + 1 != len(plate) and plate[p] in numbers: # if number found and not the last one
            if plate[p+1] not in numbers: #check if next char not a number
                result = False
                break
    
    return result
        
def no_numbers(plate:str):
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    result:bool = True

    for i in plate:
        if i in numbers:
            result = False
            break
    
    return result

def starts_with_two_letters(plate:str):
    first_letter:str = ""
    second_letter:str = ""
    
    if len(plate) > 1:
        first_letter, second_letter = plate[:2]
    else:
        return False

    if first_letter.isalpha() and second_letter.isalpha:
        return True
    else:
        return False
    
def no_special_characters(plate:str):
    special_chars:list = ['!',' ', '.', '_']
    is_valid:str = ""

    for i in plate:
        if i in special_chars:
            is_valid = "False"
            break
    
    return False if is_valid == "False" else True

def max_six_characters(plate:str):
    return True if len(plate) <= 6 else False

def numbers_at_end(plate:str):
    max_number_pos:int = 0

    for i in range(len(plate)):
        if plate[i].isnumeric():
            max_number_pos = i + 1

    return True if int(max_number_pos) == len(plate) else False


def first_number_not_zero(plate:str):
    numbers:list = []

    for i in plate:
        if i.isnumeric():
            numbers.append(i)

    return False if int(numbers[0]) == 0 else True


if __name__ == "__main__":
    main()
