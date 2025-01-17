def main():
    value = input("Input: ")
    print(f"{shorten(value)}")


def shorten(word:str):
    vowels:list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    new_text:str = ""

    for letter in word:
        if letter in vowels:
            new_text += ""
        else:
            new_text += letter

    return new_text


if __name__ == "__main__":
    main()
