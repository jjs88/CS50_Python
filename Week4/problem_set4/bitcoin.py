import sys
import requests

def valid_bitcoin(args:str):
    try:
        if len(args) == 1:
            sys.exit("Missing command-line argument")
        
        float(args[1])

    except ValueError:
        sys.exit("Command-line argument is not a number")

    return float(args[1])

def call_api():
    data = {}
    try:
        req = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

        if req.status_code == 200:
            data = req.json()
        else:
            sys.exit("Unable to make API Request")
    
    except requests.RequestException:
        sys.exit("Error with API Request")
    
    return data

def calc_current_cost(bitcoin_amount:float, rate:float):
    cost:str = format(bitcoin_amount * rate, ",.4f")
    return '$' + cost


def main():
    args = sys.argv
    bitcoin:float = valid_bitcoin(args)
    api_data = call_api()
    current_usd_rate:float = api_data["bpi"]["USD"]["rate_float"]
    print(calc_current_cost(bitcoin, current_usd_rate))

main()