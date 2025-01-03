

# print("hello world")

# input("what is your name?")

# name = input("What is your name?")
# print(f"Your name is: {name}")
# print(f" \"Hello\" {name}  ")




#stripping whitespace
# name = input("What is your name?")
# name = name.strip()
# print(f"Nice to meet you, {name}")


#integers
# x = input("Enter a number")
# y = input("Enter another number")
# x = x.strip()
# y = y.strip()
# print(f"You entered: {x} and {y}") 

#functions
# def hello(arg:str="World"):
#     print(f"Hello, {arg}")

# hello()


#using main as script entry point
def main():
    name = input("What is your name?")

    def hello(arg):
        arg = arg.strip()
        print(f"Hello, {arg}")
    
    hello(name)

main()


