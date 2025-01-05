
#turn what the user inputs into all lowercase and then print the result
def indoor(arg:str):
    arg = arg.lower()
    print(f"{arg}")

def main():
    output = input("What would you like to say? ")    
    indoor(output)

main()