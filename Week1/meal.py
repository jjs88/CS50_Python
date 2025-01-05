
def main():
    prompt:str = input("What time is it? ")
    convert(prompt)

def convert(time:str):
    hours, minutes = time.split(":")
    hours_into_seconds = int(hours) * 3600
    minutes_into_seconds = int(minutes) * 60
    total_seconds_into_hours:float = (hours_into_seconds + minutes_into_seconds) / 3600

    if total_seconds_into_hours >= 18.00 and total_seconds_into_hours <= 19.00:
        print("dinner time")
    elif total_seconds_into_hours >= 12.00 and total_seconds_into_hours <= 13.00:
        print("lunch time")
    elif total_seconds_into_hours >= 7.00 and total_seconds_into_hours <= 8.00:
        print("breakfast time")
    else:
        print("")


if __name__  == "__main__":
    main()