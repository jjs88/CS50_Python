import csv
import sys

def get_args(args:list):
    if len(args) < 3:
        sys.exit("Too few command-line arguments")
    elif len(args) > 3:
        sys.exit("Too many command-line arguments")
    return args

def cleanse_file(file_name:str):
    try:
        cleansed_data = []
        with open(file_name) as file:
            reader = csv.DictReader(file)
            for row in reader:
                last, first = row["name"].split(",")
                cleansed_data.append({"first": first.strip(), "last": last.strip(), "house": row["house"]})

            return cleansed_data

    except FileNotFoundError:
        sys.exit(f"Could not read {file_name}")

def write_to_file(data:list, file_name:str):
    with open(file_name, 'w', newline='') as output_file:
        fieldnames = ['first', 'last', 'house']
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()

        for row in data:
            record = {"first": row["first"], "last": row["last"], "house": row["house"]}
            writer.writerow(record)

def main():
    args = get_args(sys.argv)
    source_file_name:str = args[1]
    output_file_name:str = args[2]

    cleansed_data:list = cleanse_file(source_file_name)
    write_to_file(cleansed_data, output_file_name)




if __name__ == "__main__":
    main()