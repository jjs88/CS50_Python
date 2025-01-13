import random
import sys

def get_game_level():
    game_level:int = 0
    while True:
        try:
            prompt:int = int(input("Level: "))

            if prompt <= 0:
                pass
            else:
                game_level = prompt
                break
        except ValueError:
            pass
    return game_level

def guess_number(winning_number:int):
    while True:
        try:
            prompt:int = int(input("Guess: "))

            if prompt < 0:
                pass
            elif prompt < winning_number:
                print("Too small!")
            elif prompt > winning_number:
                print("Too large!")
            else:
                print("Just right!")
                break
        
        except ValueError:
            pass


def main():
    level:int = get_game_level()
    winning_number:int = random.randint(1, level)
    guess_number(winning_number)
    sys.exit()
    
main()