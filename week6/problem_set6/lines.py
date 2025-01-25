import sys

def argument_check(args:list):
    if len(args) == 1:
        sys.exit("Too few command-line arguments")

    elif len(args) > 2:
        sys.exit("Too many command-line arguments")

def is_python_file(file:str):
    extension:str = file.split('.')[-1]

    if extension == str("py"):
        return True
    else:
        sys.exit("Not a Python file")

def has_whitespace(row:str):
    if row.isspace():
        return True
    else:
        return False

def has_comments(row:str):
    if row.strip().startswith("#"):
        return True
    else:
        return False

def read_file(file_name:str):
    try:
        valid_count:int = 0

        with open(file_name) as file:
            for row in file:
                if has_whitespace(row) or has_comments(row):
                    pass
                else:
                    valid_count = valid_count + 1

        return valid_count

    except FileNotFoundError:
        sys.exit("File does not exist")


def main():
    args:list = sys.argv
    argument_check(args)
    file:str = args[-1]

    if is_python_file(file) == True:
        lines:int = read_file(file)
        print(lines)

main()