
#test.txt.pdf
def media_type(arg:str):
    extension:str = ""
    arg = arg.split(".")

    if(len(arg) == 2):
        extension = arg[1]
    elif(len(arg) == 3):
        extension = arg[2]
    else:
        extension = ""

    match extension:
        case "png":
            print(f"image/png")
        case "gif":
            print(f"image/gif")
        case "jpg" | "jpeg":
            print(f"image/jpeg")
        case "pdf":
            print(f"application/pdf")
        case "txt":
            print(f"text/plain")
        case "zip":
            print(f"application/zip")
        case _:
            print("application/octet-stream")

def main():
    prompt:str = input("File Name: ")
    prompt = prompt.strip().lower()
    media_type(prompt)

main()