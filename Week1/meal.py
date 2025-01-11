
def main():
    prompt:str = input("What time is it? ")
    result:float = convert(prompt)

    if result >= 18.00 and result <= 19.00:
        print("dinner time")
    elif result >= 12.00 and result <= 13.00:
        print("lunch time")
    elif result >= 7.00 and result <= 8.00:
        print("breakfast time")
    else:
        print("")




def convert(time:str):
    hours, minutes = time.split(":")
    hours_into_seconds = int(hours) * 3600
    minutes_into_seconds = int(minutes) * 60
    total_seconds_into_hours:float = (hours_into_seconds + minutes_into_seconds) / 3600

    return total_seconds_into_hours

if __name__  == "__main__":
    main()