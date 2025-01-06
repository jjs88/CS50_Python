

def remove_vowels(text:str):
    vowels:list = ['a', 'e', 'i', 'o', 'u']
    new_text:str = ""

    for letter in text:
        if letter.lower() in vowels:
            new_text += ""
        else:
            new_text += letter
    
    return new_text


def main():
    value = input("Input: ")
    print(f"{remove_vowels(value)}")

main()