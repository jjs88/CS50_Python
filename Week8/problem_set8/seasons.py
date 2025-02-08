from datetime import date
import sys
import re
import datetime
import inflect

def parse_birth_date(birth_date:str):
    #make sure date is in YYYY-MM-DD format
    if re.search(r"^\d{4}+\-+\d{2}+\-+\d{2}", birth_date):
        year, month, day = birth_date.split('-')
        if int(month) not in range(1, 13):
            sys.exit("Invalid Date")
        if int(day) not in range(1,32):
            sys.exit("Invalid Date")
    else:
        sys.exit("Invalid Date")
    return int(year), int(month), int(day)

def age_in_minutes(year:int, month:int, day:int):
    birth_date = datetime.date(year, month, day)
    todays_date = datetime.date.today()
    time_difference = todays_date - birth_date
    minutes = int(abs(time_difference.total_seconds()/60))
    return minutes

def minutes_to_english(minutes:int):
    p = inflect.engine()
    number_to_english:str = p.number_to_words(minutes).capitalize()
    new_number_to_english = number_to_english.replace(" and ", " ")
    return f"{new_number_to_english} minutes"

    
def main():
    year, month, day = parse_birth_date(input("Date of Birth: ").strip())
    minutes = age_in_minutes(year, month, day)
    print(minutes_to_english(minutes))




if __name__ == "__main__":
    main()