

prompt:str = input("Expression: ")
prompt = prompt.split(" ")
x:int = prompt[0]
y:str = prompt[1]
z:int = prompt[2]
result:float

def operation(x:int,y:str,z:int):
    if y == "+":
        return int(x) + int(z)
    elif y == '-':
        return int(x) - int(z)
    elif y == '/':
        return int(x) / int(z)
    elif y == '*':
        return int(x) * int(z)
    else:
        return 0.00

result = "%.1f" % operation(x,y,z)
print(result)



