

def denom_greater_than_num(x:str, y:str):
    if int(x) > int(y):
        raise Exception("x is greater than than y!")
    else:
        return True
    
def fuel_calculation(fuel:float):
    if fuel >= .99:
        print("F")
    elif fuel == .75:
        print("75%")
    elif fuel == .67:
        print("67%")
    elif fuel == .50:
        print("50%")
    elif fuel == .33:
        print("33%")
    elif fuel == .25:
        print("25%")
    elif fuel <= .01:
        print("E")
    else:
        print()

def main():
    while True:
        try:
            value = input("Fraction: ")
            x, y = value.split("/")
            result:float = int(x) / int(y)
            result_two_decimal:float = f"{result:.2f}"
            # print(result_two_decimal)
            
            #if passes the division above, continue on
            denom_greater_than_num(x,y)
            fuel_calculation(float(result_two_decimal))

        except ValueError:
            print("values are not ints")
        except ZeroDivisionError:
            print("divide by zero error")
        except Exception as e:
            print(f"{e}")
        else:
            break

main()