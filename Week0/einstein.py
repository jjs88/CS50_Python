

mass:int = input("Please enter Mass as an integer ")

def formula(arg:int):
    speed_of_light = int(300000000 ** 2)
    result:int= int(arg) * speed_of_light
    print(result)
    
formula(mass)