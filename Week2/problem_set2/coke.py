



def coke_machine():
    coin:int = 0
    bottle_price:int = 50
    total_inserted:int = 0

    while total_inserted < 50:
        print(f"Amount Due: {int(bottle_price) - int(total_inserted)}")
        coin = input("Insert Coin: ")

        if int(coin) == 25 or int(coin) == 10 or int(coin) == 5:
            total_inserted = int(total_inserted) + int(coin)

    print(f"Change Owed: {abs(int(bottle_price) - int(total_inserted))}")
    
    
def main():
    coke_machine()

main()