import sys
import csv
from tabulate import tabulate

def get_file_name(args:list):
    #check if correct # of args
    if len(args) < 2:
        sys.exit("Too few command-line arguments")
    elif len(args) > 2:
        sys.exit("Too many command-line arguments")
    
    #check if argument ends with .csv
    if args[1].find(".") != -1:
        file_name, extension = args[1].split(".")
        if extension != "csv":
            sys.exit("Not a CSV file")
    else:
        sys.exit("Not a csv file")
    
    return args[1]

def main():
    file_name:str = get_file_name(sys.argv)

    try:
        data:list = []
        with open(file_name) as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)


            table = data

            print(tabulate(table, headers="keys", tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()