import sys
import csv
from PIL import Image, ImageOps

def validate_and_parse_args(args:list):
    #proper number of args passed in
    if len(args) < 3:
        sys.exit("Too few command-line arguments ")
    elif len(args) > 3:
        sys.exit("Too many command-line arguments")

    #input/out have different extensions
    valid_args:list = args[1:]
    valid_format:list = ["jpeg", "png", "jpg"]
    name1, ext1 = args[1].split(".")
    name2, ext2 = args[2].split(".")

    if ext1 != ext2:
        sys.exit("Input and output have different extensions")
    if ext1 and ext2 not in valid_format:
        sys.exit("Invalid output")
    return valid_args

def overlay_shirt_to_image(photo:str, changed_photo:str):
    try:
        shirt = Image.open("shirt.png")
        photo = Image.open(photo)
        #get size of the shirt
        size = shirt.size
        #resize the photo to be same size as the shirt
        cropped = ImageOps.fit(image=photo, size=size)
        #overlay shirt onto the photo then save file
        cropped.paste(shirt, shirt)
        cropped.save(changed_photo)
    except FileNotFoundError:
        sys.exit("Input does not exist")
    
def main():
    photo, changed_photo_name = validate_and_parse_args(sys.argv)
    overlay_shirt_to_image(photo, changed_photo_name)

if __name__ == "__main__":
    main()