
month_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():

    while True:
        user_val:str = input("Date: ")

        if user_val.find('/') != -1:
            month, day, year = user_val.split('/')
            
            if int(month) <= 12 and int(day) <= 31:
                print(f"{year}-{int(month):02}-{int(day):02}")
                break
                 
        elif user_val.find(',') != -1:
            month, day, year = user_val.split(' ')
            day = day.replace(',', '')
            
            if month in month_list and int(day) <= 31:
                month_num = month_list.index(month) + 1
                print(f"{year}-{int(month_num):02}-{int(day):02}")
                break
main()