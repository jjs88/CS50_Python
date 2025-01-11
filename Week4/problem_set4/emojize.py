import emoji


def main():
    prompt = input("")


    if prompt.find("_") == -1:
        print("_ not found")
        print(emoji.emojize(prompt, language='alias'))
    else:
        new_text = prompt.replace(":earth_asia:", ":globe_showing_Asia-Australia:")
        print(emoji.emojize(new_text, language='en'))

main()