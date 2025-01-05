


def snake_case(word:str):
    new_word:str = ""

    for letter in word:
        if word.index(letter) == 0 and letter == letter.capitalize():
            new_word += letter.lower()

        elif letter == letter.capitalize() and word.index(letter) != 0:
            new_word +=  "_" + letter.lower()

        else:
            new_word += letter

    return new_word

def main():
    word:str = input("Enter a word: ")
    print(snake_case(word))

main()