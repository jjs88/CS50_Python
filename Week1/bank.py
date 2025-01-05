

greeting:str = input("Greeting: ")
greeting = greeting.strip().lower()

if greeting[:5] == "hello":
    print("$0")
elif greeting[:1] == "h" and greeting[:2] != "e":
    print("$20")
else:
    print("$100")