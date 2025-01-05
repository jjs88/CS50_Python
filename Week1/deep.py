

prompt:str = "What is the Answer to the Great Question of Life, the Universe, and Everything? "
result:str = input(prompt)
result = result.lower().replace("-", " ").strip()

if result == "42" or result == "forty two":
    print("Yes")
else:
    print("No")