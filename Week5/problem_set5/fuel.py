import math

def main():
    value = input("Fraction: ")
    convert(value)

def convert(fraction):
    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)

        if y == 0:
            raise ZeroDivisionError
        
        elif x > y:
            raise ValueError
        
        result:int = math.floor(int(x) / int(y) * 100)
        
        return result

    
    except ValueError:
        raise ValueError("Value error")
    except ZeroDivisionError:
        raise ZeroDivisionError("Divide by zero error")


def gauge(percentage:int):

    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()