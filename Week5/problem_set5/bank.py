def main():
    greeting:str = input("Greeting: ")
    print(value(greeting))


def value(greeting):
    greeting = greeting.strip().lower()

    if greeting[:5] == "hello":
        return 0
    elif greeting[:1] == "h" and greeting[:5] != "hello":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()