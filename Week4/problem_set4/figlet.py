from pyfiglet import Figlet
import sys as sys
import random
import string

def main():
    figlet = Figlet()

    valid_fonts = ["slant", "rectangles", "alphabet"]
    valid_flags = ["-f"]

    #if zero, print a random text of letters
    if(len(sys.argv) == 1):
        random_text = "".join(random.choices(string.ascii_letters, k=10))
        print(figlet.renderText(random_text))

    #2 if the user wants specific font
    elif(len(sys.argv) == 3):
        font_style = sys.argv[2]
        flag = sys.argv[1]

        if font_style in valid_fonts and flag in valid_flags:
            figlet.setFont(font=font_style)
            user_text = input("Input: ")

            print(figlet.renderText(user_text))
        else:
            str(sys.exit("Invalid Usage"))

    else:
        str(sys.exit("Invalid Usage"))


main()
