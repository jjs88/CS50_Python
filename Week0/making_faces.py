
def convert(arg:str):
    slightly_smiling = "\N{slightly smiling face}"
    slightly_frowning = "\N{slightly frowning face}"
    arg = arg.strip().replace(":)", slightly_smiling).replace(":(", slightly_frowning)
    print(f"{arg}")

def main():
    result:str = input(f"Enter Something ")
    convert(result)

main()