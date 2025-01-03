
#Take users input and replace each space with 3 dots
def playback_speed(arg:str):
        arg = arg.replace(" ", "...")
        print(f"{arg}")

def main():
    result = input("Enter Something ")
    result = result.strip()
    playback_speed(result)

main()