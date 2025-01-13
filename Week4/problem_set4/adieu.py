import inflect

def main():
    p = inflect.engine()
    names:list = []
    phrase:str = "Adieu, adieu, to "
    names_clean:str = ""

    while True:
        try:
            prompt = input("Name: ")
            names.append(prompt)

        except (KeyboardInterrupt, EOFError):
            print("", end="\n")
            names_clean = p.join(names)
            print(phrase + names_clean)
            break
main()